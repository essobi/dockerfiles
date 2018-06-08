FROM jenkins:1.651.3  
  
ENV DOCKER_VERSION=1.9.1 \  
RANCHER_COMPOSE_VERSION=0.8.6  
  
USER root  
  
RUN cd / && \  
# install docker client  
curl -O -sSL
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz && \  
tar -xzvf docker-${DOCKER_VERSION}.tgz && \  
rm docker-${DOCKER_VERSION}.tgz && \  
groupadd -g 999 docker && \  
usermod -a -G docker jenkins && \  
# install build-essential  
apt-get update && \  
apt-get install -y build-essential python2.7 python-pip && \  
# install rancher-compose  
curl -O -sSL
https://releases.rancher.com/compose/v${RANCHER_COMPOSE_VERSION}/rancher-
compose-linux-amd64-v${RANCHER_COMPOSE_VERSION}.tar.gz && \  
tar -xzvf rancher-compose-linux-amd64-v${RANCHER_COMPOSE_VERSION}.tar.gz && \  
mv rancher-compose-v${RANCHER_COMPOSE_VERSION}/rancher-compose /usr/local/bin
&& \  
rm rancher-compose-linux-amd64-v${RANCHER_COMPOSE_VERSION}.tar.gz && \  
rm -rf rancher-compose-v${RANCHER_COMPOSE_VERSION}/ && \  
# insall aws cli  
pip install awscli  
  
USER jenkins  

