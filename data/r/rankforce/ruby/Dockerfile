FROM ruby:2.3-alpine  
MAINTAINER Ryuichi Tanaka <mapserver2007@gmail.com>  
  
RUN apk add --update git build-base \  
&& rm -rf /var/cache/apk/*  
  
RUN gem install bundler && \  
gem install rspec  
  
RUN git clone https://github.com/rankforce/rankforce-core.git rankforce && \  
cd rankforce && \  
bundle install  
  
WORKDIR /rankforce  

