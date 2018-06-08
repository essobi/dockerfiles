FROM debian:latest  
  
MAINTAINER Thom May <thom@scaleworks.io>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update && apt-get install -qy build-essential libffi-dev
libgdbm-dev libncurses5-dev libreadline-dev libssl-dev libyaml-dev zlib1g-dev
curl libyaml-0-2 libxml2-dev libxslt-dev  
  
RUN mkdir -p /srv && useradd -d /srv -m -s /bin/bash ruby && chown -R ruby
/srv  
RUN mkdir -p /usr/local/src  
WORKDIR /usr/local/src  
  
# Build latest ruby version, and install it in /usr/local  
RUN curl -O http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.5.tar.bz2 \  
&& tar xjf ruby-2.1.5.tar.bz2 \  
&& cd ruby-2.1.5 \  
&& ./configure --prefix=/usr/local \  
&& make && make install \  
&& /usr/local/bin/gem install --no-rdoc --no-ri bundler nokogiri puma \  
&& rm -r /usr/local/src && chown -R ruby: /usr/local  
  
USER ruby  

