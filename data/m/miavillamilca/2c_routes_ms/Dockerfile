FROM ruby:2.3  
RUN mkdir /routes-ms  
WORKDIR /routes-ms  
  
ADD Gemfile /routes-ms/Gemfile  
ADD Gemfile.lock /routes-ms/Gemfile.lock  
  
RUN bundle install  
ADD . /routes-ms  
  
EXPOSE 6001  

