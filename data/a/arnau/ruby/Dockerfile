FROM debian:wheezy  
MAINTAINER Arnau Siches <asiches@gmail.com>  
  
ENV RUBY_MAJOR 2.1  
ENV RUBY_VERSION 2.1.5  
ENV RUBY_SRC_DIR /usr/src/ruby  
  
# Essentials  
RUN apt-get update -qqy \  
&& apt-get install -qqy \  
autoconf \  
build-essential \  
curl \  
git \  
imagemagick \  
libbz2-dev \  
libcurl4-openssl-dev \  
libevent-dev \  
libffi-dev \  
libglib2.0-dev \  
libjpeg-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libmysqlclient-dev \  
libncurses-dev \  
libpq-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
procps \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update -qqy \  
&& apt-get install -qqy locales \  
&& rm -rf /var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
  
# Ruby specifics  
RUN apt-get update -qqy \  
&& apt-get install -qqy \  
bison \  
ruby \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p $RUBY_SRC_DIR \  
&& curl -s -SL "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.bz2" \  
| tar -xjC $RUBY_SRC_DIR --strip-components=1  
  
WORKDIR $RUBY_SRC_DIR  
  
RUN autoconf \  
&& ./configure \  
\--disable-install-doc \  
&& make -j"$(nproc)" \  
&& apt-get purge -qqy --auto-remove bison ruby \  
&& make install \  
&& rm -r /usr/src/ruby  
  
CMD ["irb"]  

