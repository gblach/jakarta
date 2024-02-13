#!/usr/bin/env python

#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

import argparse, datetime, re
import glob, json, os, subprocess

repo = 'https://github.com/unicode-org/cldr-json.git'

files = {
	'python': 'jakarta/generated.py',
}

syntax = {
	'python': {
		'func_begin_lang_n_str': 'def {}(lang: str, n: float) -> str:',
		'func_begin_lang_list': 'def {}(lang: str) -> list:',
		'func_begin_lang_dict': 'def {}(lang: str) -> dict:',
		'n_to_i': 'i = int(n)',
		'plurals_math': [
			'if i == n:',
			'\tf = t = v = w = 0',
			'else:',
			'\tfstr = str(n).split(".")[1]',
			'\tf = t = int(fstr)',
			'\tv = w = len(fstr)',
			'c = e = 0',
		],
		'lang_replace': 'lang = lang.replace("_", "-")',
		'lang_cut': 'lang = lang.split("-")[0]',
		'if_lang': 'if lang == "{}":',
		'elif_lang': 'elif lang == "{}":',
		'if_rule': 'if {}:',
		'return_str': 'return "{}"',
		'return_list': 'return {}',
		'return_map': 'return {}',
		'block_end': '',
		'comment': '#',
	},
}

list_re = re.compile(r'([a-z](\s%\s\d+)*) ([!=]+) ([\d\.]+(\,[\d\.]+)+)')
range_eq_re = re.compile(r'([a-z](\s%\s\d+)*) == (\d+)\.\.(\d+)')
range_eq_sub = r'(\3 <= \1 and \1 <= \4)'
range_ne_re = re.compile(r'([a-z](\s%\s\d+)*) != (\d+)\.\.(\d+)')
range_ne_sub = r'(\1 < \3 or \4 < \1)'
eq_re = re.compile(r' == ([\((range)])')
eq_sub = r' in \1'
ne_re = re.compile(r' != ([\((range)])')
ne_sub = r' not in \1'
number_re = re.compile(r'([\d\.]+)[\~\,\s]*([\d\.]*)')

def repo_clone_update():
	if not os.path.isdir('.cldr-json'):
		subprocess.run(['git', 'clone', '--depth', '1', repo, '.cldr-json'], check=True)
	else:
		os.chdir('.cldr-json')
		subprocess.run(['git', 'pull'], check=True)
		os.chdir('..')

### form

def rewrite_rule(rule):
	rule = rule.split(' @')[0].replace(' = ', ' == ')
	while m := list_re.search(rule):
		sub = ''
		for part in m.group(4).split(','):
			if sub: sub += ' or '
			sub += fr'\1 \3 {part}'
		sub = f'({sub})'
		rule = list_re.sub(sub, rule, 1)
	rule = range_eq_re.sub(range_eq_sub, rule)
	rule = range_ne_re.sub(range_ne_sub, rule)
	rule = eq_re.sub(eq_sub, rule)
	rule = ne_re.sub(ne_sub, rule)
	return rule

def write_form(f, s, cldr):
	cldr_type = func_name = ''
	if 'plurals-type-cardinal' in cldr.keys():
		cldr_type = 'plurals-type-cardinal'
		func_name = 'plural_form'
	if 'plurals-type-ordinal' in cldr.keys():
		cldr_type = 'plurals-type-ordinal'
		func_name = 'ordinal_form'

	f.write(s['func_begin_lang_n_str'].format(func_name) + '\n')
	f.write('\t' + s['n_to_i'] + '\n')
	if cldr_type == 'plurals-type-cardinal':
		for line in s['plurals_math']:
			f.write('\t' + line + '\n')

	f.write('\t' + s['lang_replace'] + '\n')
	for lang, data in cldr[cldr_type].items():
		if '-' in lang:
			f.write('\t' + s['if_lang'].format(lang) + '\n')
			for form, rule in data.items():
				rule = rewrite_rule(rule)
				if rule: f.write('\t\t' + s['if_rule'].format(rule) + ' ')
				else: f.write('\t\t')
				f.write(s['return_str'].format(form[17:]) + '\n')

	i = 0
	f.write('\t' + s['lang_cut'] + '\n')
	for lang, data in cldr[cldr_type].items():
		if '-' not in lang and len(data) > 1:
			if i == 0: f.write('\t' + s['if_lang'].format(lang) + '\n')
			else: f.write('\t' + s['elif_lang'].format(lang) + '\n')
			for form, rule in data.items():
				if form[17:] != 'other':
					rule = rewrite_rule(rule)
					f.write('\t\t' + s['if_rule'].format(rule) + ' ')
					f.write(s['return_str'].format(form[17:]) + '\n')
			i += 1

	f.write('\t' + s['return_str'].format('other') + '\n')
	f.write(s['block_end'] + '\n')

### samples

def get_samples(lang, data):
	samples = []
	for form, sample in data.items():
		if n:= number_re.search(sample.split(' @')[1]):
			number = float(n.group(1))
			if number == 0 and n.group(2) != '': number = float(n.group(2))
			if number == int(number): number = int(number)
			samples.append((form[17:], number))
	return samples

def write_samples(f, s, cldr):
	cldr_type = func_name = ''
	if 'plurals-type-cardinal' in cldr.keys():
		cldr_type = 'plurals-type-cardinal'
		func_name = 'plural_samples'
	if 'plurals-type-ordinal' in cldr.keys():
		cldr_type = 'plurals-type-ordinal'
		func_name = 'ordinal_samples'

	f.write(s['func_begin_lang_list'].format(func_name) + '\n')

	f.write('\t' + s['lang_replace'] + '\n')
	for lang, data in cldr[cldr_type].items():
		if '-' in lang:
			samples = get_samples(lang, data)
			f.write('\t' + s['if_lang'].format(lang) + ' ')
			f.write(s['return_list'].format(samples) + '\n')

	f.write('\t' + s['lang_cut'] + '\n')
	for lang, data in cldr[cldr_type].items():
		if '-' not in lang:
			samples = get_samples(lang, data)
			f.write('\t' + s['if_lang'].format(lang) + ' ')
			f.write(s['return_list'].format(samples) + '\n')

	f.write('\t' + s['return_list'].format([]) + '\n')
	f.write(s['block_end'] + '\n')

### format number

def get_number_symbols(lang, path):
	file = os.path.sep.join([path, 'numbers.json'])
	symbols = json.load(open(file))['main'][lang]['numbers']['symbols-numberSystem-latn']
	return {
		'decimal': symbols['decimal'],
		'group': symbols['group'],
	}

def write_number_symbols(f, s, directory):
	f.write(s['func_begin_lang_dict'].format('number_symbols') + '\n')

	f.write('\t' + s['lang_replace'] + '\n')
	for path in glob.iglob(directory + '/*'):
		lang = os.path.basename(path)
		if '-' in lang:
			symbols = get_number_symbols(lang, path)
			f.write('\t' + s['if_lang'].format(lang) + ' ')
			f.write(s['return_map'].format(symbols) + '\n')

	f.write('\t' + s['lang_cut'] + '\n')
	for path in glob.iglob(directory + '/*'):
		lang = os.path.basename(path)
		if '-' not in lang:
			symbols = get_number_symbols(lang, path)
			f.write('\t' + s['if_lang'].format(lang) + ' ')
			f.write(s['return_map'].format(symbols) + '\n')

	f.write(s['block_end'] + '\n')

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('syntax')
	args = parser.parse_args()

	if args.syntax in syntax:
		s = syntax[args.syntax]
	else:
		quit(1)

	repo_clone_update()

	f = open(files[args.syntax], 'w')
	f.write('%s  This Source Code Form is subject to the terms of the Mozilla Public\n'
		% s['comment'])
	f.write('%s  License, v. 2.0. If a copy of the MPL was not distributed with this\n'
		% s['comment'])
	f.write('%s  file, You can obtain one at https://mozilla.org/MPL/2.0/.\n\n' % s['comment'])
	f.write('%s %s\n\n' % (s['comment'], datetime.date.today()))

	plurals_file = '.cldr-json/cldr-json/cldr-core/supplemental/plurals.json'
	ordinals_file = '.cldr-json/cldr-json/cldr-core/supplemental/ordinals.json'
	plurals = json.load(open(plurals_file))['supplemental']
	ordinals = json.load(open(ordinals_file))['supplemental']

	write_form(f, s, plurals)
	write_form(f, s, ordinals)
	write_samples(f, s, plurals)
	write_samples(f, s, ordinals)
	write_number_symbols(f, s, '.cldr-json/cldr-json/cldr-numbers-modern/main')
