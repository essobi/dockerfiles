FROM node:7-slim  
MAINTAINER Matthew Hartstonge <matt@mykro.co.nz>  
  
ENV DOCKER_VERSION="1.13.0-0~debian-jessie"  
# Valid versions  
# 1.13.0-0~debian-jessie  
# 1.12.6-0~debian-jessie  
# 1.12.5-0~debian-jessie  
# 1.12.4-0~debian-jessie  
# 1.12.3-0~jessie  
# 1.12.2-0~jessie  
# 1.12.1-0~jessie  
# 1.12.0-0~jessie  
# 1.11.2-0~jessie  
# 1.11.1-0~jessie  
# 1.11.0-0~jessie  
# 1.10.3-0~jessie  
# 1.10.2-0~jessie  
# 1.10.1-0~jessie  
# 1.10.0-0~jessie  
# 1.9.1-0~jessie  
# 1.9.0-0~jessie  
# 1.8.3-0~jessie  
# 1.8.2-0~jessie  
# 1.8.1-0~jessie  
# 1.8.0-0~jessie  
# 1.7.1-0~jessie  
# 1.7.0-0~jessie  
# 1.6.2-0~jessie  
# 1.6.1-0~jessie  
# 1.6.0-0~jessie  
# 1.5.0-0~jessie  
  
RUN apt-get update \  
&& apt-get install -y \  
apt-transport-https \  
ca-certificates \  
g++ \  
make \  
python \  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& echo "deb https://apt.dockerproject.org/repo debian-jessie main" >>
/etc/apt/sources.list.d/docker.list \  
&& apt-get update && apt-get install -y \  
docker-engine="${DOCKER_VERSION}" \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

