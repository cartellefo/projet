build:
	docker build -t publish .

run:
	docker run --name cbrpub --net container:b9824e32f61c publish 

clean:
	-docker stop cbrpub
	-docker rm cbrpub