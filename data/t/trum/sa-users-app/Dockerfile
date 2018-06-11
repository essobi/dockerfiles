FROM ruby:2.3  
RUN mkdir /users-app  
RUN apt-get update  
RUN apt-get install libc-ares2 libv8-3.14.5 nodejs  
WORKDIR /users-app  
  
ADD Gemfile /users-app/Gemfile  
ADD Gemfile.lock /users-app/Gemfile.lock  
  
RUN bundle install  
ADD . /users-app

