# https://github.com/docker-library/ruby/blob/master/2.3/onbuild/Dockerfile  
FROM ruby:2.3-alpine  
MAINTAINER Tomohiro TAIRA <tomohiro.t@gmail.com>  
  
RUN apk add \--no-cache git build-base libxml2-dev libxslt-dev sqlite-dev  
  
# Throw errors if Gemfile has been modified since Gemfile.lock  
RUN bundle config \--global frozen 1  
  
# Bundler build configuration  
RUN bundle config \--global build.nokogiri --use-system-libraries  
RUN bundle config \--global build.sqlite3 --use-system-libraries  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY Gemfile /usr/src/app/  
ONBUILD COPY Gemfile.lock /usr/src/app/  
ONBUILD RUN bundle install  
  
ONBUILD COPY . /usr/src/app  

