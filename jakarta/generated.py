#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

#  2024-02-14

def plural_form(lang: str, n: float) -> str:
	i = int(n)
	if i == n:
		f = t = v = w = 0
	else:
		fstr = str(n).split(".")[1]
		f = t = int(fstr)
		v = w = len(fstr)
	c = e = 0
	lang = lang.replace("_", "-")
	if lang == "pt-PT":
		if i == 1 and v == 0: return "one"
		if e == 0 and i != 0 and i % 1000000 == 0 and v == 0 or (e < 0 or 5 < e): return "many"
		return "other"
	lang = lang.split("-")[0]
	if lang == "af":
		if n == 1: return "one"
	elif lang == "ak":
		if (0 <= n and n <= 1): return "one"
	elif lang == "am":
		if i == 0 or n == 1: return "one"
	elif lang == "an":
		if n == 1: return "one"
	elif lang == "ar":
		if n == 0: return "zero"
		if n == 1: return "one"
		if n == 2: return "two"
		if (3 <= n % 100 and n % 100 <= 10): return "few"
		if (11 <= n % 100 and n % 100 <= 99): return "many"
	elif lang == "ars":
		if n == 0: return "zero"
		if n == 1: return "one"
		if n == 2: return "two"
		if (3 <= n % 100 and n % 100 <= 10): return "few"
		if (11 <= n % 100 and n % 100 <= 99): return "many"
	elif lang == "as":
		if i == 0 or n == 1: return "one"
	elif lang == "asa":
		if n == 1: return "one"
	elif lang == "ast":
		if i == 1 and v == 0: return "one"
	elif lang == "az":
		if n == 1: return "one"
	elif lang == "bal":
		if n == 1: return "one"
	elif lang == "be":
		if n % 10 == 1 and n % 100 != 11: return "one"
		if (2 <= n % 10 and n % 10 <= 4) and (n % 100 < 12 or 14 < n % 100): return "few"
		if n % 10 == 0 or (5 <= n % 10 and n % 10 <= 9) or (11 <= n % 100 and n % 100 <= 14): return "many"
	elif lang == "bem":
		if n == 1: return "one"
	elif lang == "bez":
		if n == 1: return "one"
	elif lang == "bg":
		if n == 1: return "one"
	elif lang == "bho":
		if (0 <= n and n <= 1): return "one"
	elif lang == "blo":
		if n == 0: return "zero"
		if n == 1: return "one"
	elif lang == "bn":
		if i == 0 or n == 1: return "one"
	elif lang == "br":
		if n % 10 == 1 and (n % 100 != 11 or n % 100 != 71 or n % 100 != 91): return "one"
		if n % 10 == 2 and (n % 100 != 12 or n % 100 != 72 or n % 100 != 92): return "two"
		if ((3 <= n % 10 and n % 10 <= 4) or n % 10 == 9) and ((n % 100 < 10 or 19 < n % 100) or (n % 100 < 70 or 79 < n % 100) or (n % 100 < 90 or 99 < n % 100)): return "few"
		if n != 0 and n % 1000000 == 0: return "many"
	elif lang == "brx":
		if n == 1: return "one"
	elif lang == "bs":
		if v == 0 and i % 10 == 1 and i % 100 != 11 or f % 10 == 1 and f % 100 != 11: return "one"
		if v == 0 and (2 <= i % 10 and i % 10 <= 4) and (i % 100 < 12 or 14 < i % 100) or (2 <= f % 10 and f % 10 <= 4) and (f % 100 < 12 or 14 < f % 100): return "few"
	elif lang == "ca":
		if i == 1 and v == 0: return "one"
		if e == 0 and i != 0 and i % 1000000 == 0 and v == 0 or (e < 0 or 5 < e): return "many"
	elif lang == "ce":
		if n == 1: return "one"
	elif lang == "ceb":
		if v == 0 and (i == 1 or i == 2 or i == 3) or v == 0 and (i % 10 != 4 or i % 10 != 6 or i % 10 != 9) or v != 0 and (f % 10 != 4 or f % 10 != 6 or f % 10 != 9): return "one"
	elif lang == "cgg":
		if n == 1: return "one"
	elif lang == "chr":
		if n == 1: return "one"
	elif lang == "ckb":
		if n == 1: return "one"
	elif lang == "cs":
		if i == 1 and v == 0: return "one"
		if (2 <= i and i <= 4) and v == 0: return "few"
		if v != 0: return "many"
	elif lang == "cy":
		if n == 0: return "zero"
		if n == 1: return "one"
		if n == 2: return "two"
		if n == 3: return "few"
		if n == 6: return "many"
	elif lang == "da":
		if n == 1 or t != 0 and (i == 0 or i == 1): return "one"
	elif lang == "de":
		if i == 1 and v == 0: return "one"
	elif lang == "doi":
		if i == 0 or n == 1: return "one"
	elif lang == "dsb":
		if v == 0 and i % 100 == 1 or f % 100 == 1: return "one"
		if v == 0 and i % 100 == 2 or f % 100 == 2: return "two"
		if v == 0 and (3 <= i % 100 and i % 100 <= 4) or (3 <= f % 100 and f % 100 <= 4): return "few"
	elif lang == "dv":
		if n == 1: return "one"
	elif lang == "ee":
		if n == 1: return "one"
	elif lang == "el":
		if n == 1: return "one"
	elif lang == "en":
		if i == 1 and v == 0: return "one"
	elif lang == "eo":
		if n == 1: return "one"
	elif lang == "es":
		if n == 1: return "one"
		if e == 0 and i != 0 and i % 1000000 == 0 and v == 0 or (e < 0 or 5 < e): return "many"
	elif lang == "et":
		if i == 1 and v == 0: return "one"
	elif lang == "eu":
		if n == 1: return "one"
	elif lang == "fa":
		if i == 0 or n == 1: return "one"
	elif lang == "ff":
		if (i == 0 or i == 1): return "one"
	elif lang == "fi":
		if i == 1 and v == 0: return "one"
	elif lang == "fil":
		if v == 0 and (i == 1 or i == 2 or i == 3) or v == 0 and (i % 10 != 4 or i % 10 != 6 or i % 10 != 9) or v != 0 and (f % 10 != 4 or f % 10 != 6 or f % 10 != 9): return "one"
	elif lang == "fo":
		if n == 1: return "one"
	elif lang == "fr":
		if (i == 0 or i == 1): return "one"
		if e == 0 and i != 0 and i % 1000000 == 0 and v == 0 or (e < 0 or 5 < e): return "many"
	elif lang == "fur":
		if n == 1: return "one"
	elif lang == "fy":
		if i == 1 and v == 0: return "one"
	elif lang == "ga":
		if n == 1: return "one"
		if n == 2: return "two"
		if (3 <= n and n <= 6): return "few"
		if (7 <= n and n <= 10): return "many"
	elif lang == "gd":
		if (n == 1 or n == 11): return "one"
		if (n == 2 or n == 12): return "two"
		if ((3 <= n and n <= 10) or (13 <= n and n <= 19)): return "few"
	elif lang == "gl":
		if i == 1 and v == 0: return "one"
	elif lang == "gsw":
		if n == 1: return "one"
	elif lang == "gu":
		if i == 0 or n == 1: return "one"
	elif lang == "guw":
		if (0 <= n and n <= 1): return "one"
	elif lang == "gv":
		if v == 0 and i % 10 == 1: return "one"
		if v == 0 and i % 10 == 2: return "two"
		if v == 0 and (i % 100 == 0 or i % 100 == 20 or i % 100 == 40 or i % 100 == 60 or i % 100 == 80): return "few"
		if v != 0: return "many"
	elif lang == "ha":
		if n == 1: return "one"
	elif lang == "haw":
		if n == 1: return "one"
	elif lang == "he":
		if i == 1 and v == 0 or i == 0 and v != 0: return "one"
		if i == 2 and v == 0: return "two"
	elif lang == "hi":
		if i == 0 or n == 1: return "one"
	elif lang == "hr":
		if v == 0 and i % 10 == 1 and i % 100 != 11 or f % 10 == 1 and f % 100 != 11: return "one"
		if v == 0 and (2 <= i % 10 and i % 10 <= 4) and (i % 100 < 12 or 14 < i % 100) or (2 <= f % 10 and f % 10 <= 4) and (f % 100 < 12 or 14 < f % 100): return "few"
	elif lang == "hsb":
		if v == 0 and i % 100 == 1 or f % 100 == 1: return "one"
		if v == 0 and i % 100 == 2 or f % 100 == 2: return "two"
		if v == 0 and (3 <= i % 100 and i % 100 <= 4) or (3 <= f % 100 and f % 100 <= 4): return "few"
	elif lang == "hu":
		if n == 1: return "one"
	elif lang == "hy":
		if (i == 0 or i == 1): return "one"
	elif lang == "ia":
		if i == 1 and v == 0: return "one"
	elif lang == "io":
		if i == 1 and v == 0: return "one"
	elif lang == "is":
		if t == 0 and i % 10 == 1 and i % 100 != 11 or t % 10 == 1 and t % 100 != 11: return "one"
	elif lang == "it":
		if i == 1 and v == 0: return "one"
		if e == 0 and i != 0 and i % 1000000 == 0 and v == 0 or (e < 0 or 5 < e): return "many"
	elif lang == "iu":
		if n == 1: return "one"
		if n == 2: return "two"
	elif lang == "jgo":
		if n == 1: return "one"
	elif lang == "jmc":
		if n == 1: return "one"
	elif lang == "ka":
		if n == 1: return "one"
	elif lang == "kab":
		if (i == 0 or i == 1): return "one"
	elif lang == "kaj":
		if n == 1: return "one"
	elif lang == "kcg":
		if n == 1: return "one"
	elif lang == "kk":
		if n == 1: return "one"
	elif lang == "kkj":
		if n == 1: return "one"
	elif lang == "kl":
		if n == 1: return "one"
	elif lang == "kn":
		if i == 0 or n == 1: return "one"
	elif lang == "ks":
		if n == 1: return "one"
	elif lang == "ksb":
		if n == 1: return "one"
	elif lang == "ksh":
		if n == 0: return "zero"
		if n == 1: return "one"
	elif lang == "ku":
		if n == 1: return "one"
	elif lang == "kw":
		if n == 0: return "zero"
		if n == 1: return "one"
		if (n % 100 == 2 or n % 100 == 22 or n % 100 == 42 or n % 100 == 62 or n % 100 == 82) or n % 1000 == 0 and ((1000 <= n % 100000 and n % 100000 <= 20000) or n % 100000 == 40000 or n % 100000 == 60000 or n % 100000 == 80000) or n != 0 and n % 1000000 == 100000: return "two"
		if (n % 100 == 3 or n % 100 == 23 or n % 100 == 43 or n % 100 == 63 or n % 100 == 83): return "few"
		if n != 1 and (n % 100 == 1 or n % 100 == 21 or n % 100 == 41 or n % 100 == 61 or n % 100 == 81): return "many"
	elif lang == "ky":
		if n == 1: return "one"
	elif lang == "lag":
		if n == 0: return "zero"
		if (i == 0 or i == 1) and n != 0: return "one"
	elif lang == "lb":
		if n == 1: return "one"
	elif lang == "lg":
		if n == 1: return "one"
	elif lang == "lij":
		if i == 1 and v == 0: return "one"
	elif lang == "ln":
		if (0 <= n and n <= 1): return "one"
	elif lang == "lt":
		if n % 10 == 1 and (n % 100 < 11 or 19 < n % 100): return "one"
		if (2 <= n % 10 and n % 10 <= 9) and (n % 100 < 11 or 19 < n % 100): return "few"
		if f != 0: return "many"
	elif lang == "lv":
		if n % 10 == 0 or (11 <= n % 100 and n % 100 <= 19) or v == 2 and (11 <= f % 100 and f % 100 <= 19): return "zero"
		if n % 10 == 1 and n % 100 != 11 or v == 2 and f % 10 == 1 and f % 100 != 11 or v != 2 and f % 10 == 1: return "one"
	elif lang == "mas":
		if n == 1: return "one"
	elif lang == "mg":
		if (0 <= n and n <= 1): return "one"
	elif lang == "mgo":
		if n == 1: return "one"
	elif lang == "mk":
		if v == 0 and i % 10 == 1 and i % 100 != 11 or f % 10 == 1 and f % 100 != 11: return "one"
	elif lang == "ml":
		if n == 1: return "one"
	elif lang == "mn":
		if n == 1: return "one"
	elif lang == "mo":
		if i == 1 and v == 0: return "one"
		if v != 0 or n == 0 or n != 1 and (1 <= n % 100 and n % 100 <= 19): return "few"
	elif lang == "mr":
		if n == 1: return "one"
	elif lang == "mt":
		if n == 1: return "one"
		if n == 2: return "two"
		if n == 0 or (3 <= n % 100 and n % 100 <= 10): return "few"
		if (11 <= n % 100 and n % 100 <= 19): return "many"
	elif lang == "nah":
		if n == 1: return "one"
	elif lang == "naq":
		if n == 1: return "one"
		if n == 2: return "two"
	elif lang == "nb":
		if n == 1: return "one"
	elif lang == "nd":
		if n == 1: return "one"
	elif lang == "ne":
		if n == 1: return "one"
	elif lang == "nl":
		if i == 1 and v == 0: return "one"
	elif lang == "nn":
		if n == 1: return "one"
	elif lang == "nnh":
		if n == 1: return "one"
	elif lang == "no":
		if n == 1: return "one"
	elif lang == "nr":
		if n == 1: return "one"
	elif lang == "nso":
		if (0 <= n and n <= 1): return "one"
	elif lang == "ny":
		if n == 1: return "one"
	elif lang == "nyn":
		if n == 1: return "one"
	elif lang == "om":
		if n == 1: return "one"
	elif lang == "or":
		if n == 1: return "one"
	elif lang == "os":
		if n == 1: return "one"
	elif lang == "pa":
		if (0 <= n and n <= 1): return "one"
	elif lang == "pap":
		if n == 1: return "one"
	elif lang == "pcm":
		if i == 0 or n == 1: return "one"
	elif lang == "pl":
		if i == 1 and v == 0: return "one"
		if v == 0 and (2 <= i % 10 and i % 10 <= 4) and (i % 100 < 12 or 14 < i % 100): return "few"
		if v == 0 and i != 1 and (0 <= i % 10 and i % 10 <= 1) or v == 0 and (5 <= i % 10 and i % 10 <= 9) or v == 0 and (12 <= i % 100 and i % 100 <= 14): return "many"
	elif lang == "prg":
		if n % 10 == 0 or (11 <= n % 100 and n % 100 <= 19) or v == 2 and (11 <= f % 100 and f % 100 <= 19): return "zero"
		if n % 10 == 1 and n % 100 != 11 or v == 2 and f % 10 == 1 and f % 100 != 11 or v != 2 and f % 10 == 1: return "one"
	elif lang == "ps":
		if n == 1: return "one"
	elif lang == "pt":
		if (0 <= i and i <= 1): return "one"
		if e == 0 and i != 0 and i % 1000000 == 0 and v == 0 or (e < 0 or 5 < e): return "many"
	elif lang == "rm":
		if n == 1: return "one"
	elif lang == "ro":
		if i == 1 and v == 0: return "one"
		if v != 0 or n == 0 or n != 1 and (1 <= n % 100 and n % 100 <= 19): return "few"
	elif lang == "rof":
		if n == 1: return "one"
	elif lang == "ru":
		if v == 0 and i % 10 == 1 and i % 100 != 11: return "one"
		if v == 0 and (2 <= i % 10 and i % 10 <= 4) and (i % 100 < 12 or 14 < i % 100): return "few"
		if v == 0 and i % 10 == 0 or v == 0 and (5 <= i % 10 and i % 10 <= 9) or v == 0 and (11 <= i % 100 and i % 100 <= 14): return "many"
	elif lang == "rwk":
		if n == 1: return "one"
	elif lang == "saq":
		if n == 1: return "one"
	elif lang == "sat":
		if n == 1: return "one"
		if n == 2: return "two"
	elif lang == "sc":
		if i == 1 and v == 0: return "one"
	elif lang == "scn":
		if i == 1 and v == 0: return "one"
	elif lang == "sd":
		if n == 1: return "one"
	elif lang == "sdh":
		if n == 1: return "one"
	elif lang == "se":
		if n == 1: return "one"
		if n == 2: return "two"
	elif lang == "seh":
		if n == 1: return "one"
	elif lang == "sh":
		if v == 0 and i % 10 == 1 and i % 100 != 11 or f % 10 == 1 and f % 100 != 11: return "one"
		if v == 0 and (2 <= i % 10 and i % 10 <= 4) and (i % 100 < 12 or 14 < i % 100) or (2 <= f % 10 and f % 10 <= 4) and (f % 100 < 12 or 14 < f % 100): return "few"
	elif lang == "shi":
		if i == 0 or n == 1: return "one"
		if (2 <= n and n <= 10): return "few"
	elif lang == "si":
		if (n == 0 or n == 1) or i == 0 and f == 1: return "one"
	elif lang == "sk":
		if i == 1 and v == 0: return "one"
		if (2 <= i and i <= 4) and v == 0: return "few"
		if v != 0: return "many"
	elif lang == "sl":
		if v == 0 and i % 100 == 1: return "one"
		if v == 0 and i % 100 == 2: return "two"
		if v == 0 and (3 <= i % 100 and i % 100 <= 4) or v != 0: return "few"
	elif lang == "sma":
		if n == 1: return "one"
		if n == 2: return "two"
	elif lang == "smi":
		if n == 1: return "one"
		if n == 2: return "two"
	elif lang == "smj":
		if n == 1: return "one"
		if n == 2: return "two"
	elif lang == "smn":
		if n == 1: return "one"
		if n == 2: return "two"
	elif lang == "sms":
		if n == 1: return "one"
		if n == 2: return "two"
	elif lang == "sn":
		if n == 1: return "one"
	elif lang == "so":
		if n == 1: return "one"
	elif lang == "sq":
		if n == 1: return "one"
	elif lang == "sr":
		if v == 0 and i % 10 == 1 and i % 100 != 11 or f % 10 == 1 and f % 100 != 11: return "one"
		if v == 0 and (2 <= i % 10 and i % 10 <= 4) and (i % 100 < 12 or 14 < i % 100) or (2 <= f % 10 and f % 10 <= 4) and (f % 100 < 12 or 14 < f % 100): return "few"
	elif lang == "ss":
		if n == 1: return "one"
	elif lang == "ssy":
		if n == 1: return "one"
	elif lang == "st":
		if n == 1: return "one"
	elif lang == "sv":
		if i == 1 and v == 0: return "one"
	elif lang == "sw":
		if i == 1 and v == 0: return "one"
	elif lang == "syr":
		if n == 1: return "one"
	elif lang == "ta":
		if n == 1: return "one"
	elif lang == "te":
		if n == 1: return "one"
	elif lang == "teo":
		if n == 1: return "one"
	elif lang == "ti":
		if (0 <= n and n <= 1): return "one"
	elif lang == "tig":
		if n == 1: return "one"
	elif lang == "tk":
		if n == 1: return "one"
	elif lang == "tl":
		if v == 0 and (i == 1 or i == 2 or i == 3) or v == 0 and (i % 10 != 4 or i % 10 != 6 or i % 10 != 9) or v != 0 and (f % 10 != 4 or f % 10 != 6 or f % 10 != 9): return "one"
	elif lang == "tn":
		if n == 1: return "one"
	elif lang == "tr":
		if n == 1: return "one"
	elif lang == "ts":
		if n == 1: return "one"
	elif lang == "tzm":
		if (0 <= n and n <= 1) or (11 <= n and n <= 99): return "one"
	elif lang == "ug":
		if n == 1: return "one"
	elif lang == "uk":
		if v == 0 and i % 10 == 1 and i % 100 != 11: return "one"
		if v == 0 and (2 <= i % 10 and i % 10 <= 4) and (i % 100 < 12 or 14 < i % 100): return "few"
		if v == 0 and i % 10 == 0 or v == 0 and (5 <= i % 10 and i % 10 <= 9) or v == 0 and (11 <= i % 100 and i % 100 <= 14): return "many"
	elif lang == "ur":
		if i == 1 and v == 0: return "one"
	elif lang == "uz":
		if n == 1: return "one"
	elif lang == "ve":
		if n == 1: return "one"
	elif lang == "vec":
		if i == 1 and v == 0: return "one"
		if e == 0 and i != 0 and i % 1000000 == 0 and v == 0 or (e < 0 or 5 < e): return "many"
	elif lang == "vo":
		if n == 1: return "one"
	elif lang == "vun":
		if n == 1: return "one"
	elif lang == "wa":
		if (0 <= n and n <= 1): return "one"
	elif lang == "wae":
		if n == 1: return "one"
	elif lang == "xh":
		if n == 1: return "one"
	elif lang == "xog":
		if n == 1: return "one"
	elif lang == "yi":
		if i == 1 and v == 0: return "one"
	elif lang == "zu":
		if i == 0 or n == 1: return "one"
	return "other"

def ordinal_form(lang: str, n: float) -> str:
	i = int(n)
	lang = lang.replace("_", "-")
	lang = lang.split("-")[0]
	if lang == "as":
		if (n == 1 or n == 5 or n == 7 or n == 8 or n == 9 or n == 10): return "one"
		if (n == 2 or n == 3): return "two"
		if n == 4: return "few"
		if n == 6: return "many"
	elif lang == "az":
		if (i % 10 == 1 or i % 10 == 2 or i % 10 == 5 or i % 10 == 7 or i % 10 == 8) or (i % 100 == 20 or i % 100 == 50 or i % 100 == 70 or i % 100 == 80): return "one"
		if (i % 10 == 3 or i % 10 == 4) or (i % 1000 == 100 or i % 1000 == 200 or i % 1000 == 300 or i % 1000 == 400 or i % 1000 == 500 or i % 1000 == 600 or i % 1000 == 700 or i % 1000 == 800 or i % 1000 == 900): return "few"
		if i == 0 or i % 10 == 6 or (i % 100 == 40 or i % 100 == 60 or i % 100 == 90): return "many"
	elif lang == "bal":
		if n == 1: return "one"
	elif lang == "be":
		if (n % 10 == 2 or n % 10 == 3) and (n % 100 != 12 or n % 100 != 13): return "few"
	elif lang == "blo":
		if i == 0: return "zero"
		if i == 1: return "one"
		if (i == 2 or i == 3 or i == 4 or i == 5 or i == 6): return "few"
	elif lang == "bn":
		if (n == 1 or n == 5 or n == 7 or n == 8 or n == 9 or n == 10): return "one"
		if (n == 2 or n == 3): return "two"
		if n == 4: return "few"
		if n == 6: return "many"
	elif lang == "ca":
		if (n == 1 or n == 3): return "one"
		if n == 2: return "two"
		if n == 4: return "few"
	elif lang == "cy":
		if (n == 0 or n == 7 or n == 8 or n == 9): return "zero"
		if n == 1: return "one"
		if n == 2: return "two"
		if (n == 3 or n == 4): return "few"
		if (n == 5 or n == 6): return "many"
	elif lang == "en":
		if n % 10 == 1 and n % 100 != 11: return "one"
		if n % 10 == 2 and n % 100 != 12: return "two"
		if n % 10 == 3 and n % 100 != 13: return "few"
	elif lang == "fil":
		if n == 1: return "one"
	elif lang == "fr":
		if n == 1: return "one"
	elif lang == "ga":
		if n == 1: return "one"
	elif lang == "gd":
		if (n == 1 or n == 11): return "one"
		if (n == 2 or n == 12): return "two"
		if (n == 3 or n == 13): return "few"
	elif lang == "gu":
		if n == 1: return "one"
		if (n == 2 or n == 3): return "two"
		if n == 4: return "few"
		if n == 6: return "many"
	elif lang == "hi":
		if n == 1: return "one"
		if (n == 2 or n == 3): return "two"
		if n == 4: return "few"
		if n == 6: return "many"
	elif lang == "hu":
		if (n == 1 or n == 5): return "one"
	elif lang == "hy":
		if n == 1: return "one"
	elif lang == "it":
		if (n == 11 or n == 8 or n == 80 or n == 800): return "many"
	elif lang == "ka":
		if i == 1: return "one"
		if i == 0 or ((2 <= i % 100 and i % 100 <= 20) or i % 100 == 40 or i % 100 == 60 or i % 100 == 80): return "many"
	elif lang == "kk":
		if n % 10 == 6 or n % 10 == 9 or n % 10 == 0 and n != 0: return "many"
	elif lang == "kw":
		if (1 <= n and n <= 4) or ((1 <= n % 100 and n % 100 <= 4) or (21 <= n % 100 and n % 100 <= 24) or (41 <= n % 100 and n % 100 <= 44) or (61 <= n % 100 and n % 100 <= 64) or (81 <= n % 100 and n % 100 <= 84)): return "one"
		if n == 5 or n % 100 == 5: return "many"
	elif lang == "lij":
		if (n == 11 or n == 8 or (80 <= n and n <= 89) or (800 <= n and n <= 899)): return "many"
	elif lang == "lo":
		if n == 1: return "one"
	elif lang == "mk":
		if i % 10 == 1 and i % 100 != 11: return "one"
		if i % 10 == 2 and i % 100 != 12: return "two"
		if (i % 10 == 7 or i % 10 == 8) and (i % 100 != 17 or i % 100 != 18): return "many"
	elif lang == "mo":
		if n == 1: return "one"
	elif lang == "mr":
		if n == 1: return "one"
		if (n == 2 or n == 3): return "two"
		if n == 4: return "few"
	elif lang == "ms":
		if n == 1: return "one"
	elif lang == "ne":
		if (1 <= n and n <= 4): return "one"
	elif lang == "or":
		if (n == 1 or n == 5 or (7 <= n and n <= 9)): return "one"
		if (n == 2 or n == 3): return "two"
		if n == 4: return "few"
		if n == 6: return "many"
	elif lang == "ro":
		if n == 1: return "one"
	elif lang == "sc":
		if (n == 11 or n == 8 or n == 80 or n == 800): return "many"
	elif lang == "scn":
		if (n == 11 or n == 8 or n == 80 or n == 800): return "many"
	elif lang == "sq":
		if n == 1: return "one"
		if n % 10 == 4 and n % 100 != 14: return "many"
	elif lang == "sv":
		if (n % 10 == 1 or n % 10 == 2) and (n % 100 != 11 or n % 100 != 12): return "one"
	elif lang == "tk":
		if (n % 10 == 6 or n % 10 == 9) or n == 10: return "few"
	elif lang == "tl":
		if n == 1: return "one"
	elif lang == "uk":
		if n % 10 == 3 and n % 100 != 13: return "few"
	elif lang == "vec":
		if (n == 11 or n == 8 or n == 80 or n == 800): return "many"
	elif lang == "vi":
		if n == 1: return "one"
	return "other"

def plural_samples(lang: str) -> list:
	lang = lang.replace("_", "-")
	if lang == "pt-PT": return [('one', 1), ('many', 1000000), ('other', 2)]
	lang = lang.split("-")[0]
	if lang == "af": return [('one', 1), ('other', 2)]
	if lang == "ak": return [('one', 1), ('other', 2)]
	if lang == "am": return [('one', 1), ('other', 2)]
	if lang == "an": return [('one', 1), ('other', 2)]
	if lang == "ar": return [('zero', 0), ('one', 1), ('two', 2), ('few', 3), ('many', 11), ('other', 100)]
	if lang == "ars": return [('zero', 0), ('one', 1), ('two', 2), ('few', 3), ('many', 11), ('other', 100)]
	if lang == "as": return [('one', 1), ('other', 2)]
	if lang == "asa": return [('one', 1), ('other', 2)]
	if lang == "ast": return [('one', 1), ('other', 2)]
	if lang == "az": return [('one', 1), ('other', 2)]
	if lang == "bal": return [('one', 1), ('other', 2)]
	if lang == "be": return [('one', 1), ('few', 2), ('many', 5), ('other', 0.1)]
	if lang == "bem": return [('one', 1), ('other', 2)]
	if lang == "bez": return [('one', 1), ('other', 2)]
	if lang == "bg": return [('one', 1), ('other', 2)]
	if lang == "bho": return [('one', 1), ('other', 2)]
	if lang == "blo": return [('zero', 0), ('one', 1), ('other', 2)]
	if lang == "bm": return [('other', 15)]
	if lang == "bn": return [('one', 1), ('other', 2)]
	if lang == "bo": return [('other', 15)]
	if lang == "br": return [('one', 1), ('two', 2), ('few', 3), ('many', 1000000), ('other', 5)]
	if lang == "brx": return [('one', 1), ('other', 2)]
	if lang == "bs": return [('one', 1), ('few', 2), ('other', 5)]
	if lang == "ca": return [('one', 1), ('many', 1000000), ('other', 2)]
	if lang == "ce": return [('one', 1), ('other', 2)]
	if lang == "ceb": return [('one', 3), ('other', 4)]
	if lang == "cgg": return [('one', 1), ('other', 2)]
	if lang == "chr": return [('one', 1), ('other', 2)]
	if lang == "ckb": return [('one', 1), ('other', 2)]
	if lang == "cs": return [('one', 1), ('few', 2), ('many', 1.5), ('other', 5)]
	if lang == "cy": return [('zero', 0), ('one', 1), ('two', 2), ('few', 3), ('many', 6), ('other', 4)]
	if lang == "da": return [('one', 1), ('other', 2)]
	if lang == "de": return [('one', 1), ('other', 2)]
	if lang == "doi": return [('one', 1), ('other', 2)]
	if lang == "dsb": return [('one', 1), ('two', 2), ('few', 3), ('other', 5)]
	if lang == "dv": return [('one', 1), ('other', 2)]
	if lang == "dz": return [('other', 15)]
	if lang == "ee": return [('one', 1), ('other', 2)]
	if lang == "el": return [('one', 1), ('other', 2)]
	if lang == "en": return [('one', 1), ('other', 2)]
	if lang == "eo": return [('one', 1), ('other', 2)]
	if lang == "es": return [('one', 1), ('many', 1000000), ('other', 2)]
	if lang == "et": return [('one', 1), ('other', 2)]
	if lang == "eu": return [('one', 1), ('other', 2)]
	if lang == "fa": return [('one', 1), ('other', 2)]
	if lang == "ff": return [('one', 1), ('other', 2)]
	if lang == "fi": return [('one', 1), ('other', 2)]
	if lang == "fil": return [('one', 3), ('other', 4)]
	if lang == "fo": return [('one', 1), ('other', 2)]
	if lang == "fr": return [('one', 1), ('many', 1000000), ('other', 2)]
	if lang == "fur": return [('one', 1), ('other', 2)]
	if lang == "fy": return [('one', 1), ('other', 2)]
	if lang == "ga": return [('one', 1), ('two', 2), ('few', 3), ('many', 7), ('other', 11)]
	if lang == "gd": return [('one', 1), ('two', 2), ('few', 3), ('other', 20)]
	if lang == "gl": return [('one', 1), ('other', 2)]
	if lang == "gsw": return [('one', 1), ('other', 2)]
	if lang == "gu": return [('one', 1), ('other', 2)]
	if lang == "guw": return [('one', 1), ('other', 2)]
	if lang == "gv": return [('one', 1), ('two', 2), ('few', 20), ('many', 1.5), ('other', 3)]
	if lang == "ha": return [('one', 1), ('other', 2)]
	if lang == "haw": return [('one', 1), ('other', 2)]
	if lang == "he": return [('one', 1), ('two', 2), ('other', 3)]
	if lang == "hi": return [('one', 1), ('other', 2)]
	if lang == "hnj": return [('other', 15)]
	if lang == "hr": return [('one', 1), ('few', 2), ('other', 5)]
	if lang == "hsb": return [('one', 1), ('two', 2), ('few', 3), ('other', 5)]
	if lang == "hu": return [('one', 1), ('other', 2)]
	if lang == "hy": return [('one', 1), ('other', 2)]
	if lang == "ia": return [('one', 1), ('other', 2)]
	if lang == "id": return [('other', 15)]
	if lang == "ig": return [('other', 15)]
	if lang == "ii": return [('other', 15)]
	if lang == "io": return [('one', 1), ('other', 2)]
	if lang == "is": return [('one', 1), ('other', 2)]
	if lang == "it": return [('one', 1), ('many', 1000000), ('other', 2)]
	if lang == "iu": return [('one', 1), ('two', 2), ('other', 3)]
	if lang == "ja": return [('other', 15)]
	if lang == "jbo": return [('other', 15)]
	if lang == "jgo": return [('one', 1), ('other', 2)]
	if lang == "jmc": return [('one', 1), ('other', 2)]
	if lang == "jv": return [('other', 15)]
	if lang == "jw": return [('other', 15)]
	if lang == "ka": return [('one', 1), ('other', 2)]
	if lang == "kab": return [('one', 1), ('other', 2)]
	if lang == "kaj": return [('one', 1), ('other', 2)]
	if lang == "kcg": return [('one', 1), ('other', 2)]
	if lang == "kde": return [('other', 15)]
	if lang == "kea": return [('other', 15)]
	if lang == "kk": return [('one', 1), ('other', 2)]
	if lang == "kkj": return [('one', 1), ('other', 2)]
	if lang == "kl": return [('one', 1), ('other', 2)]
	if lang == "km": return [('other', 15)]
	if lang == "kn": return [('one', 1), ('other', 2)]
	if lang == "ko": return [('other', 15)]
	if lang == "ks": return [('one', 1), ('other', 2)]
	if lang == "ksb": return [('one', 1), ('other', 2)]
	if lang == "ksh": return [('zero', 0), ('one', 1), ('other', 2)]
	if lang == "ku": return [('one', 1), ('other', 2)]
	if lang == "kw": return [('zero', 0), ('one', 1), ('two', 2), ('few', 3), ('many', 21), ('other', 4)]
	if lang == "ky": return [('one', 1), ('other', 2)]
	if lang == "lag": return [('zero', 0), ('one', 1), ('other', 2)]
	if lang == "lb": return [('one', 1), ('other', 2)]
	if lang == "lg": return [('one', 1), ('other', 2)]
	if lang == "lij": return [('one', 1), ('other', 2)]
	if lang == "lkt": return [('other', 15)]
	if lang == "ln": return [('one', 1), ('other', 2)]
	if lang == "lo": return [('other', 15)]
	if lang == "lt": return [('one', 1), ('few', 2), ('many', 0.1), ('other', 10)]
	if lang == "lv": return [('zero', 10), ('one', 1), ('other', 2)]
	if lang == "mas": return [('one', 1), ('other', 2)]
	if lang == "mg": return [('one', 1), ('other', 2)]
	if lang == "mgo": return [('one', 1), ('other', 2)]
	if lang == "mk": return [('one', 1), ('other', 2)]
	if lang == "ml": return [('one', 1), ('other', 2)]
	if lang == "mn": return [('one', 1), ('other', 2)]
	if lang == "mo": return [('one', 1), ('few', 2), ('other', 20)]
	if lang == "mr": return [('one', 1), ('other', 2)]
	if lang == "ms": return [('other', 15)]
	if lang == "mt": return [('one', 1), ('two', 2), ('few', 3), ('many', 11), ('other', 20)]
	if lang == "my": return [('other', 15)]
	if lang == "nah": return [('one', 1), ('other', 2)]
	if lang == "naq": return [('one', 1), ('two', 2), ('other', 3)]
	if lang == "nb": return [('one', 1), ('other', 2)]
	if lang == "nd": return [('one', 1), ('other', 2)]
	if lang == "ne": return [('one', 1), ('other', 2)]
	if lang == "nl": return [('one', 1), ('other', 2)]
	if lang == "nn": return [('one', 1), ('other', 2)]
	if lang == "nnh": return [('one', 1), ('other', 2)]
	if lang == "no": return [('one', 1), ('other', 2)]
	if lang == "nqo": return [('other', 15)]
	if lang == "nr": return [('one', 1), ('other', 2)]
	if lang == "nso": return [('one', 1), ('other', 2)]
	if lang == "ny": return [('one', 1), ('other', 2)]
	if lang == "nyn": return [('one', 1), ('other', 2)]
	if lang == "om": return [('one', 1), ('other', 2)]
	if lang == "or": return [('one', 1), ('other', 2)]
	if lang == "os": return [('one', 1), ('other', 2)]
	if lang == "osa": return [('other', 15)]
	if lang == "pa": return [('one', 1), ('other', 2)]
	if lang == "pap": return [('one', 1), ('other', 2)]
	if lang == "pcm": return [('one', 1), ('other', 2)]
	if lang == "pl": return [('one', 1), ('few', 2), ('many', 5), ('other', 1.5)]
	if lang == "prg": return [('zero', 10), ('one', 1), ('other', 2)]
	if lang == "ps": return [('one', 1), ('other', 2)]
	if lang == "pt": return [('one', 1), ('many', 1000000), ('other', 2)]
	if lang == "rm": return [('one', 1), ('other', 2)]
	if lang == "ro": return [('one', 1), ('few', 2), ('other', 20)]
	if lang == "rof": return [('one', 1), ('other', 2)]
	if lang == "ru": return [('one', 1), ('few', 2), ('many', 5), ('other', 1.5)]
	if lang == "rwk": return [('one', 1), ('other', 2)]
	if lang == "sah": return [('other', 15)]
	if lang == "saq": return [('one', 1), ('other', 2)]
	if lang == "sat": return [('one', 1), ('two', 2), ('other', 3)]
	if lang == "sc": return [('one', 1), ('other', 2)]
	if lang == "scn": return [('one', 1), ('other', 2)]
	if lang == "sd": return [('one', 1), ('other', 2)]
	if lang == "sdh": return [('one', 1), ('other', 2)]
	if lang == "se": return [('one', 1), ('two', 2), ('other', 3)]
	if lang == "seh": return [('one', 1), ('other', 2)]
	if lang == "ses": return [('other', 15)]
	if lang == "sg": return [('other', 15)]
	if lang == "sh": return [('one', 1), ('few', 2), ('other', 5)]
	if lang == "shi": return [('one', 1), ('few', 2), ('other', 11)]
	if lang == "si": return [('one', 1), ('other', 2)]
	if lang == "sk": return [('one', 1), ('few', 2), ('many', 1.5), ('other', 5)]
	if lang == "sl": return [('one', 1), ('two', 2), ('few', 3), ('other', 5)]
	if lang == "sma": return [('one', 1), ('two', 2), ('other', 3)]
	if lang == "smi": return [('one', 1), ('two', 2), ('other', 3)]
	if lang == "smj": return [('one', 1), ('two', 2), ('other', 3)]
	if lang == "smn": return [('one', 1), ('two', 2), ('other', 3)]
	if lang == "sms": return [('one', 1), ('two', 2), ('other', 3)]
	if lang == "sn": return [('one', 1), ('other', 2)]
	if lang == "so": return [('one', 1), ('other', 2)]
	if lang == "sq": return [('one', 1), ('other', 2)]
	if lang == "sr": return [('one', 1), ('few', 2), ('other', 5)]
	if lang == "ss": return [('one', 1), ('other', 2)]
	if lang == "ssy": return [('one', 1), ('other', 2)]
	if lang == "st": return [('one', 1), ('other', 2)]
	if lang == "su": return [('other', 15)]
	if lang == "sv": return [('one', 1), ('other', 2)]
	if lang == "sw": return [('one', 1), ('other', 2)]
	if lang == "syr": return [('one', 1), ('other', 2)]
	if lang == "ta": return [('one', 1), ('other', 2)]
	if lang == "te": return [('one', 1), ('other', 2)]
	if lang == "teo": return [('one', 1), ('other', 2)]
	if lang == "th": return [('other', 15)]
	if lang == "ti": return [('one', 1), ('other', 2)]
	if lang == "tig": return [('one', 1), ('other', 2)]
	if lang == "tk": return [('one', 1), ('other', 2)]
	if lang == "tl": return [('one', 3), ('other', 4)]
	if lang == "tn": return [('one', 1), ('other', 2)]
	if lang == "to": return [('other', 15)]
	if lang == "tpi": return [('other', 15)]
	if lang == "tr": return [('one', 1), ('other', 2)]
	if lang == "ts": return [('one', 1), ('other', 2)]
	if lang == "tzm": return [('one', 1), ('other', 2)]
	if lang == "ug": return [('one', 1), ('other', 2)]
	if lang == "uk": return [('one', 1), ('few', 2), ('many', 5), ('other', 1.5)]
	if lang == "und": return [('other', 15)]
	if lang == "ur": return [('one', 1), ('other', 2)]
	if lang == "uz": return [('one', 1), ('other', 2)]
	if lang == "ve": return [('one', 1), ('other', 2)]
	if lang == "vec": return [('one', 1), ('many', 1000000), ('other', 2)]
	if lang == "vi": return [('other', 15)]
	if lang == "vo": return [('one', 1), ('other', 2)]
	if lang == "vun": return [('one', 1), ('other', 2)]
	if lang == "wa": return [('one', 1), ('other', 2)]
	if lang == "wae": return [('one', 1), ('other', 2)]
	if lang == "wo": return [('other', 15)]
	if lang == "xh": return [('one', 1), ('other', 2)]
	if lang == "xog": return [('one', 1), ('other', 2)]
	if lang == "yi": return [('one', 1), ('other', 2)]
	if lang == "yo": return [('other', 15)]
	if lang == "yue": return [('other', 15)]
	if lang == "zh": return [('other', 15)]
	if lang == "zu": return [('one', 1), ('other', 2)]
	return []

def ordinal_samples(lang: str) -> list:
	lang = lang.replace("_", "-")
	lang = lang.split("-")[0]
	if lang == "af": return [('other', 15)]
	if lang == "am": return [('other', 15)]
	if lang == "an": return [('other', 15)]
	if lang == "ar": return [('other', 15)]
	if lang == "as": return [('one', 1), ('two', 2), ('few', 4), ('many', 6), ('other', 11)]
	if lang == "ast": return [('other', 15)]
	if lang == "az": return [('one', 1), ('few', 3), ('many', 6), ('other', 9)]
	if lang == "bal": return [('one', 1), ('other', 2)]
	if lang == "be": return [('few', 2), ('other', 1)]
	if lang == "bg": return [('other', 15)]
	if lang == "blo": return [('zero', 0), ('one', 1), ('few', 2), ('other', 7)]
	if lang == "bn": return [('one', 1), ('two', 2), ('few', 4), ('many', 6), ('other', 11)]
	if lang == "bs": return [('other', 15)]
	if lang == "ca": return [('one', 1), ('two', 2), ('few', 4), ('other', 5)]
	if lang == "ce": return [('other', 15)]
	if lang == "cs": return [('other', 15)]
	if lang == "cy": return [('zero', 7), ('one', 1), ('two', 2), ('few', 3), ('many', 5), ('other', 10)]
	if lang == "da": return [('other', 15)]
	if lang == "de": return [('other', 15)]
	if lang == "dsb": return [('other', 15)]
	if lang == "el": return [('other', 15)]
	if lang == "en": return [('one', 1), ('two', 2), ('few', 3), ('other', 4)]
	if lang == "es": return [('other', 15)]
	if lang == "et": return [('other', 15)]
	if lang == "eu": return [('other', 15)]
	if lang == "fa": return [('other', 15)]
	if lang == "fi": return [('other', 15)]
	if lang == "fil": return [('one', 1), ('other', 2)]
	if lang == "fr": return [('one', 1), ('other', 2)]
	if lang == "fy": return [('other', 15)]
	if lang == "ga": return [('one', 1), ('other', 2)]
	if lang == "gd": return [('one', 1), ('two', 2), ('few', 3), ('other', 4)]
	if lang == "gl": return [('other', 15)]
	if lang == "gsw": return [('other', 15)]
	if lang == "gu": return [('one', 1), ('two', 2), ('few', 4), ('many', 6), ('other', 5)]
	if lang == "he": return [('other', 15)]
	if lang == "hi": return [('one', 1), ('two', 2), ('few', 4), ('many', 6), ('other', 5)]
	if lang == "hr": return [('other', 15)]
	if lang == "hsb": return [('other', 15)]
	if lang == "hu": return [('one', 1), ('other', 2)]
	if lang == "hy": return [('one', 1), ('other', 2)]
	if lang == "ia": return [('other', 15)]
	if lang == "id": return [('other', 15)]
	if lang == "is": return [('other', 15)]
	if lang == "it": return [('many', 8), ('other', 7)]
	if lang == "ja": return [('other', 15)]
	if lang == "ka": return [('one', 1), ('many', 2), ('other', 21)]
	if lang == "kk": return [('many', 6), ('other', 5)]
	if lang == "km": return [('other', 15)]
	if lang == "kn": return [('other', 15)]
	if lang == "ko": return [('other', 15)]
	if lang == "kw": return [('one', 1), ('many', 5), ('other', 6)]
	if lang == "ky": return [('other', 15)]
	if lang == "lij": return [('many', 8), ('other', 7)]
	if lang == "lo": return [('one', 1), ('other', 2)]
	if lang == "lt": return [('other', 15)]
	if lang == "lv": return [('other', 15)]
	if lang == "mk": return [('one', 1), ('two', 2), ('many', 7), ('other', 3)]
	if lang == "ml": return [('other', 15)]
	if lang == "mn": return [('other', 15)]
	if lang == "mo": return [('one', 1), ('other', 2)]
	if lang == "mr": return [('one', 1), ('two', 2), ('few', 4), ('other', 5)]
	if lang == "ms": return [('one', 1), ('other', 2)]
	if lang == "my": return [('other', 15)]
	if lang == "nb": return [('other', 15)]
	if lang == "ne": return [('one', 1), ('other', 5)]
	if lang == "nl": return [('other', 15)]
	if lang == "no": return [('other', 15)]
	if lang == "or": return [('one', 1), ('two', 2), ('few', 4), ('many', 6), ('other', 10)]
	if lang == "pa": return [('other', 15)]
	if lang == "pl": return [('other', 15)]
	if lang == "prg": return [('other', 15)]
	if lang == "ps": return [('other', 15)]
	if lang == "pt": return [('other', 15)]
	if lang == "ro": return [('one', 1), ('other', 2)]
	if lang == "ru": return [('other', 15)]
	if lang == "sc": return [('many', 8), ('other', 7)]
	if lang == "scn": return [('many', 8), ('other', 7)]
	if lang == "sd": return [('other', 15)]
	if lang == "sh": return [('other', 15)]
	if lang == "si": return [('other', 15)]
	if lang == "sk": return [('other', 15)]
	if lang == "sl": return [('other', 15)]
	if lang == "sq": return [('one', 1), ('many', 4), ('other', 2)]
	if lang == "sr": return [('other', 15)]
	if lang == "sv": return [('one', 1), ('other', 3)]
	if lang == "sw": return [('other', 15)]
	if lang == "ta": return [('other', 15)]
	if lang == "te": return [('other', 15)]
	if lang == "th": return [('other', 15)]
	if lang == "tk": return [('few', 6), ('other', 5)]
	if lang == "tl": return [('one', 1), ('other', 2)]
	if lang == "tpi": return [('other', 15)]
	if lang == "tr": return [('other', 15)]
	if lang == "uk": return [('few', 3), ('other', 2)]
	if lang == "und": return [('other', 15)]
	if lang == "ur": return [('other', 15)]
	if lang == "uz": return [('other', 15)]
	if lang == "vec": return [('many', 8), ('other', 7)]
	if lang == "vi": return [('one', 1), ('other', 2)]
	if lang == "yue": return [('other', 15)]
	if lang == "zh": return [('other', 15)]
	if lang == "zu": return [('other', 15)]
	return []

def number_symbols(lang: str) -> dict:
	lang = lang.replace("_", "-")
	if lang == "af-NA": return {'decimal': ',', 'group': '\xa0'}
	if lang == "ar-AE": return {'decimal': '.', 'group': ','}
	if lang == "ar-BH": return {'decimal': '.', 'group': ','}
	if lang == "ar-DJ": return {'decimal': '.', 'group': ','}
	if lang == "ar-DZ": return {'decimal': ',', 'group': '.'}
	if lang == "ar-EG": return {'decimal': '.', 'group': ','}
	if lang == "ar-EH": return {'decimal': '.', 'group': ','}
	if lang == "ar-ER": return {'decimal': '.', 'group': ','}
	if lang == "ar-IL": return {'decimal': '.', 'group': ','}
	if lang == "ar-IQ": return {'decimal': '.', 'group': ','}
	if lang == "ar-JO": return {'decimal': '.', 'group': ','}
	if lang == "ar-KM": return {'decimal': '.', 'group': ','}
	if lang == "ar-KW": return {'decimal': '.', 'group': ','}
	if lang == "ar-LB": return {'decimal': ',', 'group': '.'}
	if lang == "ar-LY": return {'decimal': ',', 'group': '.'}
	if lang == "ar-MA": return {'decimal': ',', 'group': '.'}
	if lang == "ar-MR": return {'decimal': ',', 'group': '.'}
	if lang == "ar-OM": return {'decimal': '.', 'group': ','}
	if lang == "ar-PS": return {'decimal': '.', 'group': ','}
	if lang == "ar-QA": return {'decimal': '.', 'group': ','}
	if lang == "ar-SA": return {'decimal': '.', 'group': ','}
	if lang == "ar-SD": return {'decimal': '.', 'group': ','}
	if lang == "ar-SO": return {'decimal': '.', 'group': ','}
	if lang == "ar-SS": return {'decimal': '.', 'group': ','}
	if lang == "ar-SY": return {'decimal': '.', 'group': ','}
	if lang == "ar-TD": return {'decimal': '.', 'group': ','}
	if lang == "ar-TN": return {'decimal': ',', 'group': '.'}
	if lang == "ar-YE": return {'decimal': '.', 'group': ','}
	if lang == "az-Latn": return {'decimal': ',', 'group': '.'}
	if lang == "be-tarask": return {'decimal': ',', 'group': '\xa0'}
	if lang == "bn-IN": return {'decimal': '.', 'group': ','}
	if lang == "bs-Latn": return {'decimal': ',', 'group': '.'}
	if lang == "ca-AD": return {'decimal': ',', 'group': '.'}
	if lang == "ca-ES-valencia": return {'decimal': ',', 'group': '.'}
	if lang == "ca-FR": return {'decimal': ',', 'group': '.'}
	if lang == "ca-IT": return {'decimal': ',', 'group': '.'}
	if lang == "da-GL": return {'decimal': ',', 'group': '.'}
	if lang == "de-AT": return {'decimal': ',', 'group': '\xa0'}
	if lang == "de-BE": return {'decimal': ',', 'group': '.'}
	if lang == "de-CH": return {'decimal': '.', 'group': '’'}
	if lang == "de-IT": return {'decimal': ',', 'group': '.'}
	if lang == "de-LI": return {'decimal': '.', 'group': '’'}
	if lang == "de-LU": return {'decimal': ',', 'group': '.'}
	if lang == "el-CY": return {'decimal': ',', 'group': '.'}
	if lang == "el-polyton": return {'decimal': ',', 'group': '.'}
	if lang == "en-001": return {'decimal': '.', 'group': ','}
	if lang == "en-150": return {'decimal': '.', 'group': ','}
	if lang == "en-AE": return {'decimal': '.', 'group': ','}
	if lang == "en-AG": return {'decimal': '.', 'group': ','}
	if lang == "en-AI": return {'decimal': '.', 'group': ','}
	if lang == "en-AS": return {'decimal': '.', 'group': ','}
	if lang == "en-AT": return {'decimal': ',', 'group': '.'}
	if lang == "en-AU": return {'decimal': '.', 'group': ','}
	if lang == "en-BB": return {'decimal': '.', 'group': ','}
	if lang == "en-BE": return {'decimal': ',', 'group': '.'}
	if lang == "en-BI": return {'decimal': '.', 'group': ','}
	if lang == "en-BM": return {'decimal': '.', 'group': ','}
	if lang == "en-BS": return {'decimal': '.', 'group': ','}
	if lang == "en-BW": return {'decimal': '.', 'group': ','}
	if lang == "en-BZ": return {'decimal': '.', 'group': ','}
	if lang == "en-CA": return {'decimal': '.', 'group': ','}
	if lang == "en-CC": return {'decimal': '.', 'group': ','}
	if lang == "en-CH": return {'decimal': '.', 'group': '’'}
	if lang == "en-CK": return {'decimal': '.', 'group': ','}
	if lang == "en-CM": return {'decimal': '.', 'group': ','}
	if lang == "en-CX": return {'decimal': '.', 'group': ','}
	if lang == "en-CY": return {'decimal': '.', 'group': ','}
	if lang == "en-DE": return {'decimal': ',', 'group': '.'}
	if lang == "en-DG": return {'decimal': '.', 'group': ','}
	if lang == "en-DK": return {'decimal': ',', 'group': '.'}
	if lang == "en-DM": return {'decimal': '.', 'group': ','}
	if lang == "en-ER": return {'decimal': '.', 'group': ','}
	if lang == "en-FI": return {'decimal': ',', 'group': '\xa0'}
	if lang == "en-FJ": return {'decimal': '.', 'group': ','}
	if lang == "en-FK": return {'decimal': '.', 'group': ','}
	if lang == "en-FM": return {'decimal': '.', 'group': ','}
	if lang == "en-GB": return {'decimal': '.', 'group': ','}
	if lang == "en-GD": return {'decimal': '.', 'group': ','}
	if lang == "en-GG": return {'decimal': '.', 'group': ','}
	if lang == "en-GH": return {'decimal': '.', 'group': ','}
	if lang == "en-GI": return {'decimal': '.', 'group': ','}
	if lang == "en-GM": return {'decimal': '.', 'group': ','}
	if lang == "en-GU": return {'decimal': '.', 'group': ','}
	if lang == "en-GY": return {'decimal': '.', 'group': ','}
	if lang == "en-HK": return {'decimal': '.', 'group': ','}
	if lang == "en-ID": return {'decimal': ',', 'group': '.'}
	if lang == "en-IE": return {'decimal': '.', 'group': ','}
	if lang == "en-IL": return {'decimal': '.', 'group': ','}
	if lang == "en-IM": return {'decimal': '.', 'group': ','}
	if lang == "en-IN": return {'decimal': '.', 'group': ','}
	if lang == "en-IO": return {'decimal': '.', 'group': ','}
	if lang == "en-JE": return {'decimal': '.', 'group': ','}
	if lang == "en-JM": return {'decimal': '.', 'group': ','}
	if lang == "en-KE": return {'decimal': '.', 'group': ','}
	if lang == "en-KI": return {'decimal': '.', 'group': ','}
	if lang == "en-KN": return {'decimal': '.', 'group': ','}
	if lang == "en-KY": return {'decimal': '.', 'group': ','}
	if lang == "en-LC": return {'decimal': '.', 'group': ','}
	if lang == "en-LR": return {'decimal': '.', 'group': ','}
	if lang == "en-LS": return {'decimal': '.', 'group': ','}
	if lang == "en-MG": return {'decimal': '.', 'group': ','}
	if lang == "en-MH": return {'decimal': '.', 'group': ','}
	if lang == "en-MO": return {'decimal': '.', 'group': ','}
	if lang == "en-MP": return {'decimal': '.', 'group': ','}
	if lang == "en-MS": return {'decimal': '.', 'group': ','}
	if lang == "en-MT": return {'decimal': '.', 'group': ','}
	if lang == "en-MU": return {'decimal': '.', 'group': ','}
	if lang == "en-MV": return {'decimal': '.', 'group': ','}
	if lang == "en-MW": return {'decimal': '.', 'group': ','}
	if lang == "en-MY": return {'decimal': '.', 'group': ','}
	if lang == "en-NA": return {'decimal': '.', 'group': ','}
	if lang == "en-NF": return {'decimal': '.', 'group': ','}
	if lang == "en-NG": return {'decimal': '.', 'group': ','}
	if lang == "en-NL": return {'decimal': ',', 'group': '.'}
	if lang == "en-NR": return {'decimal': '.', 'group': ','}
	if lang == "en-NU": return {'decimal': '.', 'group': ','}
	if lang == "en-NZ": return {'decimal': '.', 'group': ','}
	if lang == "en-PG": return {'decimal': '.', 'group': ','}
	if lang == "en-PH": return {'decimal': '.', 'group': ','}
	if lang == "en-PK": return {'decimal': '.', 'group': ','}
	if lang == "en-PN": return {'decimal': '.', 'group': ','}
	if lang == "en-PR": return {'decimal': '.', 'group': ','}
	if lang == "en-PW": return {'decimal': '.', 'group': ','}
	if lang == "en-RW": return {'decimal': '.', 'group': ','}
	if lang == "en-SB": return {'decimal': '.', 'group': ','}
	if lang == "en-SC": return {'decimal': '.', 'group': ','}
	if lang == "en-SD": return {'decimal': '.', 'group': ','}
	if lang == "en-SE": return {'decimal': ',', 'group': '\xa0'}
	if lang == "en-SG": return {'decimal': '.', 'group': ','}
	if lang == "en-SH": return {'decimal': '.', 'group': ','}
	if lang == "en-SI": return {'decimal': ',', 'group': '.'}
	if lang == "en-SL": return {'decimal': '.', 'group': ','}
	if lang == "en-SS": return {'decimal': '.', 'group': ','}
	if lang == "en-SX": return {'decimal': '.', 'group': ','}
	if lang == "en-SZ": return {'decimal': '.', 'group': ','}
	if lang == "en-TC": return {'decimal': '.', 'group': ','}
	if lang == "en-TK": return {'decimal': '.', 'group': ','}
	if lang == "en-TO": return {'decimal': '.', 'group': ','}
	if lang == "en-TT": return {'decimal': '.', 'group': ','}
	if lang == "en-TV": return {'decimal': '.', 'group': ','}
	if lang == "en-TZ": return {'decimal': '.', 'group': ','}
	if lang == "en-UG": return {'decimal': '.', 'group': ','}
	if lang == "en-UM": return {'decimal': '.', 'group': ','}
	if lang == "en-VC": return {'decimal': '.', 'group': ','}
	if lang == "en-VG": return {'decimal': '.', 'group': ','}
	if lang == "en-VI": return {'decimal': '.', 'group': ','}
	if lang == "en-VU": return {'decimal': '.', 'group': ','}
	if lang == "en-WS": return {'decimal': '.', 'group': ','}
	if lang == "en-ZA": return {'decimal': '.', 'group': ','}
	if lang == "en-ZM": return {'decimal': '.', 'group': ','}
	if lang == "en-ZW": return {'decimal': '.', 'group': ','}
	if lang == "es-419": return {'decimal': '.', 'group': ','}
	if lang == "es-AR": return {'decimal': ',', 'group': '.'}
	if lang == "es-BO": return {'decimal': ',', 'group': '.'}
	if lang == "es-BR": return {'decimal': '.', 'group': ','}
	if lang == "es-BZ": return {'decimal': '.', 'group': ','}
	if lang == "es-CL": return {'decimal': ',', 'group': '.'}
	if lang == "es-CO": return {'decimal': ',', 'group': '.'}
	if lang == "es-CR": return {'decimal': ',', 'group': '\xa0'}
	if lang == "es-CU": return {'decimal': '.', 'group': ','}
	if lang == "es-DO": return {'decimal': '.', 'group': ','}
	if lang == "es-EA": return {'decimal': ',', 'group': '.'}
	if lang == "es-EC": return {'decimal': ',', 'group': '.'}
	if lang == "es-GQ": return {'decimal': ',', 'group': '.'}
	if lang == "es-GT": return {'decimal': '.', 'group': ','}
	if lang == "es-HN": return {'decimal': '.', 'group': ','}
	if lang == "es-IC": return {'decimal': ',', 'group': '.'}
	if lang == "es-MX": return {'decimal': '.', 'group': ','}
	if lang == "es-NI": return {'decimal': '.', 'group': ','}
	if lang == "es-PA": return {'decimal': '.', 'group': ','}
	if lang == "es-PE": return {'decimal': '.', 'group': ','}
	if lang == "es-PH": return {'decimal': ',', 'group': '.'}
	if lang == "es-PR": return {'decimal': '.', 'group': ','}
	if lang == "es-PY": return {'decimal': ',', 'group': '.'}
	if lang == "es-SV": return {'decimal': '.', 'group': ','}
	if lang == "es-US": return {'decimal': '.', 'group': ','}
	if lang == "es-UY": return {'decimal': ',', 'group': '.'}
	if lang == "es-VE": return {'decimal': ',', 'group': '.'}
	if lang == "fa-AF": return {'decimal': '.', 'group': ','}
	if lang == "fr-BE": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-BF": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-BI": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-BJ": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-BL": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-CA": return {'decimal': ',', 'group': '\xa0'}
	if lang == "fr-CD": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-CF": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-CG": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-CH": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-CI": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-CM": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-DJ": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-DZ": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-GA": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-GF": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-GN": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-GP": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-GQ": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-HT": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-KM": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-LU": return {'decimal': ',', 'group': '.'}
	if lang == "fr-MA": return {'decimal': ',', 'group': '.'}
	if lang == "fr-MC": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-MF": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-MG": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-ML": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-MQ": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-MR": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-MU": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-NC": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-NE": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-PF": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-PM": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-RE": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-RW": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-SC": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-SN": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-SY": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-TD": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-TG": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-TN": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-VU": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-WF": return {'decimal': ',', 'group': '\u202f'}
	if lang == "fr-YT": return {'decimal': ',', 'group': '\u202f'}
	if lang == "ga-GB": return {'decimal': '.', 'group': ','}
	if lang == "ha-GH": return {'decimal': '.', 'group': ','}
	if lang == "ha-NE": return {'decimal': '.', 'group': ','}
	if lang == "hi-Latn": return {'decimal': '.', 'group': ','}
	if lang == "hr-BA": return {'decimal': ',', 'group': '.'}
	if lang == "it-CH": return {'decimal': '.', 'group': '’'}
	if lang == "it-SM": return {'decimal': ',', 'group': '.'}
	if lang == "it-VA": return {'decimal': ',', 'group': '.'}
	if lang == "ko-CN": return {'decimal': '.', 'group': ','}
	if lang == "ko-KP": return {'decimal': '.', 'group': ','}
	if lang == "ms-BN": return {'decimal': ',', 'group': '.'}
	if lang == "ms-ID": return {'decimal': ',', 'group': '.'}
	if lang == "ms-SG": return {'decimal': '.', 'group': ','}
	if lang == "nb-SJ": return {'decimal': ',', 'group': '\xa0'}
	if lang == "ne-IN": return {'decimal': '.', 'group': ','}
	if lang == "nl-AW": return {'decimal': ',', 'group': '.'}
	if lang == "nl-BE": return {'decimal': ',', 'group': '.'}
	if lang == "nl-BQ": return {'decimal': ',', 'group': '.'}
	if lang == "nl-CW": return {'decimal': ',', 'group': '.'}
	if lang == "nl-SR": return {'decimal': ',', 'group': '.'}
	if lang == "nl-SX": return {'decimal': ',', 'group': '.'}
	if lang == "pa-Guru": return {'decimal': '.', 'group': ','}
	if lang == "ps-PK": return {'decimal': ',', 'group': '.'}
	if lang == "pt-AO": return {'decimal': ',', 'group': '\xa0'}
	if lang == "pt-CH": return {'decimal': ',', 'group': '\xa0'}
	if lang == "pt-CV": return {'decimal': ',', 'group': '\xa0'}
	if lang == "pt-GQ": return {'decimal': ',', 'group': '\xa0'}
	if lang == "pt-GW": return {'decimal': ',', 'group': '\xa0'}
	if lang == "pt-LU": return {'decimal': ',', 'group': '\xa0'}
	if lang == "pt-MO": return {'decimal': ',', 'group': '\xa0'}
	if lang == "pt-MZ": return {'decimal': ',', 'group': '\xa0'}
	if lang == "pt-PT": return {'decimal': ',', 'group': '\xa0'}
	if lang == "pt-ST": return {'decimal': ',', 'group': '\xa0'}
	if lang == "pt-TL": return {'decimal': ',', 'group': '\xa0'}
	if lang == "ro-MD": return {'decimal': ',', 'group': '.'}
	if lang == "ru-BY": return {'decimal': ',', 'group': '\xa0'}
	if lang == "ru-KG": return {'decimal': ',', 'group': '\xa0'}
	if lang == "ru-KZ": return {'decimal': ',', 'group': '\xa0'}
	if lang == "ru-MD": return {'decimal': ',', 'group': '\xa0'}
	if lang == "ru-UA": return {'decimal': ',', 'group': '\xa0'}
	if lang == "sd-Arab": return {'decimal': '.', 'group': ','}
	if lang == "so-DJ": return {'decimal': '.', 'group': ','}
	if lang == "so-ET": return {'decimal': '.', 'group': ','}
	if lang == "so-KE": return {'decimal': '.', 'group': ','}
	if lang == "sq-MK": return {'decimal': ',', 'group': '\xa0'}
	if lang == "sq-XK": return {'decimal': ',', 'group': '\xa0'}
	if lang == "sr-Cyrl-BA": return {'decimal': ',', 'group': '.'}
	if lang == "sr-Cyrl-ME": return {'decimal': ',', 'group': '.'}
	if lang == "sr-Cyrl-XK": return {'decimal': ',', 'group': '.'}
	if lang == "sr-Cyrl": return {'decimal': ',', 'group': '.'}
	if lang == "sr-Latn-BA": return {'decimal': ',', 'group': '.'}
	if lang == "sr-Latn-ME": return {'decimal': ',', 'group': '.'}
	if lang == "sr-Latn-XK": return {'decimal': ',', 'group': '.'}
	if lang == "sr-Latn": return {'decimal': ',', 'group': '.'}
	if lang == "sv-AX": return {'decimal': ',', 'group': '\xa0'}
	if lang == "sv-FI": return {'decimal': ',', 'group': '\xa0'}
	if lang == "sw-CD": return {'decimal': ',', 'group': '.'}
	if lang == "sw-KE": return {'decimal': '.', 'group': ','}
	if lang == "sw-UG": return {'decimal': '.', 'group': ','}
	if lang == "ta-LK": return {'decimal': '.', 'group': ','}
	if lang == "ta-MY": return {'decimal': '.', 'group': ','}
	if lang == "ta-SG": return {'decimal': '.', 'group': ','}
	if lang == "tr-CY": return {'decimal': ',', 'group': '.'}
	if lang == "ur-IN": return {'decimal': '.', 'group': ','}
	if lang == "uz-Latn": return {'decimal': ',', 'group': '\xa0'}
	if lang == "yo-BJ": return {'decimal': '.', 'group': ','}
	if lang == "yue-Hans": return {'decimal': '.', 'group': ','}
	if lang == "yue-Hant": return {'decimal': '.', 'group': ','}
	if lang == "zh-Hans-HK": return {'decimal': '.', 'group': ','}
	if lang == "zh-Hans-MO": return {'decimal': '.', 'group': ','}
	if lang == "zh-Hans-SG": return {'decimal': '.', 'group': ','}
	if lang == "zh-Hans": return {'decimal': '.', 'group': ','}
	if lang == "zh-Hant-HK": return {'decimal': '.', 'group': ','}
	if lang == "zh-Hant-MO": return {'decimal': '.', 'group': ','}
	if lang == "zh-Hant": return {'decimal': '.', 'group': ','}
	lang = lang.split("-")[0]
	if lang == "af": return {'decimal': ',', 'group': '\xa0'}
	if lang == "am": return {'decimal': '.', 'group': ','}
	if lang == "ar": return {'decimal': '.', 'group': ','}
	if lang == "as": return {'decimal': '.', 'group': ','}
	if lang == "az": return {'decimal': ',', 'group': '.'}
	if lang == "be": return {'decimal': ',', 'group': '\xa0'}
	if lang == "bg": return {'decimal': ',', 'group': '\xa0'}
	if lang == "bn": return {'decimal': '.', 'group': ','}
	if lang == "bs": return {'decimal': ',', 'group': '.'}
	if lang == "ca": return {'decimal': ',', 'group': '.'}
	if lang == "chr": return {'decimal': '.', 'group': ','}
	if lang == "cs": return {'decimal': ',', 'group': '\xa0'}
	if lang == "cy": return {'decimal': '.', 'group': ','}
	if lang == "da": return {'decimal': ',', 'group': '.'}
	if lang == "de": return {'decimal': ',', 'group': '.'}
	if lang == "dsb": return {'decimal': ',', 'group': '.'}
	if lang == "el": return {'decimal': ',', 'group': '.'}
	if lang == "en": return {'decimal': '.', 'group': ','}
	if lang == "es": return {'decimal': ',', 'group': '.'}
	if lang == "et": return {'decimal': ',', 'group': '\xa0'}
	if lang == "eu": return {'decimal': ',', 'group': '.'}
	if lang == "fa": return {'decimal': '.', 'group': ','}
	if lang == "fi": return {'decimal': ',', 'group': '\xa0'}
	if lang == "fil": return {'decimal': '.', 'group': ','}
	if lang == "fr": return {'decimal': ',', 'group': '\u202f'}
	if lang == "ga": return {'decimal': '.', 'group': ','}
	if lang == "gd": return {'decimal': '.', 'group': ','}
	if lang == "gl": return {'decimal': ',', 'group': '.'}
	if lang == "gu": return {'decimal': '.', 'group': ','}
	if lang == "ha": return {'decimal': '.', 'group': ','}
	if lang == "he": return {'decimal': '.', 'group': ','}
	if lang == "hi": return {'decimal': '.', 'group': ','}
	if lang == "hr": return {'decimal': ',', 'group': '.'}
	if lang == "hsb": return {'decimal': ',', 'group': '.'}
	if lang == "hu": return {'decimal': ',', 'group': '\xa0'}
	if lang == "hy": return {'decimal': ',', 'group': '\xa0'}
	if lang == "id": return {'decimal': ',', 'group': '.'}
	if lang == "ig": return {'decimal': '.', 'group': ','}
	if lang == "is": return {'decimal': ',', 'group': '.'}
	if lang == "it": return {'decimal': ',', 'group': '.'}
	if lang == "ja": return {'decimal': '.', 'group': ','}
	if lang == "jv": return {'decimal': ',', 'group': '.'}
	if lang == "ka": return {'decimal': ',', 'group': '\xa0'}
	if lang == "kk": return {'decimal': ',', 'group': '\xa0'}
	if lang == "km": return {'decimal': '.', 'group': ','}
	if lang == "kn": return {'decimal': '.', 'group': ','}
	if lang == "ko": return {'decimal': '.', 'group': ','}
	if lang == "kok": return {'decimal': '.', 'group': ','}
	if lang == "ky": return {'decimal': ',', 'group': '\xa0'}
	if lang == "lo": return {'decimal': ',', 'group': '.'}
	if lang == "lt": return {'decimal': ',', 'group': '\xa0'}
	if lang == "lv": return {'decimal': ',', 'group': '\xa0'}
	if lang == "mk": return {'decimal': ',', 'group': '.'}
	if lang == "ml": return {'decimal': '.', 'group': ','}
	if lang == "mn": return {'decimal': '.', 'group': ','}
	if lang == "mr": return {'decimal': '.', 'group': ','}
	if lang == "ms": return {'decimal': '.', 'group': ','}
	if lang == "my": return {'decimal': '.', 'group': ','}
	if lang == "nb": return {'decimal': ',', 'group': '\xa0'}
	if lang == "ne": return {'decimal': '.', 'group': ','}
	if lang == "nl": return {'decimal': ',', 'group': '.'}
	if lang == "nn": return {'decimal': ',', 'group': '\xa0'}
	if lang == "no": return {'decimal': ',', 'group': '\xa0'}
	if lang == "or": return {'decimal': '.', 'group': ','}
	if lang == "pa": return {'decimal': '.', 'group': ','}
	if lang == "pl": return {'decimal': ',', 'group': '\xa0'}
	if lang == "ps": return {'decimal': ',', 'group': '.'}
	if lang == "pt": return {'decimal': ',', 'group': '.'}
	if lang == "ro": return {'decimal': ',', 'group': '.'}
	if lang == "ru": return {'decimal': ',', 'group': '\xa0'}
	if lang == "sd": return {'decimal': '.', 'group': ','}
	if lang == "si": return {'decimal': '.', 'group': ','}
	if lang == "sk": return {'decimal': ',', 'group': '\xa0'}
	if lang == "sl": return {'decimal': ',', 'group': '.'}
	if lang == "so": return {'decimal': '.', 'group': ','}
	if lang == "sq": return {'decimal': ',', 'group': '\xa0'}
	if lang == "sr": return {'decimal': ',', 'group': '.'}
	if lang == "sv": return {'decimal': ',', 'group': '\xa0'}
	if lang == "sw": return {'decimal': '.', 'group': ','}
	if lang == "ta": return {'decimal': '.', 'group': ','}
	if lang == "te": return {'decimal': '.', 'group': ','}
	if lang == "th": return {'decimal': '.', 'group': ','}
	if lang == "tk": return {'decimal': ',', 'group': '\xa0'}
	if lang == "tr": return {'decimal': ',', 'group': '.'}
	if lang == "uk": return {'decimal': ',', 'group': '\xa0'}
	if lang == "und": return {'decimal': '.', 'group': ','}
	if lang == "ur": return {'decimal': '.', 'group': ','}
	if lang == "uz": return {'decimal': ',', 'group': '\xa0'}
	if lang == "vi": return {'decimal': ',', 'group': '.'}
	if lang == "yo": return {'decimal': '.', 'group': ','}
	if lang == "yue": return {'decimal': '.', 'group': ','}
	if lang == "zh": return {'decimal': '.', 'group': ','}
	if lang == "zu": return {'decimal': '.', 'group': ','}
