FROM ruby:2.4-alpine  
  
RUN apk update && apk add build-base nodejs postgresql-dev  
  
RUN mkdir /app  
WORKDIR /app  
  
COPY Gemfile Gemfile.lock ./  
RUN bundle config mirror.https://rubygems.org https://gems.ruby-china.org \  
&& bundle install  
  
COPY . .  
  
LABEL maintainer="Bin Li <holysoros@gmail.com>"  
  
CMD puma -C config/puma.rb  

