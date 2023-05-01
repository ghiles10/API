build : 
	docker-compose build

test : 
	docker-compose up test-app 

run : 
	docker-compose up app 
	
down : 
	docker-compose down 
