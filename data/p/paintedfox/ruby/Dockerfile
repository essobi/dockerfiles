# Ruby (https://www.ruby-lang.org/en/)  
FROM ubuntu:precise  
MAINTAINER Ryan Seto <ryanseto@yak.net>  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list && \  
apt-get update && \  
apt-get upgrade  
  
# Ensure UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Install ruby.  
# Solution from: http://stackoverflow.com/a/16224372  
ADD http://cache.ruby-lang.org/pub/ruby/2.0/ruby-2.0.0-p353.tar.gz /tmp/  
RUN apt-get -y install build-essential zlib1g-dev libssl-dev libreadline6-dev
libyaml-dev && \  
tar -xzf /tmp/ruby-2.0.0-p353.tar.gz && \  
(cd ruby-2.0.0-p353/ && ./configure --disable-install-doc && make && make
install) && \  
rm -rf ruby-2.0.0-p353/ && \  
rm -f /tmp/ruby-2.0.0-p353.tar.gz  

