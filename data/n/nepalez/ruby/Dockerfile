# The container includes:  
#  
# * Ubuntu 14.04  
# * MRI Ruby 2.1.2  
# * Bundler  
#  
FROM ubuntu:14.04  
MAINTAINER Andrew Kozin <andrew.kozin@gmail.com>  
  
#
==============================================================================  
# Ubuntu Linux 14.04 with postgres client  
#
==============================================================================  
# Ignore APT warnings about not having a TTY  
ENV DEBIAN_FRONTEND noninteractive  
  
# Ensure UTF-8 locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
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
postgresql-client-9.3 \  
software-properties-common \  
wget \  
zlib1g-dev  
  
#
==============================================================================  
# Ruby with postgres support  
#
==============================================================================  
# Set $PATH so that non-login shells will see the Ruby binaries  
ENV PATH $PATH:/opt/rubies/ruby-2.1.2/bin  
  
# Add PostgreSQL Global Development Group apt source  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" \  
> /etc/apt/sources.list.d/pgdg.list  
  
# Add PGDG repository key  
RUN wget -qO - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc \  
| apt-key add -  
  
# Install MRI Ruby 2.1.2  
RUN curl -O http://ftp.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz && \  
tar -zxvf ruby-2.1.2.tar.gz && \  
cd ruby-2.1.2 && \  
./configure --disable-install-doc && \  
make && \  
make install && \  
cd .. && \  
rm -r ruby-2.1.2 ruby-2.1.2.tar.gz && \  
echo 'gem: --no-document' > /usr/local/etc/gemrc  
  
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
/bin/bash -l -c 'gem install bundler --no-rdoc --no-ri' && \  
echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
  
# Clean up APT and temporary files when done  
RUN apt-get clean -qq && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Define working directory  
WORKDIR /app  
  
# Set bash as a default process  
CMD ["bash"]  

