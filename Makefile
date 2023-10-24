@all:
	./venv/bin/python -m main

i:
	./venv/bin/python

clean:
	rm -rf $(find lib -name __pycache__) __pycache__/
