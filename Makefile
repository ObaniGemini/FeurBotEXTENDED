all: deps build
	./main.bin

deps:
	pip install -U discord.py

build:
	nuitka3 main.py

clean:
	rm -rf main.b*
	truncate --size 0 token.txt