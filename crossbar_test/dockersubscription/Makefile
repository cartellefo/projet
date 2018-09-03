build:
	docker build -t subscribe .

run:
	docker run --name cbrsub publish &

clean:
	-docker stop cbrsub
	-docker rm cbrsub