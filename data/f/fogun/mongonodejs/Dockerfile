# Pull base image  
FROM ubuntu:14.04  
MAINTAINER fogun  
  
# Install Python  
RUN \  
apt-get update && \  
apt-get install -y software-properties-common python-software-properties
python python-dev python-pip python-virtualenv && \  
rm -rf /var/lib/apt/lists/*  
  
# Install SSH server so we can connect multiple times to the container  
RUN \  
apt-get update && \  
apt-get -y install openssh-server && \  
mkdir -p /var/run/sshd /var/run/sshd  
  
# Install JDK 7 (latest edition)  
RUN apt-get install -y openjdk-7-jdk  
  
# Install nodejs and npm  
RUN apt-get install -y curl && \  
curl -sL https://deb.nodesource.com/setup | bash - && \  
apt-get install -y nodejs && \  
npm install npm@1.4.28 -g && \  
npm install -g grunt-cli && \  
apt-get install -y build-essential  
  
# Install git  
RUN apt-get install -q -y git git-core  
  
# Install MongoDB.  
RUN \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen'
> /etc/apt/sources.list.d/mongodb.list && \  
apt-get update && \  
apt-get install -y mongodb-org && \  
rm -rf /var/lib/apt/lists/*  
  
# Define mountable directories.  
VOLUME ["/data/db"]  
  
# Define working directory.  
WORKDIR /data  
  
# Expose ports  
# - 27017: process  
# - 28017: http  
EXPOSE 27017 28017  
CMD ["/bin/bash"]  

