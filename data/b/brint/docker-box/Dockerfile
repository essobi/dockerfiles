FROM alpine:3.5  
MAINTAINER Brint O'Hearn <brint.ohearn@rackspace.com>  
  
ENV DOCKER_COMPOSE_VERSION 1.11.1  
ENV DOCKER_MACHINE_VERSION 0.9.0  
  
RUN apk update && apk upgrade && apk add \--no-cache bash curl && \  
adduser -D -s /bin/bash user && \  
apk add \--no-cache \--repository http://dl-
cdn.alpinelinux.org/alpine/edge/main \--repository http://dl-
cdn.alpinelinux.org/alpine/edge/community docker && \  
curl -L
https://github.com/docker/machine/releases/download/v${DOCKER_MACHINE_VERSION}/docker-
machine-`uname -s`-`uname -m` >/usr/local/bin/docker-machine && \  
chmod +x /usr/local/bin/docker-machine && \  
apk \--update add py2-pip py-yaml && \  
pip install -U pip docker-compose==${DOCKER_COMPOSE_VERSION} && \  
rm -rf `find / -regex '.*\.py[co]' -or -name apk`  
  
WORKDIR /home/user  
USER user  
CMD ["/bin/bash"]  

