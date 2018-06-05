FROM golang:latest  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
autoconf \  
automake \  
bison \  
build-essential \  
bzip2 \  
file \  
g++ \  
gcc \  
imagemagick \  
libbz2-dev \  
libc6-dev \  
libcurl4-openssl-dev \  
libevent-dev \  
libffi-dev \  
libgeoip-dev \  
libglib2.0-dev \  
libjpeg-dev \  
libgdbm-dev \  
liblzma-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libmysqlclient-dev \  
libncurses-dev \  
libpng-dev \  
libpq-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libtool \  
libwebp-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
make \  
patch \  
ruby \  
vim \  
xz-utils \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# [ruby] Skip installing gem documentation  
RUN echo 'install: --no-document\nupdate: --no-document' >> "$HOME/.gemrc"  
  
ENV RUBY_MAJOR 2.3  
ENV RUBY_VERSION 2.3.1  
ENV RUBY_DOWNLOAD_SHA256
b87c738cb2032bf4920fef8e3864dc5cf8eae9d89d8d523ce0236945c5797dcd  
ENV RUBYGEMS_VERSION 2.6.4  
# [ruby] Some of ruby's build scripts are written in ruby  
# We purge this later to make sure our final image uses what we just  
# built.  
RUN mkdir -p /usr/src/ruby \  
&& curl -fSL -o ruby.tar.gz "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz" \  
&& echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.gz" | sha256sum -c - \  
&& tar -xzf ruby.tar.gz -C /usr/src/ruby --strip-components=1 \  
&& rm ruby.tar.gz \  
&& cd /usr/src/ruby \  
&& autoconf \  
&& ./configure --disable-install-doc \  
&& make -j"$(nproc)" \  
&& make install \  
&& apt-get purge -y --auto-remove bison libgdbm-dev ruby \  
&& gem update --system $RUBYGEMS_VERSION \  
&& rm -r /usr/src/ruby  
  
# [ruby] Install gems globally.  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
  
# [ruby] Install bundler.  
ENV BUNDLER_VERSION 1.11.2  
RUN gem install bundler --version "$BUNDLER_VERSION" \  
&& bundle config --global path "$GEM_HOME" \  
&& bundle config --global bin "$GEM_HOME/bin"  
# [ruby] Don't create ".bundle" in all our apps.  
ENV BUNDLE_APP_CONFIG $GEM_HOME  

