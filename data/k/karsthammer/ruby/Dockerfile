FROM ubuntu:14.04  
MAINTAINER Karst Hammer <karst@noxa.nl>  
  
RUN apt-get update  
  
# Install ruby dependencies  
RUN apt-get install -y wget curl \  
build-essential git git-core vim \  
zlib1g-dev libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3
libxml2-dev libxslt1-dev &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install ruby-build  
RUN git clone https://github.com/sstephenson/ruby-build.git &&\  
./ruby-build/install.sh &&\  
rm -r ./ruby-build  
  
# Install Ruby 2.1.5  
RUN ruby-build 2.1.5 /usr/local  
  
# Add options to gemrc  
RUN echo "gem: --no-document" > ~/.gemrc  
  
# Install bundler  
RUN gem install bundler

