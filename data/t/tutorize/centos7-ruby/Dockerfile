#!/usr/bin/env bash  
# Dockerfile for centos 7 based image with ruby-2.3.4 installed.  
# Partly based on the official debian ruby image: https://github.com/docker-
library/ruby  
FROM centos:centos7.3.1611  
MAINTAINER TUTORize <developer@tutorize.com>  
  
# Ruby + version config  
ENV RUBY_MAJOR 2.3  
ENV RUBY_VERSION 2.3.4  
ENV DEFAULT_PREFIX /usr/local  
ENV BUNDLER_VERSION 1.15.3  
# Install ruby build dependencies  
# We compile with support for:  
# - openssl  
# - readline  
# But without:  
# - dbm  
# - gddm  
RUN yum update -y && \  
yum install -y gcc-c++ \  
openssl-devel \  
readline-devel \  
make && \  
yum clean all -y  
  
# Do not install documentation for gems  
RUN mkdir -p /usr/local/etc && \  
echo 'install: --no-document' >> /usr/local/etc/gemrc && \  
echo 'update: --no-document' >> /usr/local/etc/gemrc  
  
# Download ruby source  
ADD https://cache.ruby-lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz
/tmp  
RUN tar -xzf /tmp/ruby-$RUBY_VERSION.tar.gz -C /tmp  
# Build and install ruby from source  
RUN cd /tmp/ruby-$RUBY_VERSION && ./configure --prefix=$DEFAULT_PREFIX
\--disable-install-doc  
RUN cd /tmp/ruby-$RUBY_VERSION && make  
RUN cd /tmp/ruby-$RUBY_VERSION && make install  
# cleanup  
RUN rm -rf /tmp/ruby-$RUBY_VERSION  
# remove build depts for ruby  
RUN yum remove -y gcc-c++ readline-devel openssl-devel  
  
RUN gem install bundler --version "$BUNDLER_VERSION"  
  
# Gem and bundle config  
ENV GEM_HOME /usr/local/bundle  
ENV BUNDLE_PATH $GEM_HOME  
ENV BUNDLE_BIN $GEM_HOME/bin  
ENV BUNDLE_SILENCE_ROOT_WARNING 1  
ENV BUNDLE_APP_CONFIG $GEM_HOME  
ENV PATH $BUNDLE_BIN:$PATH  
  
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN"  
RUN chmod 777 "$GEM_HOME" "$BUNDLE_BIN"  
  
CMD [ "irb" ]  

