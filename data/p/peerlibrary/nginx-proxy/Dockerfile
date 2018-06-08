FROM peerlibrary/nginx  
  
MAINTAINER Mitar <mitar.docker@tnode.com>  
  
ENV DOCKER_HOST unix:///docker.sock  
  
RUN apt-get update -q -q && \  
apt-get install wget ca-certificates \--yes \--force-yes && \  
mkdir /dockergen && \  
wget -P /dockergen https://github.com/jwilder/docker-
gen/releases/download/0.3.1/docker-gen-linux-amd64-0.3.1.tar.gz && \  
tar xvzf /dockergen/docker-gen-linux-amd64-0.3.1.tar.gz -C /dockergen && \  
apt-get purge wget ca-certificates \--yes \--force-yes && \  
apt-get autoremove \--yes \--force-yes  
  
COPY ./etc /etc  
COPY ./dockergen /dockergen  

