FROM ubuntu:14.04.1  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN locale  
  
# https://gorails.com/setup/ubuntu/14.04  
RUN apt-get install -y git-core curl zlib1g-dev build-essential libssl-dev
libffi-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev
libxslt1-dev libcurl4-openssl-dev python-software-properties bison ruby  
RUN ruby -v  
ADD ruby-1.9.3-p551 /ruby-1.9.3-p551  
RUN cd /ruby-1.9.3-p551 && ./configure && make install  
RUN apt-get purge -y ruby  
RUN ruby -v  
  
RUN gem install bundler --no-rdoc --no-ri  
RUN irb -v  
RUN gem -v  
RUN gem list  
  
ENV HOME /home  
WORKDIR /home  

