FROM ruby:2.2.3-onbuild  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev redis-
server libgmp3-dev  
  
RUN mkdir /myapp  
WORKDIR /myapp  
  
ADD Gemfile /myapp/Gemfile  
ADD Gemfile.lock /myapp/Gemfile.lock  
  
ADD . /myapp

