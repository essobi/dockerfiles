FROM ruby:2.2.0  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs  
RUN mkdir /palladium  
WORKDIR /palladium  
ADD Gemfile /palladium/Gemfile  
ADD Gemfile.lock /palladium/Gemfile.lock  
RUN bundle install  
ADD . /palladium  
  

