#This is an extreamly basic makefile. Not really required

all: lint doc test


doc:
	pdoc --force --html --output-dir ./docs anthill

test:
	pytest

lint:
	pylint anthill

clean:
	rm -rf docs
