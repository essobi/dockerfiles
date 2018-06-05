FROM ubuntu:16.04  
MAINTAINER Marc Wickenden <marc@4armed.com>  
  
# Update package repo  
RUN apt-get -yqq update && apt-get install -yqq autoconf \  
build-essential \  
libreadline-dev \  
libpq-dev \  
libssl-dev \  
libxml2-dev \  
libyaml-dev \  
libffi-dev \  
zlib1g-dev \  
git-core \  
curl \  
nodejs \  
npm \  
libcurl4-openssl-dev \  
bison \  
ruby  
  
ENV RUBY_MAJOR 2.4  
ENV RUBY_VERSION 2.4.1  
ENV RUBY_SHA256
a330e10d5cb5e53b3a0078326c5731888bb55e32c4abfeb27d9e7f8e5d000250  
  
RUN mkdir -p /usr/src/ruby  
RUN cd /usr/src/ruby && \  
curl -OSL "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz" && \  
$(test "$(sha256sum ruby-${RUBY_VERSION}.tar.gz |cut -d' ' -f1)" =
"${RUBY_SHA256}" || \  
$(>&2 echo "[\\!] Checksum error"; exit 1)) && \  
tar xzf ruby-${RUBY_VERSION}.tar.gz --strip-components=1 && \  
rm ruby-${RUBY_VERSION}.tar.gz && \  
autoconf && ./configure --disable-install-doc && make -j"$(nproc)" && \  
apt-get purge -y --auto-remove bison \  
ruby && \  
make install && \  
rm -rf /usr/src/ruby && \  
rm -rf /var/lib/apt/lists/*  
RUN gem install bundler  

