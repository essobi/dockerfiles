FROM ubuntu:14.04  
MAINTAINER Michal Martinek <martinek8@gmail.com>  
RUN echo 'gem: --no-document' > /usr/local/etc/gemrc  
  
ENV RUBY_MAJOR_MINOR_VERSION 2.2  
ENV RUBY_VERSION 2.2.0  
ENV RUBY_TARBALL_MD5 d03cd4690fec1fff81d096d1c1255fde  
ENV GEM_HOME /usr/local/lib/ruby/gems/${RUBY_MAJOR_MINOR_VERSION}.0  
RUN apt-get -qq update && \  
DEBIAN_FRONTEND=noninteractive apt-get -qy --no-install-recommends install \  
build-essential \  
ca-certificates \  
curl \  
libffi-dev \  
libreadline6-dev \  
libssl-dev \  
libyaml-dev \  
zlib1g-dev && \  
curl -s -O http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR_MINOR_VERSION/ruby-$RUBY_VERSION.tar.bz2 && \  
[ $(md5sum ruby-$RUBY_VERSION.tar.bz2 | awk '{ print $1 }') =
$RUBY_TARBALL_MD5 ] && \  
tar -jxf ruby-$RUBY_VERSION.tar.bz2 && \  
cd ruby-$RUBY_VERSION && \  
./configure --disable-install-doc && \  
make -j$(nproc) && \  
make install && \  
gem update --system && \  
cd .. && \  
rm -rf ruby-$RUBY_VERSION ruby-$RUBY_VERSION.tar.bz2 /tmp/* /var/tmp/* && \  
apt-get -qy clean autoclean autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  

