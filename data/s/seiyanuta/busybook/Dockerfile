FROM ruby:2.4.0  
MAINTAINER Seiya Nuta <nuta@seiya.me>  
  
ADD Gemfile /app/Gemfile  
ADD Gemfile.lock /app/Gemfile.lock  
WORKDIR /app  
  
ADD . /app  
ADD config/database.yml /app/config/database.yml  
WORKDIR /app  
  
ENV RAILS_ENV production  
ENV PORT 8080  
RUN bundle install --jobs 2  
CMD bundle exec puma  

