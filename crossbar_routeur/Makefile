
run: clean
	docker run -d -p 8080:8080 --name="crossbar-router" crossbario/crossbar

clean:
	-docker stop crossbar-router
	-docker rm crossbar-router