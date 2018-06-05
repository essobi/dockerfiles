FROM ubuntu:xenial  
  
RUN apt-get -y update && \  
apt-get -y install git python-virtualenv python-dev ruby ruby-dev rubygems gcc
make && \  
gem install --no-ri \--no-rdoc fpm  

