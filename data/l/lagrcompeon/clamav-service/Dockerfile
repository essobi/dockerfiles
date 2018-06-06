FROM buildpack-deps:jessie  
MAINTAINER https://compeon.de Lars Greiving <lgreiving@compeon.de>  
  
# skip installing gem documentation  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc  
  
ENV RUBY_MAJOR 2.3  
ENV RUBY_VERSION 2.3.1  
ENV RUBY_DOWNLOAD_SHA256
b87c738cb2032bf4920fef8e3864dc5cf8eae9d89d8d523ce0236945c5797dcd  
ENV RUBYGEMS_VERSION 2.6.6  
# some of ruby's build scripts are written in ruby  
# we purge this later to make sure our final image uses what we just built  
RUN set -ex \  
&& buildDeps=' \  
bison \  
libgdbm-dev \  
ruby \  
' \  
&& clamavDeps=' \  
clamav-daemon \  
clamav-freshclam \  
clamdscan \  
libclamunrar7 \  
' \  
&& echo "deb http://http.debian.net/debian/ jessie main contrib non-free" >
/etc/apt/sources.list \  
&& echo "deb http://http.debian.net/debian/ jessie-updates main contrib non-
free" >> /etc/apt/sources.list \  
&& echo "deb http://security.debian.org/ jessie/updates main contrib non-free"
>> /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& apt-get install -y --no-install-recommends $clamavDeps \  
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
  
ENV BUNDLER_VERSION 1.12.5  
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
  
# initial update of av databases  
RUN wget -O /var/lib/clamav/main.cvd http://database.clamav.net/main.cvd && \  
wget -O /var/lib/clamav/daily.cvd http://database.clamav.net/daily.cvd && \  
wget -O /var/lib/clamav/bytecode.cvd http://database.clamav.net/bytecode.cvd
&& \  
chown clamav:clamav /var/lib/clamav/*.cvd  
  
# permission juggling  
RUN mkdir /var/run/clamav && \  
chown clamav:clamav /var/run/clamav && \  
chmod 750 /var/run/clamav  
  
# av configuration update  
RUN sed -i 's/^Foreground .*$/Foreground true/g' /etc/clamav/freshclam.conf  
  
# volume provision  
VOLUME ["/var/lib/clamav"]  
  
# av daemon bootstrapping  
ADD Gemfile /  
RUN bundle  
ADD . /  
CMD ["bash", "/bootstrap.sh"]  

