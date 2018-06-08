FROM ruby:2.5-alpine3.7  
LABEL maintainer="Thomas Schmitz", version="1.0.0"  
  
ENV RAILS_VERSION=5.1.4  
RUN apk add --no-cache --virtual .build-deps\  
build-base\  
sqlite-dev\  
nodejs\  
&& gem install rails --version "$RAILS_VERSION" \--force\  
&& gem install rubocop\  
&& mkdir /app  
  
WORKDIR /app  

