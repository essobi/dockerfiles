FROM jenkins:2.46.3  
#FROM jenkins:1.642.1  
MAINTAINER Yogi S <yogi29aus@gmail.com>  
  
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
#ARG DOCKER_ENGINE=1.10.2  
#ARG DOCKER_COMPOSE=1.6.2  
# Install base packages  
RUN apt-get update -y && \  
apt-get install apt-transport-https ca-certificates curl software-properties-
common gnupg2 -y && \  
apt-get install python-pip python-pip-whl python-dev python-setuptools gcc
make libssl-dev -y && \  
apt-get install sudo ansible python-boto -y && \  
pip install boto3  
  
# Install Docker-CE  
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - &&
\  
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian
$(lsb_release -cs) stable" && \  
apt-get update -y && \  
apt-get install docker-ce -y && \  
usermod -aG docker jenkins && \  
usermod -aG users jenkins  
  
# Install Docker-Compose  
RUN curl -L https://github.com/docker/compose/releases/download/1.13.0/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  
# Add user to /etc/sudoers & Change to jenkins user  
RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
#chmod 777 /var/run/docker.sock && \  
USER jenkins  
  
# Add Jenkins plugins  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  

