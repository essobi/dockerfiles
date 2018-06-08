FROM ubuntu:12.04  
  
MAINTAINER Zhenbo Li  
  
#To Edit PPA  
RUN apt-get update -qq  
RUN apt-get install -y python-software-properties  
  
RUN apt-get update -qq  
  
#Build Tools  
RUN apt-get install -y build-essential  
RUN apt-get install -y gcc g++  
RUN apt-get install -y autoconf automake libtool libltdl-dev  
RUN apt-get install -y cmake  
RUN apt-get install -y bison flex  
  
#Other related Tools  
RUN apt-get install -y git  
  
#Install cross-compile tools  
RUN apt-get install -y binutils-mingw-w64-i686  
RUN apt-get install -y gcc-mingw-w64-i686  
  

