FROM ruby:2.2  
MAINTAINER Dieter Provoost <dieter.provoost@marlon.be>  
  
# Use UTF-8 (see https://oncletom.io/2015/docker-encoding/)  
ENV LANG C.UTF-8  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update && apt-get install -y \  
nodejs \  
yarn  

