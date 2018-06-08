FROM ruby:2.4.2  
MAINTAINER Kazuhisa Yamamoto <ak.hisashi@gmail.com>  
RUN mkdir /work  
WORKDIR /work  
COPY Gemfile .  
COPY Gemfile.lock .  
COPY pullreq.rb .  
RUN bundle install  
CMD bundle exec ruby pullreq.rb

