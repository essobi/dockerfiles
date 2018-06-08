# A simple container with the Chef omnibus installed on Ubuntu 14.04  
FROM ubuntu:14.04  
MAINTAINER James Johnson  
  
RUN apt-get update && apt-get -y install openssh-server curl lsb-release  
  
RUN curl -L https://www.chef.io/chef/install.sh | sudo bash -s -- -v 12.3.0  

