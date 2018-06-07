FROM ubuntu:10.04  
MAINTAINER Alan Grosskurth <code@alan.grosskurth.ca>  
  
ADD . /tmp  
  
RUN \  
apt-get update && \  
env DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y && \  
apt-get install -y build-essential debootstrap git-core && \  
/tmp/bin/cedar.sh  

