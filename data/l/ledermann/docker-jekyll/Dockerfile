# Build with Ruby  
FROM ruby:2.5-alpine AS Builder  
RUN apk add --update --no-cache \  
build-base  
WORKDIR /project  
COPY Gemfile* /project/  
RUN bundle install  
COPY . /project  
RUN bundle exec jekyll build  
  
# Deploy with Nginx  
FROM nginx:stable-alpine  
LABEL maintainer="mail@georg-ledermann.de"  
COPY _nginx.conf /etc/nginx/conf.d/default.conf  
COPY \--from=Builder /project/_site /usr/share/nginx/html  

