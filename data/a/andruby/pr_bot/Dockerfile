FROM ruby:2.3-alpine  
MAINTAINER andruby  
  
# Needed to build eventmachine and download gems from git  
RUN apk update && apk add --no-cache g++ musl-dev make git && rm -rf
/var/cache/apk/*  
  
RUN mkdir -p /var/www/pr_bot  
WORKDIR /var/www/pr_bot  
COPY Gemfile .  
COPY Gemfile.lock .  
RUN bundle install  
COPY app.rb .  
COPY lib/ lib/  
  
ENV BIND 0.0.0.0  
EXPOSE 4567  
CMD bundle exec ruby app.rb  

