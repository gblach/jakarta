#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

import cdblib
from . import generated as gen

class Jakarta:
	def __init__(self, fn):
		data = open(fn, 'rb').read()
		self.map = cdblib.Reader(data)
		self.langs = []

	def set_langs(self, *langs):
		self.langs = langs

	def _(self, one):
		for lang in self.langs:
			key = f'{lang}:{one}'.encode()
			if key in self.map: return self.map[key].decode()
		return one

	def p(self, one, other, n):
		for lang in self.langs:
			form = gen.plural_form(lang, n)
			key = f'{lang}.{form}:{one}'.encode()
			if key in self.map: return self.map[key].decode().format(n)
		if n == 1: return one.format(n)
		return other.format(n)

	def o(self, one, n):
		for lang in self.langs:
			form = gen.ordinal_form(lang, n)
			key = f'{lang}.{form}:{one}'.encode()
			if key in self.map: return self.map[key].decode().format(n)
		if n % 10 == 1 and n % 100 != 11: return one.format(f'{n}st')
		elif n % 10 == 2 and n % 100 != 12: return one.format(f'{n}nd')
		elif n % 10 == 3 and n % 100 != 13: return one.format(f'{n}rd')
		return one.format(f'{n}th')
