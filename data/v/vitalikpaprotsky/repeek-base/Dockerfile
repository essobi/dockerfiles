FROM ruby:2.4.1  
  
RUN apt-get update -qq && apt-get install -y build-essential  
  
# for nokogiri  
RUN apt-get install -y libxml2-dev libxslt1-dev  
  
# for a JS runtime  
RUN apt-get install -y nodejs  
  
RUN mkdir /usr/src/app  
WORKDIR /usr/src/app  
  

