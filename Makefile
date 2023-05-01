build:
	docker-compose build

test:
	docker-compose up  --exit-code-from test-app test-app

run:
	docker-compose up app

down:
	docker-compose down
