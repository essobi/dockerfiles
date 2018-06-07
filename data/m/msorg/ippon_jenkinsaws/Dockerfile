FROM jenkins  
MAINTAINER Mallik Sambaraju <msambaraju@ipponusa.com>  
  
# Change to root user  
USER root  
  
ARG DOCKER_GID=497  
# Create Docker Group with GID  
# Set default value of 497 if DOCKER_GID set to blank string by Docker Compose  
RUN groupadd -g ${DOCKER_GID:-497} docker && usermod -aG docker jenkins  
  
# Install base packages  
RUN apt-get update  
RUN apt-get install --reinstall groff-base  
RUN apt-get install -y python  
RUN curl -O https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
RUN pip install awscli  
RUN pip install boto  
  
#Copy custom build scripts  
RUN mkdir /usr/ipponscripts/  
COPY ./script /usr/ipponscripts/  
  
USER jenkins

