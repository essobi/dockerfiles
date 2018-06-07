#################################################################  
# This docker image build file creates an image that contains  
# nginx, passenger, rvm with ruby on rails.  
#  
# ## .  
# ## ## ## ==  
# ## ## ## ## ===  
# /""""""""""""""""\\___/ ===  
# ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ / ===- ~~~  
# \\______ o __/  
# \ \ __/  
# \\____\\______/  
#  
# Component: RNTD  
# Author: Dou Chunrong <douchunrong@gmail.com>  
# Copyright: (c) 2015-2016 RNTD Ltd. All rights reserved.  
#################################################################  
#version 0.0.1  
FROM douchunrong/docker_ror  
  
MAINTAINER Dou Chunrong <douchunrong@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
  
RUN apt-get install -y git libcurl4-openssl-dev apt-utils  
  
RUN apt-get -y install nodejs  
  
RUN /bin/bash -l -c "rvm -v"  
  
  
# 安装 buneld & passenger  
RUN /bin/bash -l -c 'gem install bundler'  
RUN /bin/bash -l -c "gem install passenger -v 5.0.23"  
  
RUN apt-get remove nginx-common nginx-full nginx  
  
RUN /bin/bash -l -c "passenger-install-nginx-module --auto-download --auto
--prefix=/opt/nginx --languages ruby"  
  
ENV PATH=$PATH:/opt/nginx/sbin  
WORKDIR /opt/nginx/sbin  
  
  
#EXPOSE 80  
  
#CMD ["nginx","-g", "daemon off;"]  

