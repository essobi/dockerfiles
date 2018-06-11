FROM centos:7  
MAINTAINER Mateus Cruz <makteus@gmail.com>  
  
ENV BUNDLER_VERSION=1.16.1  
ENV
PG_DOWNLOAD_SHA256=cdebdeeae50744f3b7e4823b55decfbf727fb4c16bb736488984007d7b1a4f76  
ENV RUBY_CONFIGURE_OPTS=--disable-install-doc  
  
# nodejs dependency  
RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | bash - \  
&& yum -y install nodejs  
# rbenv dependencies  
RUN yum install -y git-core zlib zlib-devel gcc-c++ patch readline readline-
devel libyaml-devel libffi-devel openssl-devel make bzip2 autoconf automake
libtool bison curl sqlite-devel  
RUN yum -y install wget  
# install postgresql  
RUN cd /tmp \  
&& wget -O postgresql.tar.gz
https://ftp.postgresql.org/pub/source/v10.1/postgresql-10.1.tar.gz \  
&& echo "$PG_DOWNLOAD_SHA256 /tmp/postgresql.tar.gz" | sha256sum -c - \  
&& mkdir -p /tmp/postgresql \  
&& tar -xzf /tmp/postgresql.tar.gz -C /tmp/postgresql --strip-components=1 \  
&& cd /tmp/postgresql \  
&& echo "Building postgresql ..." \  
&& CFLAGS="-O3 -pipe" ./configure --prefix=/usr/local 1>/dev/null \  
&& make -j"$(getconf _NPROCESSORS_ONLN)" install 1>/dev/null 2>/dev/null  
# ruby 2.4.0  
RUN cd /usr/local/src \  
&& wget https://cache.ruby-lang.org/pub/ruby/2.4/ruby-2.4.0.tar.gz \  
&& tar zxf ruby-2.4.0.tar.gz \  
&& cd ruby-2.4.0 \  
&& ./configure \  
&& make \  
&& make install -j"$(getconf _NPROCESSORS_ONLN)"  
  
RUN cd /usr/local/src \  
&& wget https://rubygems.org/rubygems/rubygems-2.7.4.tgz \  
&& tar zxf rubygems-2.7.4.tgz \  
&& cd rubygems-2.7.4 \  
&& /usr/local/bin/ruby setup.rb  
  
# clean tmp files and yum cache  
RUN yum clean all  
  

