FROM centos:7  
MAINTAINER Przemyslaw Ozgo linux@ozgo.info  
  
ENV DOCKER_PORT=2375 \  
DOCKER_COMPOSE_VERSION=1.7.1  
COPY container-files /  
  
RUN \  
rpm --rebuilddb && yum clean all && \  
yum install -y docker-engine && \  
yum clean all && \  
curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  
EXPOSE 2375  
ENTRYPOINT ["/bootstrap.sh"]  

