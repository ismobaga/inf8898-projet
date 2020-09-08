

.PHONY: install run gen-data


run: src/bench.py
	python src/bench.py

gen-data: src/data.py
	python src/bench.py

install:
	pip install -Ur requirements.txt