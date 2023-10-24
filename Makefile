@all:
	echo "make [enter | leave | clean]"

clean:
	rm -rf $(find lib -name __pycache__) __pycache__/
