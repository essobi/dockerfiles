FROM jpetazzo/dind  
  
RUN apt-get update && apt-get install -y -q curl git  
  
RUN curl -L https://github.com/docker/compose/releases/download/1.2.0/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  

