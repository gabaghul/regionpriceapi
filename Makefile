make install-poetry:
	echo === Installing poetry ===
	curl -sSL https://install.python-poetry.org | python3 -

make env:
	echo == Installing dependencies ===
	poetry install

make run-regionprice-api:
	echo == Running region price API ===
	python main.py