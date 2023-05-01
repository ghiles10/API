build:
	docker-compose build

test:
	docker-compose up --abort-on-container-exit --exit-code-from test-app test-app

run:
	docker-compose up app

down:
	docker-compose down
