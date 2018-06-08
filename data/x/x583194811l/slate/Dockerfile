FROM ruby:latest  
  
MAINTAINER "LANG XIONG <x583194811l@gmail.com>"  
COPY sources.list /etc/apt/  
  
VOLUME /usr/src/myapp  
  
EXPOSE 4567  
RUN apt-get update  
RUN apt-get install -y \  
pkg-config \  
build-essential \  
nodejs \  
git \  
libxml2-dev \  
libxslt-dev  
  
RUN apt-get autoremove -yq  
  
WORKDIR /usr/src/myapp  
  
COPY Gemfile /usr/src/myapp/  
COPY Gemfile.lock /usr/src/myapp/  
  
RUN cd /usr/src/myapp && bundle install  
  

