#  
# ruby-install Dockerfile  
#  
# https://github.com/coderjoe/dockerfile-ruby-install  
#  
FROM ubuntu:14.04  
MAINTAINER Joseph Bauser <coderjoe@coderjoe.net>  
  
RUN apt-get update && apt-get install -y curl make build-essential  
  
ADD https://github.com/postmodern/ruby-install/archive/v0.6.0.tar.gz
/tmp/ruby-install.tar.gz  
RUN cd /tmp && \  
tar -xzvf ruby-install.tar.gz && \  
cd /tmp/ruby-install-* && \  
make install && \  
rm -rf /tmp/ruby-install*  

