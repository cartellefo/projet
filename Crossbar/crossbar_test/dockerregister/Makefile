build:
	docker build -t regis .

run:
	docker run --name cbrreg publish &

clean:
	-docker stop cbrreg
	-docker rm cbrreg