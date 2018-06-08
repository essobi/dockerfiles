# Version 1.0.0  
FROM ubuntu:12.04  
MAINTAINER Mike Bartoli "michael.bartoli@pomona.edu"  
RUN apt-get update  
RUN apt-get -y install \  
build-essential \  
make \  
curl \  
zlib1g-dev \  
libssl-dev \  
libreadline6-dev \  
libyaml-dev \  
git \  
nodejs \  
python  
  
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
  
RUN gem install redcarpet  
RUN gem install jekyll  
RUN gem install execjs  

