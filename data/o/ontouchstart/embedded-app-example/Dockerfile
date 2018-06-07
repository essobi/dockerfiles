FROM ubuntu:14.04  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
RUN apt-get update  
RUN apt-get upgrade  
  
# https://gorails.com/setup/ubuntu/14.04  
RUN apt-get install -y git-core curl zlib1g-dev build-essential libssl-dev
libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev
libcurl4-openssl-dev python-software-properties libpq-dev  
ADD . /src  
RUN tar -xzvf /src/ruby-1.9.3-p551.tar.gz  
RUN cd ruby-1.9.3-p551/ && ./configure && make install  
RUN ruby -v  
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
RUN gem install bundle  
RUN cd /src && bundle install  
  

