From ubuntu

RUN apt-get update && apt-get -y upgrade  && apt-get install -y \
	python3-pip \
	python3

RUN pip3 install -U \
	numpy \
	txaio \
	twisted \
	autobahn

#run iptables -t nat -A  DOCKER -p tcp --dport 8080 -j DNAT --to-destination 127.0.0.1:8080
#expose 8080

COPY publish.py /.

CMD ["python3","publish.py"]

#crossbario/crossbar
#docker inspect  crossbario/crossbar | grep 127.0.0.1