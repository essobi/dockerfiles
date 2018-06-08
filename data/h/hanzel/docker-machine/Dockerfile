FROM alpine:edge  
  
ENV DOCKER_MACHINE_NAME=default  
ENV DOCKER_MACHINE_PORT=2376  
RUN apk -q update && apk add bash docker curl openssh-client py2-pip git jq  
  
RUN pip install docker-compose  
RUN docker-compose --version  
  
RUN curl -L
https://github.com/docker/machine/releases/download/v0.13.0/docker-
machine-`uname -s`-`uname -m` > /usr/bin/docker-machine && chmod +x
/usr/bin/docker-machine  
RUN docker-machine --version  
  
RUN pip install awscli  
RUN mkdir -p /root/.docker/machine  

