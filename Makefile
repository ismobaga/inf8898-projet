# Only run install if requirements.txt is newer than vendored folder

.PHONY: install run


run: src/bench.py
	python src/bench.py

install:
	pip install -Ur requirements.txt