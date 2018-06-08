FROM node:10.1.0  
MAINTAINER Anthony Smith <anthony@sticksnleaves.com>  
  
ENV APP_HOME /usr/src/app  
  
RUN curl -L https://api.github.com/repos/npm/npm/tarball/latest -o npm.tar.gz  
RUN tar xzf npm.tar.gz  
RUN npm-npm-*/scripts/install.sh  
RUN rm -f npm.tar.gz  
RUN rm -rf npm-npm-*/  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
  
RUN apt-get update && \  
apt-get install apt-transport-https  
  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update && \  
apt-get install yarn  
  
RUN apt-get clean  
  
WORKDIR $APP_HOME  

