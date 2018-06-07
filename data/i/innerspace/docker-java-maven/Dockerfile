# modified version of:  
# https://hub.docker.com/r/jamesdbloom/docker-java8-maven/~/dockerfile/  
FROM java:8  
  
MAINTAINER Matt MacGillivray "matthew.macgillivray@gmail.com"  
  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y vim maven  

