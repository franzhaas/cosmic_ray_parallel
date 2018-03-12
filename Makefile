init:
	pip install pipenv
	pipenv install --dev  --skip-lock
	pipenv install -e .

test:
	cd test && 	pipenv run python -m robot accept.robot
