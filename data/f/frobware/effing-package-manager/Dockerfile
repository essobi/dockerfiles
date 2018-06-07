FROM debian:jessie  
MAINTAINER Andrew McDermott <aim@frobware.com>  
  
RUN apt-get -qq update && apt-get -y install eatmydata  
  
RUN eatmydata apt-get -qq update && \  
eatmydata apt-get -y install file ruby-dev rubygems build-essential && \  
/usr/bin/gem install --verbose fpm  

