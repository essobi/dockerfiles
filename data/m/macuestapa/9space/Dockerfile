FROM ruby:2.3  
RUN mkdir /api-gateway  
WORKDIR /api-gateway  
  
ADD Gemfile /api-gateway/Gemfile  
ADD Gemfile.lock /api-gateway/Gemfile.lock  
  
RUN bundle install  
ADD . /api-gateway  

