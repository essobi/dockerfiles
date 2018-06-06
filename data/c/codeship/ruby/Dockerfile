FROM debian:jessie  
  
MAINTAINER dev@codeship.com  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential \  
curl \  
libffi-dev \  
libgdbm-dev \  
libncurses-dev \  
libreadline6-dev \  
libssl-dev \  
libyaml-dev \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV RUBY_MAJOR 2.3  
ENV RUBY_VERSION 2.3.1  
RUN echo 'install: --no-doc --no-ri\nupdate: --no-doc --no-ri' >>
"$HOME/.gemrc"  
  
RUN mkdir -p /tmp/ruby && \  
cd /tmp/ruby && \  
curl -L "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.bz2" | \  
tar -xjC /tmp/ruby --strip-components=1 && \  
./configure --disable-install-doc && \  
nice make -j && \  
make install && \  
gem update --system && \  
rm -r /tmp/ruby  
  
RUN gem install bundler  
  

