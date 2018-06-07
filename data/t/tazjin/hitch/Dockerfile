FROM centos:7  
MAINTAINER Vincent Ambo <hej@tazj.in>  
  
# Simple Dockerfile for Hitch:  
# https://github.com/varnish/hitch  
# Install build dependencies  
RUN yum groupinstall -y "Development Tools" && \  
yum install -y libev libev-devel openssl-devel  
  
# Build Hitch  
WORKDIR /tmp  
RUN curl -O https://hitch-tls.org/source/hitch-1.0.1.tar.gz && \  
tar xvf hitch-1.0.1.tar.gz && \  
cd hitch-1.0.1 && \  
./configure && make && make install  
RUN useradd -u 1000 hitch  
  
EXPOSE 8443  
ENTRYPOINT /usr/local/sbin/hitch  

