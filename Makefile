install:
	#install commands
	curl -sSL https://install.python-poetry.org | python3 - &&\
 		  poetry self update &&\
 		  poetry install

format:
	#format code
	black *.py app/../*.py

lint:
	#flake8 or #pylint
	pylint -j 4 --rcfile=pylint.rc app/

unittests:
	# Run all unittests
	python -m pytest app/tests/01_unit_tests
	coverage report --show-missing

integrationstests:
	# Run all integration tests
	python -m pytest app/tests/02_integration_tests


alltests: unittests integrationstests
