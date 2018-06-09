FROM ruby:2.5.1-alpine  
RUN apk add --no-cache \  
build-base \  
libxml2-dev \  
libxslt-dev  
RUN mkdir /app  
WORKDIR /app  
COPY Gemfile /app/Gemfile  
COPY Gemfile /app/Gemfile.lock  
RUN bundle install  
COPY . /app  

