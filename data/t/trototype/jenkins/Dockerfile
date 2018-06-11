FROM jenkins:1.642.1  
MAINTAINER kerem tiryaki <keremtiryaki@gmail.com>  
  
# Suppress apt installation warnings  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Change to root user  
USER root  
  
# Used to set the docker group ID  
# Set to 497 by default, which is the group ID used by AWS Linux ECS Instance  
ARG DOCKER_GID=497  
# Create Docker Group with GID  
# Set default value of 497 if DOCKER_GID set to blank string by Docker Compose  
RUN groupadd -g ${DOCKER_GID:-497} docker  
  
# Used to control Docker and Docker Compose versions installed  
# NOTE: As of February 2016, AWS Linux ECS only supports Docker 1.9.1  
ARG DOCKER_ENGINE=1.10.2  
ARG DOCKER_COMPOSE=1.6.2  
# Install base packages  
RUN apt-get update -y && \  
apt-get install apt-transport-https curl python-dev python-setuptools gcc make
libssl-dev -y && \  
easy_install pip  
  
# Install Docker Engine  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D && \  
echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" | tee
/etc/apt/sources.list.d/docker.list && \  
apt-get update -y && \  
apt-get purge lxc-docker* -y && \  
apt-get install docker-engine=${DOCKER_ENGINE:-1.10.2}-0~trusty -y && \  
usermod -aG docker jenkins && \  
usermod -aG users jenkins  
  
# Install Docker Compose  
RUN pip install docker-compose==${DOCKER_COMPOSE:-1.6.2} && \  
pip install 'ansible==2.1.0' boto boto3  
  
# Change to jenkins user  
USER jenkins  
  
# Add Jenkins plugins  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt

