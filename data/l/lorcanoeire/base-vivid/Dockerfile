FROM ubuntu:vivid  
MAINTAINER Lorcan O'Flynn <lorcan.oflynn@gmail.com>  
  
# Install build dependencies  
RUN apt-get update -qq && \  
apt-get install -y -qq \  
build-essential \  
ca-certificates \  
curl \  
libcurl4-openssl-dev \  
libffi-dev \  
libgdbm-dev \  
libpq-dev \  
libreadline6-dev \  
libssl-dev \  
libtool \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
software-properties-common \  
wget \  
zlib1g-dev \  
libmysqlclient-dev \  
imagemagick \  
git \  
nodejs  
  
# Set $PATH so that non-login shells will see the Ruby binaries  
ENV PATH $PATH:/opt/rubies/ruby-2.1.2/bin  
# Install MRI Ruby 2.1.2  
RUN curl -O http://ftp.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz && \  
tar -zxvf ruby-2.1.2.tar.gz && \  
cd ruby-2.1.2 && \  
./configure \--disable-install-doc && \  
make && \  
make install && \  
cd .. && \  
rm -r ruby-2.1.2 ruby-2.1.2.tar.gz && \  
echo 'gem: \--no-document' > /usr/local/etc/gemrc  
#
==============================================================================  
# Rubygems, Bundler and Foreman  
#
==============================================================================  
# Install rubygems and bundler  
ADD http://production.cf.rubygems.org/rubygems/rubygems-2.3.0.tgz /tmp/  
RUN cd /tmp && \  
tar -zxf /tmp/rubygems-2.3.0.tgz && \  
cd /tmp/rubygems-2.3.0 && \  
ruby setup.rb && \  
/bin/bash -l -c 'gem install bundler \--no-rdoc \--no-ri' && \  
echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
# Clean up APT and temporary files when done  
RUN apt-get clean -qq && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

