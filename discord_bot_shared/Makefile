# Use Python 3.11 explicitly
PYTHON = python

# AWS CDK executable
CDK = cdk

.PHONY: install lint format test synth deploy all

install:
	@echo "Installing dependencies..."
	$(PYTHON) -m pip install -r requirements.txt

lint:
	@echo "Running flake8 linting..."
	flake8 .

format:
	@echo "Running black formatter..."
	black .

test:
	@echo "Running pytest..."
	pytest

synth:
	@echo "Synthesizing CDK stack..."
	cd src/cdk && $(CDK) synth

deploy:
	@echo "Deploying CDK stack..."
	$(CDK) deploy --require-approval never

all: install lint format test synth deploy
