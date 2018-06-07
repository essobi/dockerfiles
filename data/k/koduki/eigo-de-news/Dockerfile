FROM ruby:2.2.2  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev
postgresql-client  
  
RUN mkdir /app  
  
WORKDIR /tmp  
COPY Gemfile Gemfile  
RUN bundle install  
  
ADD . /app  
WORKDIR /app  

