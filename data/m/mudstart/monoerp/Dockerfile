FROM ruby:2.3.1  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs  
  
RUN mkdir /railsapp  
WORKDIR /railsapp  
  
ADD Gemfile /railsapp/Gemfile  
ADD Gemfile.lock /railsapp/Gemfile.lock  
  
RUN bundle install  
  
ADD . /railsapp  

