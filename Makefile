.PHONY: usage clean build run tests lint

usage:
	@echo "Available commands:"
	@echo "\tclean - stop the running containers and remove the volumes and network"
	@echo "\tbuild - build the docker image"
	@echo "\trun - run program"
	@echo "\ttests - run tests"
	@echo "\tlint - run flake8"

clean:
	find . -type f -name '*.pyc' -exec rm -f {} ';'
	find . -type d -name '__pycache__' -exec rm -f {} ';'
	docker-compose down

build: clean
	docker-compose build

tests: build
	docker-compose run zopa_example bash -c "python -m pytest /zopa-example/tests/*.py"

lint:
	docker-compose run zopa_example bash -c "flake8 /zopa-example"

run: build
	docker-compose run zopa_example bash
