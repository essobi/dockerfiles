FROM ruby:2.4.0  
# basic for rails  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs  
  
# install phantomjs  
ADD install_phantomjs.sh /install_phantomjs.sh  
RUN /bin/bash install_phantomjs.sh  
  
RUN mkdir /certificate_authority  
WORKDIR /certificate_authority  
ADD Gemfile /certificate_authority/Gemfile  
ADD Gemfile.lock /certificate_authority/Gemfile.lock  
RUN bundle install  
ADD . /certificate_authority  

