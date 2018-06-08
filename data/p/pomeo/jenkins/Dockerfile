## -*- docker-image-name: "jenkins" -*-  
FROM jenkins/jenkins:lts  
MAINTAINER Sergey Ovechkin <me@pomeo.me>  
USER root  
  
# Install packages  
RUN ln -snf /bin/bash /bin/sh  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y \  
git-core \  
curl \  
build-essential \  
libssl-dev \  
pkg-config \  
libexpat1-dev \  
libicu-dev \  
libcairo2-dev \  
libkrb5-dev \  
libjpeg62-turbo-dev \  
libgif-dev \  
libpango1.0-dev \  
g++  
  
USER jenkins  

