#!/usr/bin/env python

from jakarta import Jakarta

# Create jakarta object with path to cdbfile passed as argument.
# Cdbfile can be None (or omitted), but then only number formatting can be used.
ja = Jakarta('hello_world.ja.cdb')

for lang in [ "en", "fr", "id", "nl", "pl", "pt", "tr" ]:
	# Set the language or languages you'd like to use for display.
	# If you set more than one language, the first one found will be used.
	# To do this, pass languages as additional arguments,
	# e.g. ja.set_langs('en', 'fr', 'id', 'nl', 'pl', 'pt', 'tr')
	ja.set_langs(lang)

	print(f'----- {lang} -----')

	# Display 'Hello World!' in the selected language.
	print(ja._('Hello World!'))

	# Display the correct form depending on the number passed as the third argument.
	print(ja.p('{} month', '{} months', 1))
	print(ja.p('{} month', '{} months', 2))

	# Same as above, but use ordinal number formatting instead of cardinal one.
	print(ja.o('Take the {} right.', 1))
	print(ja.o('Take the {} right.', 2))

	# Display number according to number formatting rules in the selected language.
	print(ja.n(1234567.89))
