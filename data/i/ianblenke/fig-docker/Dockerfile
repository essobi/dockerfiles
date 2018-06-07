FROM ubuntu  
MAINTAINER Ian Blenke <ian@blenke.com>  
  
RUN set -x ; \  
export LC_ALL=C.UTF-8 ; \  
export DEBIAN_FRONTEND=noninteractive ; \  
apt-get update -y && \  
apt-get install -y wget python-pip && \  
pip install -U fig  
  
# Add the docker command as well  
RUN mkdir -p /usr/local/bin && \  
wget -qO /usr/local/bin/docker --no-check-certificate
https://test.docker.io/builds/`uname -s`/`uname -m`/docker-latest && \  
chmod +x /usr/local/bin/docker  
  
VOLUME /app  
WORKDIR /app  
  
CMD fig  

