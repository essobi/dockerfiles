FROM ubuntu:trusty  
MAINTAINER Randall Smith <perlstalker@gmail.com>  
  
RUN apt-get update  
  
RUN apt-get install -y git ruby ruby-dev gems rbenv ruby-redcloth build-
essential python-pygments nodejs  
  
WORKDIR /usr/local/src  
RUN git clone https://github.com/PerlStalker/perlstalker.vuser.org.git
perlstalker.vuser.org  
WORKDIR perlstalker.vuser.org  
RUN gem install bundler  
RUN rbenv rehash  
#RUN gem install RedCloth -v '4.2.9'  
RUN bundle install  
  
ENTRYPOINT git pull && rake generate && rake deploy  
#ENTRYPOINT /bin/bash

