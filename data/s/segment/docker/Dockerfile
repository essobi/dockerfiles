# This Dockerfile is used to build the base containers used for continuous  
# integration.  
FROM ubuntu:16.04  
# install dependencies  
RUN apt-get update && \  
apt-get install -y apt-transport-https ca-certificates build-essential git
curl libsystemd-dev && \  
apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D && \  
echo "deb https://apt.dockerproject.org/repo ubuntu-wily main" >
/etc/apt/sources.list.d/docker.list && \  
curl -s -L https://github.com/docker/compose/releases/download/1.7.1/docker-
compose-$(uname -s)-$(uname -m) > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose && \  
apt-get update && \  
apt-get install -y docker-engine=1.9.1-0~wily && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/*  
  
# configure the container's entrypoint  
COPY files/Makefile.docker /usr/src/Makefile.docker  
ENTRYPOINT ["make", "-f", "/usr/src/Makefile.docker"]  

