#!/usr/bin/env python

#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

import argparse, datetime, re
import glob, json, os, subprocess
from mako.template import Template
from mako.lookup import TemplateLookup

repo = 'https://github.com/unicode-org/cldr-json.git'

files = {
	'python': 'jakarta/generated.py',
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
	return rule.strip()

def gen_form(cldr):
	output = {
		'part0': {},
		'part1': {},
	}

	if 'plurals-type-cardinal' in cldr.keys():
		cldr_type = 'plurals-type-cardinal'
		output['func_name'] = 'plural_form'
	if 'plurals-type-ordinal' in cldr.keys():
		cldr_type = 'plurals-type-ordinal'
		output['func_name'] = 'ordinal_form'

	for lang, data in cldr[cldr_type].items():
		for form, rule in data.items():
			part = 'part0' if '-' in lang else 'part1'
			form = form[17:]
			if part == 'part0' or form != 'other':
				if lang not in output[part]:
					output[part][lang] = {}
				rule = rewrite_rule(rule)
				output[part][lang][form] = rule

	return output

### samples

def extract_samples(lang, data):
	samples = []
	for form, sample in data.items():
		if n:= number_re.search(sample.split(' @')[1]):
			number = float(n.group(1))
			if number == 0 and n.group(2) != '': number = float(n.group(2))
			if number == int(number): number = int(number)
			samples.append((form[17:], number))
	return samples

def gen_samples(cldr):
	output = {
		'part0': {},
		'part1': {},
	}

	if 'plurals-type-cardinal' in cldr.keys():
		cldr_type = 'plurals-type-cardinal'
		output['func_name'] = 'plural_samples'
	if 'plurals-type-ordinal' in cldr.keys():
		cldr_type = 'plurals-type-ordinal'
		output['func_name'] = 'ordinal_samples'

	for lang, data in cldr[cldr_type].items():
		for form, rule in data.items():
			part = 'part0' if '-' in lang else 'part1'
			if part == 'part0' or form != 'other':
				output[part][lang] = extract_samples(lang, data)

	return output

### format number

def gen_number_symbols(directory):
	output = {
		'part0': {},
		'part1': {},
	}

	for path in glob.iglob(directory + '/*'):
		lang = os.path.basename(path)
		part = 'part0' if '-' in lang else 'part1'
		f = open(os.path.sep.join([path, 'numbers.json']))
		symbols = json.load(f)['main'][lang]['numbers']['symbols-numberSystem-latn']
		output[part][lang] = {
			'decimal': symbols['decimal'],
			'group': symbols['group'],
		}

	return output

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('proglang')
	args = parser.parse_args()

	repo_clone_update()

	plurals_file = '.cldr-json/cldr-json/cldr-core/supplemental/plurals.json'
	ordinals_file = '.cldr-json/cldr-json/cldr-core/supplemental/ordinals.json'
	plurals = json.load(open(plurals_file))['supplemental']
	ordinals = json.load(open(ordinals_file))['supplemental']
	numbers_dir = '.cldr-json/cldr-json/cldr-numbers-modern/main'

	templates = TemplateLookup(directories=['templates'])
	template = templates.get_template(args.proglang + '.mako')
	f = open(files[args.proglang], 'w')

	f.write(template.render(**{
		'datestamp': datetime.date.today(),
		'plural_form': gen_form(plurals),
		'ordinal_form': gen_form(ordinals),
		'plural_samples': gen_samples(plurals),
		'ordinal_samples': gen_samples(ordinals),
		'number_symbols': gen_number_symbols(numbers_dir),
	}))
