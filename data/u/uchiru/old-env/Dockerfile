FROM ubuntu:trusty  
  
ENV RUBY_MAJOR 2.1  
ENV RUBY_VERSION 2.1.5  
RUN apt-get update && apt-get install -y bison dpkg-dev libgdbm-dev ruby wget  
RUN apt-get install -y build-essential automake zlib1g-dev libssl-dev  
RUN wget -O ruby.tar.xz "https://cache.ruby-
lang.org/pub/ruby/${RUBY_MAJOR%-rc}/ruby-$RUBY_VERSION.tar.xz" \  
&& mkdir -p /usr/src/ruby \  
&& tar -xJf ruby.tar.xz -C /usr/src/ruby --strip-components=1 \  
&& rm ruby.tar.xz \  
&& cd /usr/src/ruby \  
&& autoconf \  
&& ./configure \  
\--disable-install-doc \  
\--enable-shared \  
&& make -j "$(nproc)" \  
&& make install \  
&& cd / \  
&& rm -r /usr/src/ruby  
RUN gem install bundler  
  
ENV GEM_HOME /usr/local/bundle  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH $BUNDLE_BIN:$PATH  
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \  
&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN"  
  
RUN apt-get install -y curl libpq-dev  
ENV NODE_VERSION 6.9.1  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
RUN localedef -i en_US -f UTF-8 en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN mkdir -p /app  
WORKDIR /app  
  
RUN apt-get install -y libjpeg8 libfontconfig1 libxrender1  
COPY Gemfile /app/  
COPY Gemfile.lock /app/  
RUN bundle install  

