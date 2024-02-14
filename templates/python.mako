#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

#  ${datestamp}

% for cldr in [plural_form, ordinal_form]:
def ${cldr['func_name']}(lang: str, n: float) -> str:
	i = int(n)
% if cldr == plural_form:
	if i == n:
		f = t = v = w = 0
	else:
		fstr = str(n).split(".")[1]
		f = t = int(fstr)
		v = w = len(fstr)
	c = e = 0
% endif
	lang = lang.replace("_", "-")
% for lang, data in cldr['part0'].items():
	if lang == "${lang}":
% for form, rule in data.items():
% if rule:
		if ${rule}: return "${form}"
% else:
		return "${form}"
% endif
% endfor
% endfor
	lang = lang.split("-")[0]
% for lang, data in cldr['part1'].items():
% if lang == list(cldr['part1'].keys())[0]:
	if lang == "${lang}":
% else:
	elif lang == "${lang}":
% endif
% for form, rule in data.items():
% if rule:
		if ${rule}: return "${form}"
% endif
% endfor
% endfor
	return "other"
% if cldr == plural_form:

% endif
% endfor

% for cldr in [plural_samples, ordinal_samples]:
def ${cldr['func_name']}(lang: str) -> list:
	lang = lang.replace("_", "-")
% for lang, samples in cldr['part0'].items():
	if lang == "${lang}": return ${samples}
% endfor
	lang = lang.split("-")[0]
% for lang, samples in cldr['part1'].items():
	if lang == "${lang}": return ${samples}
% endfor
	return []
% if cldr == plural_samples:

% endif
% endfor

def number_symbols(lang: str) -> dict:
	lang = lang.replace("_", "-")
% for lang, symbols in number_symbols['part0'].items():
	if lang == "${lang}": return ${symbols}
% endfor
	lang = lang.split("-")[0]
% for lang, symbols in number_symbols['part1'].items():
	if lang == "${lang}": return ${symbols}
% endfor
