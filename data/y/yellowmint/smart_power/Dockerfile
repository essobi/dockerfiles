FROM ruby:2.4.1  
RUN apt-get update -qq  
RUN apt-get install -y build-essential libpq-dev nodejs webp  
  
RUN mkdir /smart_power  
WORKDIR /smart_power  
  
ADD . /smart_power  
  
RUN bundle install  

