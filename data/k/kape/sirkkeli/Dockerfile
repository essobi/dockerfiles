FROM node:8.11.1  
  
RUN apt-get update -y && apt-get install -y --no-install-recommends \  
git \  
qt5-default \  
libqt5webkit5-dev \  
xvfb \  
xauth \  
default-jre \  
python-pip \  
python-dev \  
&& rm -rf /var/lib/apt/lists  
  
# manually install phantomjs  
#RUN curl -sL -o -
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
| tar -xjf - -O phantomjs-2.1.1-linux-x86_64/bin/phantomjs >
/usr/bin/phantomjs && chmod +x /usr/bin/phantomjs  
# skip installing gem documentation  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc  
  
ENV RUBY_MAJOR 2.3  
ENV RUBY_VERSION 2.3.4  
ENV RUBYGEMS_VERSION 2.6.11  
# some of ruby's build scripts are written in ruby  
# we purge system ruby later to make sure our final image uses what we just
built  
RUN set -ex \  
\  
&& buildDeps=' \  
bison \  
libgdbm-dev \  
ruby \  
' \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
\  
&& wget -O ruby.tar.xz "https://cache.ruby-
lang.org/pub/ruby/${RUBY_MAJOR%-rc}/ruby-$RUBY_VERSION.tar.xz" \  
\  
&& mkdir -p /usr/src/ruby \  
&& tar -xJf ruby.tar.xz -C /usr/src/ruby --strip-components=1 \  
&& rm ruby.tar.xz \  
\  
&& cd /usr/src/ruby \  
\  
# hack in "ENABLE_PATH_CHECK" disabling to suppress:  
# warning: Insecure world writable dir  
&& { \  
echo '#define ENABLE_PATH_CHECK 0'; \  
echo; \  
cat file.c; \  
} > file.c.new \  
&& mv file.c.new file.c \  
\  
&& autoconf \  
&& ./configure --disable-install-doc --enable-shared \  
&& make -j"$(nproc)" \  
&& make install \  
\  
&& apt-get purge -y --auto-remove $buildDeps \  
&& cd / \  
&& rm -r /usr/src/ruby \  
\  
&& gem update --system "$RUBYGEMS_VERSION"  
  
ENV BUNDLER_VERSION 1.14.6  
  
RUN gem install bundler --version "$BUNDLER_VERSION"  
# install things globally, for great justice  
# and don't create ".bundle" in all our apps  
ENV GEM_HOME /usr/local/bundle  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH $BUNDLE_BIN:$PATH  
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \  
&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN"  
# Setup Code Climate test-reporter
(https://docs.codeclimate.com/docs/configuring-test-coverage)  
RUN curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-
latest-linux-amd64 > /usr/bin/cc-test-reporter && chmod +x /usr/bin/cc-test-
reporter  
  
RUN pip install awscli  
  
CMD [ "irb" ]  

