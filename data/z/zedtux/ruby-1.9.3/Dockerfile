FROM ubuntu:14.04  
  
MAINTAINER Guillaume Hain, zedtux@zedroot.org  
  
ENV PATH /usr/local/rvm/bin:$PATH  
RUN apt-get update && apt-get -y upgrade && apt-get -y install ruby 1.9.3  
RUN ln -sf /usr/bin/ruby1.9.3 /etc/alternatives/ruby  

