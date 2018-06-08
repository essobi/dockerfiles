FROM quay.io/nordstrom/baseimage-ubuntu:16.04  
MAINTAINER Nordstrom Kubernetes Platform Team "invcldtm@nordstrom.com"  
ARG RUBY_VERSION  
ENV RUBY_VERSION $RUBY_VERSION  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C3173AA6 \  
&& echo "deb http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu xenial main" \  
> /etc/apt/sources.list.d/brightbox_ruby.list  
  
RUN apt-get update -qy \  
&& apt-get install -qy \  
ruby${RUBY_VERSION} \  
ruby${RUBY_VERSION}-dev  
  
RUN echo "gem: --no-document --no-ri" > /etc/gemrc  
RUN gem update --system \  
&& gem install bundler  

