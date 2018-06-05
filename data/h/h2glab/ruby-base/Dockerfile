FROM ruby:2.5.1  
MAINTAINER H2G Lab <hello@h2g.io>  
  
ENV LANG C.UTF-8  
  
RUN apt-get update -q \  
&& apt-get install -y cmake nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gem install bundler  

