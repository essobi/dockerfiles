FROM dodb/jenkins-java-slave  
MAINTAINER David Op de Beeck <davidopdebeeck@hotmail.com>  
  
# Docker  
RUN \  
cd /opt && wget https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz
&& \  
tar -xvzf docker-latest.tgz && \  
mv docker/* /usr/bin/  
  
ENV DOCKER_TLS_VERIFY true  
ENV DOCKER_CERT_PATH /etc/docker/certs  

