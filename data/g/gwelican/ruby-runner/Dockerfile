FROM ruby:2.3.3-alpine  
  
RUN mkdir /ambient  
WORKDIR /ambient  
COPY Gemfile /ambient/  
  
RUN apk add \--no-cache --virtual build-dependencies build-base cmake g++ gcc
&& \  
apk add \--no-cache git openssh libxml2-dev libxml2 libxslt-dev postgresql-dev
make && \  
bundle config build.nokogiri --use-system-libraries && \  
bundle install && \  
adduser -D -u 1000 rubyrunner && \  
apk del build-dependencies  

