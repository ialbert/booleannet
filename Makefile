
BASEDIR=boolean2


all:develop test

clean:
	rm -rf *.egg-info; rm -rf $(BASEDIR)/*.egg-info
	rm -rf $(BASEDIR)/__pycache__; rm -f $(BASEDIR)/*.pyc
	rm -rf $(BASEDIR)/ply/__pycache__; rm -rf $(BASEDIR)/ply/*.pyc
	rm -rf $(BASEDIR)/plde/__pycache__; rm -f $(BASEDIR)/plde/*.pyc
	rm -rf build; rm -rf dist

install:
	python setup.py install

develop:
	python setup.py develop 

uninstall:
	python setup.py develop -u

test:
	python tests/test_all.py

	# Run unit tests on python files

	python $(BASEDIR)/boolmodel.py
	python $(BASEDIR)/network.py
	python $(BASEDIR)/ruleparser.py
	python $(BASEDIR)/state.py
	python $(BASEDIR)/timemodel.py
	python $(BASEDIR)/tokenizer.py
	python $(BASEDIR)/util.py



