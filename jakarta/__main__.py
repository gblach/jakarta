#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

import tomllib
from .tool import Tool

def main():
	file = open('jakarta.toml', 'rb')
	config = tomllib.load(file)
	Tool(config).main()

if __name__ == '__main__':
	main()
