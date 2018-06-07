FROM docker:1.10-dind  
MAINTAINER Yves Serrano <y@yas.ch>  
ENV DOCKER_COMPOSE_VERSION=1.6.2  
FROM docker:1.11-dind  
MAINTAINER Yves Serrano <y@yas.ch>  
ENV DOCKER_COMPOSE_VERSION=1.7.1  
  
RUN apk add --update \  
bash \  
python \  
py-pip \  
curl \  
git \  
git-perl \  
make \  
openssh-client \  
tar \  
rsync \  
findutils \  
&& rm -rf /var/cache/apk/* && \  
pip install docker-compose==$DOCKER_COMPOSE_VERSION  
  
ADD dockerd-entrypoint.sh /usr/local/bin/  

