############################################################  
# Dockerfile to run Apache usergrid_  
# Based on Ubuntu Image  
############################################################  
  
# Set the base image to use to Ubuntu  
FROM ubuntu  
  
MAINTAINER Gabor Wnuk <gabor.wnuk@me.com>  
  
RUN mkdir /usergrid-portal  
WORKDIR /usergrid-portal  
  
#RUN apt-get update;  
#RUN apt-get install build-essential;  
#RUN apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev
libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev;  
  
#RUN add-apt-repository ppa:fkrull/deadsnakes  
RUN apt-get update  
RUN apt-get install -y python  
  
ADD usergrid-portal /usergrid-portal  
  
EXPOSE 3000  
  
CMD python -m SimpleHTTPServer 3000

