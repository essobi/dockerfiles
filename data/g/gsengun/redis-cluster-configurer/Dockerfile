# This tag use ubuntu 14.04  
FROM phusion/baseimage:0.9.16  
MAINTAINER Gökhan Şengün <gokhansengun@gmail.com>  
  
# Some Environment Variables  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
# # Ensure UTF-8 lang and locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Initial update and install of dependency that can add apt-repos  
RUN apt-get -y update && apt-get install -y software-properties-common python-
software-properties  
  
# Add global apt repos  
RUN add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu precise
universe" && \  
add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu precise main
restricted universe multiverse" && \  
add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu precise-updates
main restricted universe multiverse" && \  
add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu precise-backports
main restricted universe multiverse"  
RUN apt-get update && apt-get -y upgrade  
  
# Install system dependencies  
RUN apt-get install -y gcc make g++ build-essential libc6-dev tcl git
supervisor ruby  
  
# Must be installed seperate from ruby or it will complain about broken
package  
RUN apt-get install -y rubygems  
  
# Install ruby dependencies so we can bootstrap the cluster via redis-trib.rb  
RUN gem install redis -v 3.3.3  
  
# checkout the 3.0.6 tag (Will change to 3.2 tag when it is released as
stable)  
RUN git clone -b 3.0.6 https://github.com/antirez/redis.git  
  
# Build redis from source  
RUN (cd /redis && make)  
  

