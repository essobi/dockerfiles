FROM ruby:2.3  
RUN mkdir /recomendation-ms  
WORKDIR /recomendation-ms  
  
ADD Gemfile /recomendation-ms/Gemfile  
ADD Gemfile.lock /recomendation-ms/Gemfile.lock  
  
RUN bundle install  
ADD . /recomendation-ms  

