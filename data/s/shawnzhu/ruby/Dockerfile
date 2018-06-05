# Ruby environment  
#  
# VERSION 0.2  
FROM ubuntu:12.04  
MAINTAINER Muriel Salvan <muriel@x-aeon.com>  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
RUN apt-get -y install build-essential zlib1g-dev libssl-dev libreadline6-dev
libyaml-dev git  
  
ADD http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.1.tar.gz /tmp/  
  
RUN cd /tmp && \  
tar -xzf ruby-2.1.1.tar.gz && \  
cd ruby-2.1.1 && \  
./configure && \  
make && \  
make install && \  
cd .. && \  
rm -rf ruby-2.1.1 && \  
rm -f ruby-2.1.1.tar.gz  
  
RUN gem install bundler --no-ri --no-rdoc  
  

