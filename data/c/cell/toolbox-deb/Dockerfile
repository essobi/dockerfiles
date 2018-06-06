FROM cell/debsandbox  
MAINTAINER Cell <maintainer.docker.cell@outer.systems>  
ENV DOCKER_IMAGE="cell/toolbox-deb"  
#Docker-compose  
ENV DOCKER_COMPOSE_VERSION=1.9.0  
RUN echo "Install docker-compose ${DOCKER_COMPOSE_VERSION}" &&\  
curl -sSL
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` \  
> /usr/local/bin/docker-compose &&\  
chmod +x /usr/local/bin/docker-compose  
  
#Import scripts  
RUN echo "Import scripts" &&\  
git clone https://github.com/Cellophan/scripts.git /tmp/scripts &&\  
find /tmp/scripts -maxdepth 1 -type f -executable -exec cp {} /usr/local/bin/
\; &&\  
rm -rf /tmp/scripts  
  
ADD material/payload /opt/payload/  
ADD material/scripts /usr/local/bin/  
RUN /usr/local/bin/dc install  
  
#zsh  
RUN echo "Install zsh" &&\  
apt-get update && apt-get install -y --no-install-recommends zsh &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/*  
  

