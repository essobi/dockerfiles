FROM ubuntu:14.04  
MAINTAINER ontouchstart <ontouchstart@gmail.com>  
  
RUN apt-get update -y  
RUN apt-get -y upgrade  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
RUN apt-get -y install ruby ruby-dev ruby-gsl make g++ git python nodejs  
RUN gem install bundler github-pages --no-rdoc --no-ri  
RUN github-pages versions  

