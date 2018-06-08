FROM jenkins:2.60.2  
MAINTAINER oliosinter <olio.sinter@gmail.com>  
  
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
  
RUN apt-get update -y && \  
apt-get install apt-transport-https ca-certificates curl gnupg2 software-
properties-common python-dev python-setuptools gcc make libssl-dev -y && \  
easy_install pip  
  
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - &&
\  
apt-key fingerprint 0EBFCD88  
  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/debian \  
$(lsb_release -cs) \  
stable"  
  
RUN apt-get update -y && \  
apt-get install docker-ce=17.06.0~ce-0~debian -y && \  
usermod -aG staff jenkins && \  
usermod -aG docker jenkins  
# usermod -aG users jenkins  
# Install Docker Compose  
RUN pip install docker-compose==1.14.0 && \  
pip install ansible boto boto3  
  
# Change to jenkins user  
USER jenkins  
  
# Add Jenkins plugins  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN xargs /usr/local/bin/install-plugins.sh < //usr/share/jenkins/plugins.txt

