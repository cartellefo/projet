FROM ubuntu
MAINTAINER Cartelle

RUN apt-get update && apt-get -y upgrade  && apt-get install -y python3-pip python3
RUN pip3 install numpy

COPY partialsum.py /.


CMD ["python3","partialsum.py"]
