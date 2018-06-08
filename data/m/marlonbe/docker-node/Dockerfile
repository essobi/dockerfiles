FROM ubuntu:xenial  
MAINTAINER Marlon BVBA <info@marlon.be>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && apt-get install -y locales  
  
RUN locale-gen nl_BE.UTF-8  
ENV LC_ALL nl_BE.UTF-8  
RUN apt-get update -y  
  
RUN apt-get install -y -f curl  
  
# Installing nodejs  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash  
RUN apt-get install -y -f nodejs  
  
# Installing yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update -y  
RUN apt-get install -y -f yarn  
  
# Apache Ant  
RUN apt-get install -y ant  
  
# GIT  
RUN apt-get install -y git-core  

