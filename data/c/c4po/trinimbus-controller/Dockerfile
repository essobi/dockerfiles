From ubuntu:vivid  
  
RUN apt-get update && apt-get install -y curl unzip vim  
  
#install docker engine  
RUN curl https://get.docker.com|sh  
  
#install docker-machine  
RUN curl -L https://github.com/docker/machine/releases/download/v0.5.0/docker-
machine_linux-amd64.zip >machine.zip && \  
unzip machine.zip && \  
rm machine.zip && \  
mv docker-machine* /usr/local/bin  
  
#install docker-compose  
RUN curl -L https://github.com/docker/compose/releases/download/1.5.1/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && chmod +x
/usr/local/bin/docker-compose  
  
ENV MACHINE_STORAGE_PATH=/machine-storage  
VOLUME /machine-storage  
  
COPY ./scripts/ /root/bin/  
  
WORKDIR /root/bin  
  
ENTRYPOINT bash

