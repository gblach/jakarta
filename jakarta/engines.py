#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from string import Template
from requests import request
from requests.exceptions import *

ENGINES = {
	'lingva': {
		'method': 'GET',
		'url': 'https://$host/api/v1/en/$lang/$text',
		'host': 'lingva.lunar.icu',
		'json_key': 'translation',
	},
	'mozhi': {
		'method': 'GET',
		'url': 'https://$host/api/translate',
		'host': 'translate.bus-hit.me',
		'params': {
			'engine': '$engine',
			'from': 'en',
			'to': '$lang',
			'text': '$text',
		},
		'engine': 'deepl',
		'json_key': 'translated-text',
	},
	'mint': {
		'method': 'POST',
		'url': 'https://$host/api/translate',
		'host': 'translate.wmcloud.org',
		'body': {
			'format': 'text',
			'source_language': 'en',
			'target_language': '$lang',
			'content': '$text',
		},
		'json_key': 'translation',
	},
}

def translate(config: str, lang: str, text: str):
	engine = ENGINES[config['jakarta']['translation-engine']]
	if config['jakarta']['translation-engine'] in config:
		for k, v in config[config['jakarta']['translation-engine']].items():
			engine[k] = v
	url = Template(engine['url']).substitute(
		host=engine['host'],
		lang=lang,
		text=text,
	)
	params = {}
	if 'params' in engine:
		for k, v in engine['params'].items():
			params[k] = Template(v).substitute(
				engine=engine['engine'],
				lang=lang,
				text=text,
			)
	body = {}
	if 'body' in engine:
		for k, v in engine['body'].items():
			body[k] = Template(v).substitute(
				lang=lang,
				text=text,
			)
	headers = { 'Content-Type': 'application/json; charset=utf-8' }
	try:
		r = request(engine['method'], url, timeout=30, \
			headers=headers, params=params, json=body)
		if r.status_code == 200:
			return r.json()[engine['json_key']]
	except ReadTimeout:
		pass
