From ubuntu


RUN apt-get update && apt-get -y upgrade  && apt-get install -y python3-pip python3
RUN pip3 install numpy 
RUN pip3 install txaio
RUN pip3 install twisted
Run pip3 install autobahn

COPY register.py /.