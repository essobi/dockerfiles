FROM ubuntu:14.04  
MAINTAINER Rodrigo Saito <rodrigo.saito@gmail.com>  
  
# Update container before continue  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Install ruby dependencies  
RUN apt-get install -y wget curl git git-core build-essential \  
libmysqlclient-dev libpq-dev \  
zlib1g-dev libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3
libxml2-dev libxslt1-dev  
  
RUN wget -q -O - http://apt.hellobits.com/hellobits.key | sudo apt-key add -  
RUN echo 'deb http://apt.hellobits.com/ trusty main' | sudo tee
/etc/apt/sources.list.d/hellobits.list  
RUN apt-get update && apt-get install -y ruby-2.1  
  
# Add options to gemrc  
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
  
# Install bundler  
RUN gem install bundler  
  

