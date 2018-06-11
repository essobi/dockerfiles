# Ruby (https://www.ruby-lang.org/en/)  
  
FROM debian:jessie  
MAINTAINER Zee Yang <zee.yang@gmail.com>  
  
RUN apt-get update -qq && apt-get install -y \  
build-essential \  
zlib1g-dev \  
libssl-dev \  
libreadline-dev \  
libyaml-dev  
  
ADD http://cache.ruby-lang.org/pub/ruby/1.9/ruby-1.9.3-p545.tar.gz
/tmp/ruby.tar.gz  
  
RUN cd /tmp \  
&& tar -xzvf ruby.tar.gz \  
&& cd $(find . -name "ruby*" -type d) \  
&& ./configure \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -fr ruby*  

