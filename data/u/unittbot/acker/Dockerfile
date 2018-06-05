# VERSION 0.5  
# DOCKER-VERSION 1.2.0  
# AUTHOR: Milo de Vries <milo@xdh.nl  
# DESCRIPTION: Ruby+Packer+AWS tools to macke some clouds  
# this is 2.2, alternatively downgrade with :2.1-slim  
FROM ruby:slim  
  
RUN apt-get update && apt-get -y install --no-install-recommends \  
ansible \  
awscli \  
build-essential \  
cmake \  
colordiff \  
curl \  
git \  
jq \  
pkg-config \  
ssh-client \  
unzip \  
wget \  
&& rm -rf /var/lib/apt/lists/* && apt-get clean all && wget -qO-
https://get.docker.com/ | sh  
  
# Since ruby:slim is really slim, we could consider fat  
# FROM ruby  
# Install sloww gems  
# COPY ./gems.sh /  
# RUN /gems.sh  

