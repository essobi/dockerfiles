FROM docker:latest  
  
RUN apk update  
RUN apk upgrade  
RUN apk add python python-dev py-pip build-base curl  
RUN curl -L https://github.com/docker/compose/releases/download/1.8.0/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
RUN pip install docker-compose

