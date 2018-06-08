FROM ubuntu:14.04  
MAINTAINER ontouchstart <ontouchstart@gmail.com>  
  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
RUN apt-get -y install ruby ruby-dev make g++ git python  
RUN gem install bundler jekyll github-pages therubyracer --no-rdoc --no-ri  

