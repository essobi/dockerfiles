FROM hmtreasury/base  
MAINTAINER HM Treasury Guidance Guarantee Programme <pensions-guidance-
members@digital.cabinet-office.gov.uk>  
  
ENV RUBY_VERSION 2.2.1  
ENV RUBY_BUILD_DEPENDENCIES build-essential curl libffi-dev libgdbm-dev
libreadline6-dev libssl-dev libyaml-dev  
  
RUN apt-get update -q && \  
apt-get install -qy $RUBY_BUILD_DEPENDENCIES \--no-install-recommends && \  
  
curl -o /ruby-$RUBY_VERSION/src.tar.bz2 \--create-dirs http://cache.ruby-
lang.org/pub/ruby/ruby-$RUBY_VERSION.tar.bz2 && \  
cd /ruby-$RUBY_VERSION && tar xjf src.tar.bz2 \--strip-components=1 && \  
./configure \--prefix=/usr \--sysconfdir=/etc \--disable-install-doc
\--without-tk \--without-win32 \--without-win32ole \--without-X11 && \  
make && make install && cd / && \  
rm -fr /ruby-$RUBY_VERSION && \  
  
apt-get remove -y $RUBY_BUILD_DEPENDENCIES && \  
cd /var/lib/apt/lists && rm -fr *Release* *Sources* *Packages* && \  
truncate -s 0 /var/log/*log  
  
RUN gem update -q \--system  

