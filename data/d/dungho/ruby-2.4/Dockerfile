# Get base ubuntu  
FROM ubuntu:16.04  
ENV RUBY_MAJOR 2.4  
ENV RUBY_VERSION 2.4.0  
ENV RUBYGEMS_VERSION 2.6.10  
ENV BUNDLER_VERSION 1.14.2  
# skip installing gem documentation  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc  
  
# Install some dependencies for Ruby.  
RUN apt-get update -qq && apt-get install -y --no-install-recommends \  
ruby \  
build-essential \  
wget \  
zlib1g-dev \  
libssl-dev \  
autoconf \  
libyaml-dev \  
libffi-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Ruby  
RUN wget -O ruby.tar.gz "https://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz" \  
&& mkdir -p /usr/src/ruby \  
&& tar -xzvf ruby.tar.gz -C /usr/src/ruby --strip-components=1 \  
&& rm ruby.tar.gz \  
&& cd /usr/src/ruby \  
&& autoconf \  
&& ./configure --disable-install-doc --enable-shared \  
&& make \  
&& make install \  
&& cd / \  
&& rm -r /usr/src/ruby \  
&& gem update --system "$RUBYGEMS_VERSION"  
  
RUN gem install bundler --version "$BUNDLER_VERSION"  
  
CMD ["irb"]

