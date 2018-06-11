FROM ruby:2.3.1-alpine  
MAINTAINER Tristan Holl  
  
RUN apk --update add --virtual build-dependencies \  
build-base \  
libxml2-dev \  
libxslt-dev \  
postgresql-dev \  
nodejs \  
tzdata \  
git \  
&& rm -rf /var/cache/apk/*  
  
RUN gem update bundler  
  
RUN mkdir /app  
WORKDIR /app  

