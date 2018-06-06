FROM jenkins:2.7.4  
USER root  
  
RUN apt-get update && apt-get install -y docker.io curl  
  
RUN curl -L https://github.com/docker/compose/releases/download/1.7.1/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
  
RUN chmod +x /usr/local/bin/docker-compose  
  
USER jenkins

