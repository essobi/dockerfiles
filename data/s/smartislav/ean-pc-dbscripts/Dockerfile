FROM debian:jessie  
  
MAINTAINER Ilya Epifanov <elijah.epifanov@gmail.com>  
  
RUN apt-get update &&\  
apt-get install -y mysql-client wget unzip --no-install-recommends &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD . /ean  
  
VOLUME /ean/eanfiles  
VOLUME /ean/eanextras  
  
WORKDIR /ean  
  
RUN ln -sfT config-docker.sh config.sh  

