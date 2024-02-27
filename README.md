# Jakarta

Jakarta is a modern localization framework, heavily inspired by GNU Gettext,
but enhanced in some areas:

1. Jakarta has built-in support for automatic online translation.

2. All translations are kept in only two files.
One file is human friendly and one is machine friendly.
GNU Gettext needs two files per language + one template file.
Some implementations of Gettext (including the original one) require a special directory structure,
which makes them more difficult to handle.

3. Jakarta has a more readable file structure, especially multiple plural forms are better marked.

4. Will provide similar developer experience in all supported programming languages.

## Components

Jakarta has two components:

1. Runtime library - required to run programs.

	The library must be rewritten in every supported programming language.
	Currently, only Python is supported.
	More programming languages will be supported in the future releases.

2. Toolchain - required to develop/localize programs.

	Written in Python, so it runs on Linux, Windows and MacOS.
	Unlike the runtime library, the toolchain supports all supported programming languages.


## How it works

*A complete example can be found in the [sample](sample/) directory.*

### 1. Write the configuration to ```jakarta.toml``` file.
The syntax of this file is described in [sample/jakarta.toml](sample/jakarta.toml).

```toml
[jakarta]
jafile = "hello_world.ja"
translate-to = [ "fr", "id", "nl", "pl", "pt", "tr" ]
translation-engine = "mozhi"

[sources]
python = [ "*.py" ]
```

### 2. Write hello world program to ```hello_world.py``` file.

```python
#!/usr/bin/env python

from jakarta import Jakarta

ja = Jakarta('hello_world.ja.cdb')

for lang in [ "en", "fr", "id", "nl", "pl", "pt", "tr" ]:
	ja.set_langs(lang)
	print(f'----- {lang} -----')
	print(ja._('Hello World!'))
	print(ja.p('{} month', '{} months', 1))
	print(ja.p('{} month', '{} months', 2))
	print(ja.o('Take the {} right.', 1))
	print(ja.o('Take the {} right.', 2))
	print(ja.n(1234567.89))
```

### 3. Run jakarta tool.

```
$ jakarta
```
or
```
$ python -m jakarta
```

This step will extract all translatable strings from source code
and try to translate them using selected translation engine.
It will create two files ```hello_world.ja``` and ```hello_world.ja.cdb```.
You can edit ```hello_world.ja``` by hand and then run jakarta tool agan.

### 4. Run ```./hello_world.py``` program.

It should write something like this to stdout:

```
----- en -----
Hello World!
1 month
2 months
Take the 1st right.
Take the 2nd right.
1,234,567.89
----- fr -----
Bonjour le monde !
1 mois
2 mois
Prendre la 1ère à droite.
Prendre la 2e à droite.
1 234 567,89
----- id -----
Hello World!
1 bulan
2 bulan
Ambil belokan ke kanan ke-1.
Ambil belokan ke kanan ke-2.
1.234.567,89
----- nl -----
Hallo Wereld!
1 maand
2 maanden
Neem de 1e rechts.
Neem de 2e rechts.
1.234.567,89
----- pl -----
Hello World!
1 miesiąc
2 miesiące
Skręć w 1. w prawo.
Skręć w 2. w prawo.
1 234 567,89
----- pt -----
Olá mundo!
1 mês
2 meses
Vire na 1ª à direita.
Vire na 2ª à direita.
1.234.567,89
----- tr -----
Merhaba Dünya!
1 ay
2 ay
1. sağdan girin.
2. sağdan girin.
1.234.567,89
```

## Future plans

- Add support for more programming languages.
- Add support for date and time formatting.
- Add support for formatting currencies.
- Add support for more automatic translation engines.
- Fix as many bugs as possible.
