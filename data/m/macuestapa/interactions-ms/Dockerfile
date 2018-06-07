FROM ruby:2.3  
RUN mkdir /interactions-ms  
WORKDIR /interactions-ms  
  
ADD Gemfile /interactions-ms/Gemfile  
ADD Gemfile.lock /interactions-ms/Gemfile.lock  
  
RUN bundle install  
ADD . /interactions-ms  

