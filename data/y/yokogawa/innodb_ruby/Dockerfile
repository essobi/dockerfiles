FROM ruby:alpine  
  
ENV INNODB_RUBY_VERSION 0.9.15  
RUN set -ex \  
&& gem install \  
innodb_ruby --version ${INNODB_RUBY_VERSION}  
  
WORKDIR /work  

