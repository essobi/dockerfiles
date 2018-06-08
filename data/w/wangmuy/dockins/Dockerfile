FROM jenkins  
  
MAINTAINER Zhongdi Wang <wangmuy@gmail.com>  
  
USER root  
COPY sources.ustc.list /etc/apt/sources.list  
RUN apt-get -q update && \  
apt-get install -y ca-certificates \  
curl  
  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 1.11.2  
RUN set -x \  
&& curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz" -o
docker.tgz \  
&& tar -xzvf docker.tgz \  
&& if [ -d docker ]; then mv docker/* /usr/local/bin/; fi \  
&& if [ -d docker ]; then rmdir docker; fi \  
&& rm docker.tgz \  
&& docker -v

