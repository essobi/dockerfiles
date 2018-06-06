FROM ceroic/jnlp-slave:2.59  
MAINTAINER Ceroic <ops@ceroic.com>  
  
ENV DOCKER_VERSION 1.11.2  
  
# Base image sets user to jenkins, switch back to root for this.  
USER root  
  
# Install Docker  
RUN \  
apt-get update && \  
apt-get install -y \  
apt-transport-https && \  
apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D && \  
echo 'deb https://apt.dockerproject.org/repo debian-jessie main' | tee
/etc/apt/sources.list.d/docker.list && \  
apt-get update && \  
apt-cache policy docker-engine && \  
apt-get install -y \  
apt-transport-https \  
docker-engine=${DOCKER_VERSION}-0~jessie && \  
gpasswd -a jenkins docker  

