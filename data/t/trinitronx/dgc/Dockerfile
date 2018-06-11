FROM odise/busybox-curl:2015.02  
ENV DOCKER_VERSION=1.11.2  
ENV DOCKER_COMPOSE_VERSION=1.7.1  
RUN \  
curl -L -o - https://get.docker.com/builds/$(uname -s)/$(uname
-m)/docker-${DOCKER_VERSION}.tgz | \  
gzip -d -c | \  
tar -C /tmp/ -xf - && mv /tmp/docker/* /usr/bin/ && mv /usr/bin/docker
/usr/bin/docker-${DOCKER_VERSION} && \  
ln -s /usr/bin/docker-${DOCKER_VERSION} /usr/bin/docker && chmod +x
/usr/bin/docker /usr/bin/docker-${DOCKER_VERSION}  
  
RUN \  
curl -L -o /usr/bin/docker-compose-${DOCKER_COMPOSE_VERSION}
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-$(uname -s)-$(uname -m) && \  
ln -s /usr/bin/docker-compose-${DOCKER_COMPOSE_VERSION} /usr/bin/docker-
compose && chmod +x /usr/bin/docker-compose /usr/bin/docker-
compose-${DOCKER_COMPOSE_VERSION}  
  
ADD . /src  
  
WORKDIR /src  
  
ENTRYPOINT ["/bin/sh", "/src/bin/dgc"]  
  
# vim: set ft=dockerfile :  

