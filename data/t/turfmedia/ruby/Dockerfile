FROM ubuntu:latest  
MAINTAINER Stéphane Busso <stephane.busso@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# skip installing gem documentation  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document --no-ri'; \  
echo 'update: --no-document --no-ri'; \  
} >> /usr/local/etc/gemrc  
  
ENV RUBY_MAJOR 2.3  
ENV RUBY_VERSION 2.3.1  
ENV RUBY_DOWNLOAD_SHA256
b87c738cb2032bf4920fef8e3864dc5cf8eae9d89d8d523ce0236945c5797dcd  
ENV RUBYGEMS_VERSION 2.6.4  
# some of ruby's build scripts are written in ruby  
# we purge this later to make sure our final image uses what we just built  
RUN set -ex \  
&& buildDeps=' \  
bison \  
libgdbm-dev \  
ruby \  
autoconf \  
build-essential \  
zlib1g-dev \  
libssl-dev \  
' \  
&& sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list \  
&& apt-get update && apt-get install -y --no-install-recommends $buildDeps
curl git \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -fSL -o ruby.tar.gz "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz" \  
&& echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.gz" | sha256sum -c - \  
&& mkdir -p /usr/src/ruby \  
&& tar -xzf ruby.tar.gz -C /usr/src/ruby --strip-components=1 \  
&& rm ruby.tar.gz \  
&& cd /usr/src/ruby \  
&& { echo '#define ENABLE_PATH_CHECK 0'; echo; cat file.c; } > file.c.new &&
mv file.c.new file.c \  
&& autoconf \  
&& ./configure --disable-install-doc \  
&& make -j"$(nproc)" \  
&& make install \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& gem update --system $RUBYGEMS_VERSION \  
&& rm -r /usr/src/ruby  
  
ENV BUNDLER_VERSION 1.11.2  
RUN gem install bundler --version "$BUNDLER_VERSION"  
  
ENV GEM_HOME /bundle  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME" \  
BUNDLE_JOBS=2  
ENV PATH $BUNDLE_BIN:$PATH  
  
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \  
&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN"  
  
CMD [ "irb" ]

