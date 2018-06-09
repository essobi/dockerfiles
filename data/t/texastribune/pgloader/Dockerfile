#FROM x110dc/dev-base  
FROM ubuntu:14.04  
MAINTAINER tech@texastribune.org  
  
RUN apt-get update  
RUN apt-get install -yq wget freetds-common freetds-dev libct4 libsybdb5  
  
RUN mkdir /app  
RUN cd /app && \  
wget -nv -O pgloader.deb
http://pgloader.io/files/pgloader_3.2.0+dfsg-1_amd64.deb && \  
dpkg -i pgloader.deb && \  
rm pgloader.deb  

