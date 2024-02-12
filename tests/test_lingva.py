#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

import pytest
import tomllib
from pathlib import Path
from jakarta import Jakarta
from jakarta.tool import Tool

@pytest.fixture(scope='session')
def cdbfile(tmp_path_factory):
	jafile = str(tmp_path_factory.mktemp('lingva') / (Path(__file__).stem + '.ja'))
	config = tomllib.loads(f'''
jafile = "{jafile}"
lang = "python"
sources = ["{__file__}"]
translate-to = [ "id", "mt", "pl", "pt", "tr" ]
translation-engine = "lingva"
''')
	yield Tool(config).main()

def test_simple(cdbfile):
	ja = Jakarta(cdbfile)
	ja.set_langs('en')
	assert ja._('Hello world') == 'Hello world'
	ja.set_langs('id')
	assert ja._('Hello world') == 'Halo Dunia'
	ja.set_langs('mt')
	assert ja._('Hello world') == 'Hello dinja'
	ja.set_langs('pl')
	assert ja._('Hello world') == 'Witaj świecie'
	ja.set_langs('pt')
	assert ja._('Hello world') == 'Olá Mundo'
	ja.set_langs('tr')
	assert ja._('Hello world') == 'Selam Dünya'

def test_plurals(cdbfile):
	ja = Jakarta(cdbfile)
	ja.set_langs('en')
	assert ja.p('{} month', '{} months', 1) == '1 month'
	assert ja.p('{} month', '{} months', 2) == '2 months'
	ja.set_langs('id')
	assert ja.p('{} month', '{} months', 15) == '15 bulan'
	ja.set_langs('mt')
	assert ja.p('{} month', '{} months', 1) == '1 xahar'
	assert ja.p('{} month', '{} months', 2) == '2 xhur'
	assert ja.p('{} month', '{} months', 3) == '3 xhur'
	assert ja.p('{} month', '{} months', 11) == '11-il xahar'
	assert ja.p('{} month', '{} months', 20) == '20 xahar'
	ja.set_langs('pl')
	assert ja.p('{} month', '{} months', 1) == '1 miesiąc'
	assert ja.p('{} month', '{} months', 2) == '2 miesiące'
	assert ja.p('{} month', '{} months', 5) == '5 miesięcy'
	assert ja.p('{} month', '{} months', 6) == '6 miesięcy'
	assert ja.p('{} month', '{} months', 1.5) == '1.5 miesiąca'
	assert ja.p('{} month', '{} months', 1.6) == '1.6 miesiąca'
	ja.set_langs('pt')
	assert ja.p('{} month', '{} months', 1) == '1 mês'
	assert ja.p('{} month', '{} months', 1000000) == '1 milhão de meses'
	assert ja.p('{} month', '{} months', 2) == '2 meses'
	ja.set_langs('tr')
	assert ja.p('{} month', '{} months', 1) == '1 ay'
	assert ja.p('{} month', '{} months', 2) == '2 ay'

def test_ordinals(cdbfile):
	ja = Jakarta(cdbfile)
	ja.set_langs('pl')
	assert ja.o('Take the {} right.', 1) == 'Skręć w 1-tą w prawo.'
	assert ja.o('Take the {} right.', 2) == 'Skręć w 2-tą w prawo.'
	assert ja.o('Take the {} right.', 3) == 'Skręć w 3-tą w prawo.'
	assert ja.o('Take the {} right.', 4) == 'Skręć w 4-tą w prawo.'
