# Production Dockerfile to automate with dockerhub  
FROM ruby:2.4.1  
MAINTAINER Guillermo Guerrero 'guillermo.guerrero@fr.fcm.travel'  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update -qq && apt-get install -y build-essential postgresql-client
yarn nodejs  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

