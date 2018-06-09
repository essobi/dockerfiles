FROM ruby:2.3  
RUN mkdir /transactions_ms  
WORKDIR /transactions_ms  
  
ADD Gemfile /transactions_ms/Gemfile  
ADD Gemfile.lock /transactions_ms/Gemfile.lock  
  
RUN bundle install  
ADD . /transactions_ms  

