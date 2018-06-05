FROM jpetazzo/dind:latest  
MAINTAINER Patrik Votocek <patrik@votocek.cz>  
  
RUN apt-get update -yqq && \  
apt-get upgrade -yqq && \  
apt-get install curl wget -yqq && \  
curl -sSL https://get.docker.com/ | sh && \  
apt-get install docker-engine -yqq && \  
apt-get clean -yqq && \  
apt-get autoremove -yqq  
  
ENV DOCKER_DAEMON_ARGS="--storage-driver=vfs"  
ENTRYPOINT ["wrapdocker"]  
CMD []  

