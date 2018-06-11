FROM wiss013/jenkins  
MAINTAINER BEN CHAABEN Wissem <benchaaben.wissem@gmail.com>  
  
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
RUN yum update -y && \  
yum install -y curl python-devel gcc make wget  
  
#Install pip  
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && \  
python get-pip.py  
  
# Install Docker Engine  
RUN yum remove -y docker docker-common docker-selinux docker-engine && \  
yum install -y yum-utils device-mapper-persistent-data lvm2 && \  
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-
ce.repo && \  
yum install -y docker-ce && \  
usermod -aG docker jenkins && \  
usermod -aG users jenkins  
  
# Install Docker Compose  
RUN pip install docker-compose && \  
pip install ansible boto boto3  
  
# Add Jenkins plugins  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
  

