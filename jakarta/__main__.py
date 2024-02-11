import tomllib
from .tool import Tool

def main():
	file = open('jakarta.toml', 'rb')
	config = tomllib.load(file)
	Tool(config).main()

if __name__ == '__main__':
	main()
