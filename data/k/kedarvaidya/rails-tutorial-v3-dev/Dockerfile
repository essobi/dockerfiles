# Setup used in Rails Tutorial  
FROM ubuntu:trusty  
MAINTAINER Kedar Vaidya kedarvaidya0@gmail.com  
  
# Ensure UTF-8.  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Update system  
RUN apt-get update  
  
# Install requirements and essential packages  
RUN apt-get -y install build-essential bison openssl libreadline6
libreadline6-dev curl git-core zlib1g zlib1g-dev libssl-dev libyaml-dev
libsqlite3-0 libsqlite3-dev sqlite3 libxml2-dev libxslt-dev autoconf libc6-dev
nodejs  
  
# Installs ImageMagick for image processing  
RUN apt-get install imagemagick --fix-missing -y  
  
# Install Ruby 2.1.4  
RUN apt-get -y install wget && \  
cd /tmp && \  
wget -q http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.4.tar.gz && \  
cd / && \  
tar -xzf /tmp/ruby-2.1.4.tar.gz && \  
(cd ruby-2.1.4/ && ./configure --disable-install-doc && make && make install)
&& \  
rm -rf ruby-2.1.4/ && \  
rm -f /tmp/ruby-2.1.4.tar.gz  
  
# Setup according to Rails Tutorial  
RUN echo 'install: --no-rdoc --no-ri' >> ~/.gemrc && \  
echo 'update: --no-rdoc --no-ri' >> ~/.gemrc && \  
gem update --system 2.1.9 && \  
gem install rails -v 4.2.0.beta2

