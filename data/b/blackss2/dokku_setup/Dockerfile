FROM ubuntu:trusty  
MAINTAINER Lucas Park <blackss3@gmail.com>  
  
# Update ubuntu  
#RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main restricted" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get update  
  
# Install basic packages  
RUN apt-get -qq -y install git  
RUN apt-get -qq -y install curl  
RUN apt-get -qq -y install wget  
RUN apt-get -qq -y install software-properties-common  
  
# Compile libraries  
RUN apt-get -qq -y install gcc  
RUN apt-get -qq -y install make  
RUN apt-get -qq -y install ssh  
#RUN apt-get -qq -y libc6=2.19-0ubuntu6 libc6-dev  
RUN rm -rf /var/lib/apt/lists/*  
  
# Install dokku  
RUN wget https://raw.githubusercontent.com/dokku/dokku/v0.4.7/bootstrap.sh  
RUN sudo DOKKU_TAG=v0.4.7 bash bootstrap.sh  

