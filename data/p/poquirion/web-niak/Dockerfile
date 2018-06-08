# A server that load and show pictures  
# Set the base image to use to Ubuntu  
FROM ubuntu:15.04  
# Set the file maintainer (your name - the file's author)  
MAINTAINER P-O Quirion  
  
# Update the default application repository sources list  
RUN apt-get update  
  
RUN apt-get install -y wget python3-pip  
  
ENV TAG=latest  
  
ENV PROJECT_ROOT_IN_DOCKER=/home/web_niak-${TAG}/niak_server/niak_server/  
# get the image  
RUN cd /home && wget https://github.com/SIMEXP/web_niak/archive/${TAG}.tar.gz
&& tar -zxvf ${TAG}.tar.gz  
  
RUN cd ${PROJECT_ROOT_IN_DOCKER}../ && python3 setup.py develop  
  
# VOLUME  
WORKDIR ${PROJECT_ROOT_IN_DOCKER}../  
  
# ENTRYPOINT ["pserve", "development.ini"]  

