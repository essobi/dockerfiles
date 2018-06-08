FROM ubuntu:14.04  
MAINTAINER Alejandro Torres <fulgorek@gmail.com>  
ENV RUBY_VERSION=2.2.2  
# Install ruby dependencies  
RUN apt-get update && apt-get install -y wget curl build-essential git git-
core \  
zlib1g-dev libssl-dev libreadline-dev libyaml-dev libsqlite3-dev \  
sqlite3 libxml2-dev libxslt1-dev  
  
# Install ruby-install  
RUN cd /tmp && \  
wget -O ruby-install-0.6.0.tar.gz https://github.com/postmodern/ruby-
install/archive/v0.6.0.tar.gz &&\  
tar -xzvf ruby-install-0.6.0.tar.gz &&\  
cd ruby-install-0.6.0/ &&\  
make install  
  
# Install MRI Ruby  
RUN ruby-install ruby $RUBY_VERSION  
  
# Add Ruby binaries to $PATH  
ENV PATH /opt/rubies/ruby-$RUBY_VERSION/bin:$PATH  
  
# Add options to gemrc  
RUN echo "gem: --no-rdoc --no-ri" > ~/.gemrc  
  
# Install bundler  
RUN gem install bundler  
  

