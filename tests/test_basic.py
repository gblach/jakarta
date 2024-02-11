import pytest
import tomllib
from pathlib import Path
from jakarta import Jakarta
from jakarta.tool import Tool
from jakarta import generated as gen

@pytest.fixture(scope='session')
def cdbfile(tmp_path_factory):
	jafile = str(tmp_path_factory.mktemp('basic') / (Path(__file__).stem + '.ja'))
	with open(jafile, 'w') as f:
		f.write('''
en = "Hello world"
pl = "Witaj świecie"
de = ""

en.one = "{} month"
en.other = "{} months"
pl.one = "{} miesiąc"
pl.few = "{} miesiące"
pl.many = "{} miesięcy"
pl.other = "{} miesiąca"
de.one = ""
de.other = ""

en.ord = "Take the {} right."
pl.other = "Skręć w {}. w prawo."
''')
	config = tomllib.loads(f'''
jafile = "{jafile}"
lang = "python"
sources = ["{__file__}"]
''')
	yield Tool(config).main()

def test_generate(cdbfile):
	assert cdbfile

def test_en(cdbfile):
	ja = Jakarta(cdbfile)
	assert ja._('Hello world') == 'Hello world'
	ja.set_langs('en', 'de')
	assert ja._('Hello world') == 'Hello world'
	ja.set_langs('de', 'en')
	assert ja._('Hello world') == 'Hello world'
	ja.set_langs('de')
	assert ja._('Hello world') == 'Hello world'

def test_pl(cdbfile):
	ja = Jakarta(cdbfile)
	ja.set_langs('en', 'de', 'pl')
	assert ja._('Hello world') == 'Witaj świecie'
	ja.set_langs('pl', 'de', 'en')
	assert ja._('Hello world') == 'Witaj świecie'

def test_not_translated(cdbfile):
	ja = Jakarta(cdbfile)
	ja.set_langs('pl')
	assert ja._('Not translated') == 'Not translated'

def test_en_plurals(cdbfile):
	ja = Jakarta(cdbfile)
	ja.set_langs('en')
	assert ja.p('{} month', '{} months', 1) == '1 month'
	assert ja.p('{} month', '{} months', 2) == '2 months'
	ja.set_langs('de')
	assert ja.p('{} month', '{} months', 1) == '1 month'
	assert ja.p('{} month', '{} months', 2) == '2 months'

def test_pl_plurals(cdbfile):
	ja = Jakarta(cdbfile)
	ja.set_langs('pl')
	assert ja.p('{} month', '{} months', 1) == '1 miesiąc'
	assert ja.p('{} month', '{} months', 2) == '2 miesiące'
	assert ja.p('{} month', '{} months', 5) == '5 miesięcy'
	assert ja.p('{} month', '{} months', 1.5) == '1.5 miesiąca'

def test_en_ordinals(cdbfile):
	ja = Jakarta(cdbfile)
	ja.set_langs('en')
	assert ja.o('Take the {} right.', 1) == 'Take the 1st right.'
	assert ja.o('Take the {} right.', 2) == 'Take the 2nd right.'
	assert ja.o('Take the {} right.', 3) == 'Take the 3rd right.'
	assert ja.o('Take the {} right.', 4) == 'Take the 4th right.'

def test_pl_ordinals(cdbfile):
	ja = Jakarta(cdbfile)
	ja.set_langs('pl')
	assert ja.o('Take the {} right.', 1) == 'Skręć w 1. w prawo.'
	assert ja.o('Take the {} right.', 2) == 'Skręć w 2. w prawo.'
	assert ja.o('Take the {} right.', 3) == 'Skręć w 3. w prawo.'
	assert ja.o('Take the {} right.', 4) == 'Skręć w 4. w prawo.'

def test_plural_rules():
	assert gen.plural_rules('en') == [('one', 1), ('other', 2)]
	assert gen.plural_rules('pl') == [('one', 1), ('few', 2), ('many', 5), ('other', 1.5)]
	assert gen.plural_rules('xx') == []

def test_ordinal_rules():
	assert gen.ordinal_rules('en') == [('one', 1), ('two', 2), ('few', 3), ('other', 4)]
	assert gen.ordinal_rules('pl') == [('other', 15)]
	assert gen.ordinal_rules('xx') == []
