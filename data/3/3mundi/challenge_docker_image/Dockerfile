# Production Dockerfile to automate with dockerhub  
FROM ruby:2.4.0  
MAINTAINER Guillermo Guerrero 'guillermo.guerrero@fr.fcm.travel'  
RUN apt-get update -qq && apt-get install -y mysql-client build-essential  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && apt-get install
-y nodejs  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install -y yarn  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

