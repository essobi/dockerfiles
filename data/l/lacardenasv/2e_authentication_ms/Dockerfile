FROM ruby:2.3  
RUN mkdir /authentication-ms  
WORKDIR /authentication-ms  
  
ADD Gemfile /authentication-ms/Gemfile  
ADD Gemfile.lock /authentication-ms/Gemfile.lock  
  
RUN bundle install  
ADD . /authentication-ms  
  
EXPOSE 4003

