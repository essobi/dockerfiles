# DOCKER-VERSION 0.4.8  
FROM ubuntu:12.04  
MAINTAINER Greg Edwards "https://twitter.com/greglearns"  
RUN apt-get -y update  
RUN apt-get -y install python-software-properties  
RUN apt-get -y install build-essential  
RUN apt-get install -y -q git  
RUN apt-get install -y curl  
RUN apt-get install -y libxml2-dev libxslt-dev libcurl4-openssl-dev  
  
# ruby-build  
ENV RUBY_ROOT /usr/local  
ENV RUBY_VERSION 2.0.0-p247  
  
RUN mkdir /src && cd /src && git clone https://github.com/sstephenson/ruby-
build.git && cd ruby-build && ./install.sh && rm -rf /src/ruby-build  
RUN ruby-build $RUBY_VERSION $RUBY_ROOT  
  
ENV RUBYGEMS_VERSION rubygems-2.0.4  
RUN cd /src && curl
http://production.cf.rubygems.org/rubygems/$RUBYGEMS_VERSION.tgz | tar -xzf -
&& cd $RUBYGEMS_VERSION && ruby setup.rb && rm -rf /src/$RUBYGEMS_VERSION  
  
RUN gem install bundler  
RUN gem install json  
RUN gem install rest-cilent  
RUN gem install httparty  

