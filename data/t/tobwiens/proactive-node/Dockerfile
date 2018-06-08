# Use proactive scheduler image and change the entrypoint  
FROM tobwiens/proactive-scheduler:master  
MAINTAINER Tobias Wiens <https://github.com/tobwiens/proactive-node-
dockerfile/>  
  
ENV DOCKER_COMPOSE_VERSION 1.5.1  
# Install tools  
RUN ["/bin/bash", "-c", "apt-get install curl -y"]  
  
# Install the docker deamon inside the node; for the docker support.  
RUN wget -qO- https://get.docker.com/ | sh  
  
# Install Docker Compose  
RUN ["/bin/bash", "-c", "curl -L
https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose"]  
RUN ["/bin/bash", "-c", "chmod +x /usr/local/bin/docker-compose"]  
  
### VOLUMES  
VOLUME /var/lib/docker # It cannot be AUFS - so make it a volume  
  
# Run proactive scheduler with zero nodes and start the docker daemon with
/usr/local/bin/wrapdocker  
ADD container-start-script.sh /  
RUN ["/bin/bash", "-c", "chmod +x /container-start-script.sh"]  
ENTRYPOINT ["/container-start-script.sh", "-Dproactive.useIPaddress=true"]  

