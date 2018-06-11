FROM ruby:2-onbuild  
MAINTAINER Steven Jack <steve.jack01.ext@bbc.co.uk>  
  
ADD .rubocop.yml /root/.rubocop.yml  
  
WORKDIR /app  
  
ENTRYPOINT ["rubocop"]  

