From postgres

RUN docker run -d -p 5432:5432 postgres
RUN docker exec -it 0e6ad7f20137 bash
RUN  psql -U postgres
Run  copy sqlcode.sql
RUN sqlcode.sql
#RUN sudo docker pull helmi03/docker-postgis
#RUN sudo docker run -d -p 5432:5432 helmi03/docker-postgis
#RUN sudo docker commit <ID> postgis-empty
#RUN sudo docker commit <ID> geotrek-0.28-empty
#RUN sudo docker commit <ID> geotrek-0.28-demo

#RUN $ sudo docker images
# RUN $ sudo docker ps
# sudo docker stop ID