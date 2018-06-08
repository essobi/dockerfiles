FROM ruby:2.3.1  
MAINTAINER paul@trippett.org  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y build-essential locales libpq-dev
libxml2-dev libxslt1-dev libqt4-webkit libqt4-dev xvfb nodejs jq python2.7
groff  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && python2.7 get-pip.py &&
pip install awscli  
RUN locale-gen en_US.UTF-8  

