FROM node:8.0.0  
MAINTAINER Tim Tegeler <tegeler@creios.net>  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update -y && apt-get install -y openssh-client rsync yarn  

