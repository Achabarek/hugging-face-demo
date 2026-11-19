
install:
	python -m pip install --upgrade pip && \
	python -m pip install -r requirements.txt && \
	python -m pip install black pylint

test:
	python -m pytest -vv --cov=hello --cov=greeting \
		--cov=math --cov=web tests
	python -m pytest --nbval notebook.ipynb # tests my Jupyter notebook
	# python -m pytest -v tests/test_web.py # if I just want to test web

debug:
	python -m pytest -vv --pdb tests/ # Debugger is invoked

one-test:
	python -m pytest -vv tests/test_train.py::test_model_training

debugthree:
	python -m pytest -vv --pdb --maxfail=3

format:
	black *.py tests/

lint:
	pylint --disable=R,C *.py

all: install lint test format