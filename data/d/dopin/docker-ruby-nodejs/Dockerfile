FROM dopin/docker-trusty-ruby:latest  
MAINTAINER dopin "dopinninja@gmail.com"  
  
# Install Node.js and npm  
RUN \  
apt-get install -y software-properties-common && \  
apt-get update && \  
add-apt-repository -y ppa:chris-lea/node.js && \  
echo "deb http://archive.ubuntu.com/ubuntu trusty universe" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y nodejs  
  

