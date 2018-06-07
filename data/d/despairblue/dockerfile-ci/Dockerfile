FROM ubuntu:16.04  
MAINTAINER Danny Arnold <despair.blue@gmail.com>  
  
RUN apt update  
RUN apt install -y apt-transport-https ca-certificates curl gnupg2 software-
properties-common  
  
# MongoDB  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5  
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu
xenial/mongodb-org/3.6 multiverse" > /etc/apt/sources.list.d/mongodb-
org-3.6.list  
RUN apt update  
RUN apt install -y mongodb-org  
  
# Yarn  
RUN apt install -y nodejs  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list  
RUN apt update && apt install -y yarn  
  
# Node  
RUN yarn global add n  
RUN n 8  
  
# Git  
RUN apt install -y git  
RUN git config --global user.email "bitbucket-ci@bitbucket.org"  
RUN git config --global user.name "Bitbucket Pipelines"  
RUN git config --global push.default simple  
  
# Docker  
RUN apt install -y docker.io  
  
# phantomjs dependency  
RUN apt install -y libfontconfig  
  
# node-gyp dependency  
RUN apt install -y python  
  
# sharp dependency  
RUN apt install -y build-essential  
  
RUN rm -rf /var/lib/apt/lists/*  

