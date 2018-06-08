FROM ruby:2.4.0  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs  
RUN mkdir /pairing  
WORKDIR /pairing  
ADD Gemfile /pairing/Gemfile  
ADD Gemfile.lock /pairing/Gemfile.lock  
RUN bundle install  
ADD . /pairing  

