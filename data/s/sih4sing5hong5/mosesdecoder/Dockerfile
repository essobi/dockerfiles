FROM ubuntu:16.04  
MAINTAINER sih4sing5hong5  
  
RUN apt-get update -qq && \  
apt-get install -y locales \  
g++ \  
libxslt1-dev git subversion automake libtool zlib1g-dev libboost-all-dev
libbz2-dev liblzma-dev libgoogle-perftools-dev libxmlrpc-c++.*-dev make \  
csh libc6-dev-i386 linux-libc-dev gcc-multilib  
  
  
RUN locale-gen zh_TW.UTF-8  
ENV LANG zh_TW.UTF-8  
ENV LC_ALL zh_TW.UTF-8  
RUN mkdir /usr/local/mosesserver  
WORKDIR /usr/local/mosesserver  
COPY . .  
  
RUN ./bjam -j 2  
  

