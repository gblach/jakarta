#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

import glob, os, re
import importlib.util
import ast_grep_py
import cdblib
from enum import Enum
from . import engines
from . import generated as gen

class Type(Enum):
	SIMPLE = 1
	PLURAL = 2
	ORDINAL = 3

class Tool:
	def __init__(self, config):
		self.config = config
		self.map = {}

	def load(self):
		f = open(self.config['jafile'])
		line_re = re.compile(r'([\w\.]+) = "(.+)"')
		for line in f.readlines():
			if m := line_re.match(line):
				(key, translation) = m.group(1, 2)
				if key in ('en', 'en.one', 'en.ord'):
					text = translation
					if key == 'en': _type = Type.SIMPLE
					elif key == 'en.one': _type = Type.PLURAL
					elif key == 'en.ord': _type = Type.ORDINAL
					self.map[text] = { '_type': _type, '_loc': [] }
				elif key == 'en.other':
					self.map[text]['_plural'] = translation
				elif '.' not in key:
					self.map[text][key] = translation
				else:
					(lang, form) = key.split('.')
					if lang not in self.map[text].keys():
						self.map[text][lang] = {}
					self.map[text][lang][form] = translation

	def extract(self):
		for src in self.config['sources']:
			for fn in glob.glob(src, recursive=True):
				code = open(fn).read()
				root = ast_grep_py.SgRoot(code, self.config['lang']).root()
				nodes = root.find_all(pattern='$O._($A)')
				self.extract_nodes(fn, nodes, Type.SIMPLE)
				nodes = root.find_all(pattern='$O.p($A, $B, $N)')
				self.extract_nodes(fn, nodes, Type.PLURAL)
				nodes = root.find_all(pattern='$O.o($A, $N)')
				self.extract_nodes(fn, nodes, Type.ORDINAL)

	def extract_nodes(self, fn, nodes, _type):
		for node in nodes:
			text = node.get_match('A').text().strip('\'"')
			if text not in self.map:
				self.map[text] = { '_type': _type, '_loc': [] }
			loc = f'{fn}:{node.range().start.line+1}'
			self.map[text]['_loc'].append(loc)
			if _type == Type.PLURAL:
				plural = node.get_match('B').text().strip('\'"')
				self.map[text]['_plural'] = plural

	def translate(self):
		translated = 0
		for text, data in self.map.items():
			if data['_type'] == Type.SIMPLE:
				for lang in self.config['translate-to']:
					if lang not in self.map[text]:
						self.translate_simple(lang, text)
						print('.', end='', flush=True)
						translated += 1
			elif data['_type'] == Type.PLURAL:
				plural = data['_plural']
				for lang in self.config['translate-to']:
					if lang not in self.map[text]:
						self.translate_plural(lang, text, plural)
						print('.', end='', flush=True)
						translated += 1
			elif data['_type'] == Type.ORDINAL:
				for lang in self.config['translate-to']:
					if lang not in self.map[text]:
						self.translate_oridnal(lang, text)
						print('.', end='', flush=True)
						translated += 1
		if translated: print('')

	def translate_simple(self, lang, text):
		translation = engines.translate(self.config, lang, text)
		if translation: self.map[text][lang] = translation

	def translate_plural(self, lang, text, plural):
		for (form, n) in gen.plural_rules(lang):
			if n == 1: translate = text.format(n)
			else: translate = plural.format(n)
			translation = engines.translate(self.config, lang, translate)
			if translation:
				if lang not in self.map[text]: self.map[text][lang] = {}
				self.map[text][lang][form] = translation \
					.replace(str(n), '{}') \
					.replace(str(n).replace('.', ','), '{}')

	def translate_oridnal(self, lang, text):
		for (form, n) in gen.ordinal_rules(lang):
			if n % 10 == 1 and n % 100 != 11: translate = text.format(f'{n}st')
			elif n % 10 == 2 and n % 100 != 12: translate = text.format(f'{n}nd')
			elif n % 10 == 3 and n % 100 != 13: translate = text.format(f'{n}rd')
			else: translate = text.format(f'{n}th')
			translation = engines.translate(self.config, lang, translate)
			if translation:
				if lang not in self.map[text]: self.map[text][lang] = {}
				self.map[text][lang][form] = translation \
					.replace(str(n), '{}') \
					.replace(str(n).replace('.', ','), '{}')

	def generate(self):
		f = open(self.config['jafile'], 'w')
		i = 0
		for text, data in self.map.items():
			for loc in data['_loc']:
				f.write(f'# {loc}\n')
			if not data['_loc']:
				f.write('# removed\n')
			if data['_type'] == Type.SIMPLE:
				f.write(f'en = "{text}"\n')
			elif data['_type'] == Type.PLURAL:
				plural = data['_plural']
				f.write(f'en.one = "{text}"\n')
				f.write(f'en.other = "{plural}"\n')
			elif data['_type'] == Type.ORDINAL:
				f.write(f'en.ord = "{text}"\n')
			for lang, data1 in data.items():
				if not lang.startswith('_'):
					if type(data1) is str:
						f.write(f'{lang} = "{data1}"\n')
					elif type(data1) is dict:
						for form, translation in data1.items():
							key = f'{lang}.{form}'
							f.write(f'{key} = "{translation}"\n')
			if 'translate-to' in self.config:
				self.generate_not_translated(f, data)
			i += 1
			if i < len(self.map):
				f.write('\n')

	def generate_not_translated(self, f, data):
		for lang in self.config['translate-to']:
			if data['_type'] == Type.SIMPLE:
				if lang not in data:
					f.write(f'{lang} = ""\n')
			elif data['_type'] == Type.PLURAL:
				if lang not in data: data[lang] = {}
				for (form, n) in gen.plural_rules(lang):
					if form not in data[lang].keys():
						f.write(f'{lang}.{form} = ""\n')
			elif data['_type'] == Type.ORDINAL:
				if lang not in data: data[lang] = {}
				for (form, n) in gen.ordinal_rules(lang):
					if form not in data[lang].keys():
						f.write(f'{lang}.{form} = ""\n')

	def compile(self):
		cdbfile = self.config['jafile'] + '.cdb'
		f = open(cdbfile, 'wb')
		cdb = cdblib.Writer(f)
		for text, data in self.map.items():
			for lang, data1 in data.items():
				if not lang.startswith('_'):
					if type(data1) is str:
						key = f'{lang}:{text}'.encode()
						cdb.put(key, data1.encode())
					elif type(data1) is dict:
						for form, translation in data1.items():
							key = f'{lang}.{form}:{text}'.encode()
							cdb.put(key, translation.encode())
		cdb.finalize()
		return cdbfile

	def main(self):
		if os.path.isfile(self.config['jafile']):
			self.load()
		self.extract()
		if 'translate-to' in self.config and 'translation-engine' in self.config:
			self.translate()
		self.generate()
		return self.compile()
