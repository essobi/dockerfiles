FROM ubuntu:16.04  
# Set environment variables.  
ENV \  
DOCKER_COMPOSE_BIN_NIX="/usr/local/bin/docker-compose" \  
REQUIREMENTS_DOCKER='17.04.0-ce' \  
REQUIREMENTS_DOCKER_COMPOSE='1.11.0' \  
URL_DOCKER_NIX="https://get.docker.com/"  
# Base tools.  
RUN \  
apt-get update && \  
apt-get install -y curl && \  
apt-get install -y sudo && \  
apt-get install -y uuid-runtime && \  
rm -rf /var/lib/apt/lists/*  
  
# Docker.  
RUN curl -fsSL ${URL_DOCKER_NIX} | sh  
  
# Docker compose.  
RUN \  
curl -fL#
https://github.com/docker/compose/releases/download/${REQUIREMENTS_DOCKER_COMPOSE}/docker-
compose-Linux-x86_64 -o "$DOCKER_COMPOSE_BIN_NIX" && \  
chmod +x "$DOCKER_COMPOSE_BIN_NIX"  
  
# Install Docksal.  
RUN \  
mkdir -p /usr/local/bin && \  
curl -fsSL https://raw.githubusercontent.com/docksal/docksal/master/bin/fin -o
/usr/local/bin/fin && \  
chmod +x /usr/local/bin/fin  
  
# Create Docksal user.  
RUN \  
newgrp docker && \  
useradd -c 'Docksal user' -m -d /home/docksal -s /bin/bash -G docker,staff
docksal  
  
# Change user.  
USER docksal  
  
# Confgure docksal.  
RUN fin update --config  
  
WORKDIR /var/www  
VOLUME ["/var/www"]

