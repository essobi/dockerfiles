FROM ruby:2.3.0  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev  
RUN mkdir /bojangles  
WORKDIR /bojangles  
ADD Gemfile /bojangles/Gemfile  
ADD Gemfile.lock /bojangles/Gemfile.lock  
RUN bundle install  
ADD . /bojangles  

