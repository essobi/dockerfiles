FROM ruby:2.3  
RUN mkdir /points_ms  
WORKDIR /points_ms  
  
ADD Gemfile /points_ms/Gemfile  
ADD Gemfile.lock /points_ms/Gemfile.lock  
  
RUN bundle install  
ADD . /points_ms  
  
EXPOSE 3301  

