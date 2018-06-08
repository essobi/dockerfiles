FROM ruby:2.4  
MAINTAINER Sida Say <sidasay@gmail.com>  
  
# setup workdir  
RUN mkdir /data  
WORKDIR /data  
  
ADD Gemfile ./Gemfile  
ADD minimal-mistakes-jekyll.gemspec ./minimal-mistakes-jekyll.gemspec  
ADD package.json ./package.json  
ADD Rakefile ./Rakefile  
  
# Install bundle  
RUN bundle install  

