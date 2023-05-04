all:
	pip install -U discord.py
	nuitka3 main.py
	./main.bin

clean:
	rm -rf main.b*
	truncate --size 0 token.txt