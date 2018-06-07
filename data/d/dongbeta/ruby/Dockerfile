FROM ubuntu:14.04  
MAINTAINER Yaodong Zhao <dongbeta@gmail.com>  
  
RUN apt-get update -yqq  
RUN apt-get install -yqq build-essential wget curl git  
  
RUN cd /tmp && \  
wget -O ruby-install-0.4.3.tar.gz https://github.com/postmodern/ruby-
install/archive/v0.4.3.tar.gz && \  
tar -xzvf ruby-install-0.4.3.tar.gz && \  
cd ruby-install-0.4.3/ && \  
make install  
  
RUN ruby-install ruby 2.1.2  
ENV PATH /opt/rubies/ruby-2.1.2/bin:$PATH  
RUN echo "gem: --no-document" > ~/.gemrc  
RUN gem install bundler

