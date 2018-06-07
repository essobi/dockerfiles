FROM ubuntu:16.04  
MAINTAINER farseer810 "https://github.com/farseer810/ubuntu-ali"  
  
# set aliyun source list as default  
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted
universe multiverse\n" > /etc/apt/sources.list && \  
echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted
universe multiverse\n" >> /etc/apt/sources.list && \  
echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted
universe multiverse\n" >> /etc/apt/sources.list && \  
echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted
universe multiverse\n" >> /etc/apt/sources.list && \  
echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted
universe multiverse\n" >> /etc/apt/sources.list && \  
echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted
universe multiverse\n" >> /etc/apt/sources.list && \  
echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main
restricted universe multiverse\n" >> /etc/apt/sources.list && \  
echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted
universe multiverse\n" >> /etc/apt/sources.list && \  
echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main
restricted universe multiverse\n" >> /etc/apt/sources.list && \  
echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial-proposed main
restricted universe multiverse\n" >> /etc/apt/sources.list && \  
echo "deb http://archive.canonical.com/ubuntu/ xenial partner\n" >>
/etc/apt/sources.list && \  
apt-get update  
  
# disable dialog frontend during installation  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C  
  
# install some basic software  
RUN apt-get install -y apt-utils build-essential vim git wget  
  

