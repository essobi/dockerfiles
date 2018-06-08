FROM buildpack-deps:jessie  
  
# skip installing gem documentation  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc  
  
ENV RUBY_MAJOR 2.1  
ENV RUBY_VERSION 2.1.10  
ENV RUBY_DOWNLOAD_SHA256
5be9f8d5d29d252cd7f969ab7550e31bbb001feb4a83532301c0dd3b5006e148  
ENV RUBYGEMS_VERSION 2.6.12  
# some of ruby's build scripts are written in ruby  
# we purge system ruby later to make sure our final image uses what we just
built  
RUN set -ex \  
\  
&& buildDeps=' \  
bison \  
dpkg-dev \  
libgdbm-dev \  
ruby \  
' \  
&& echo "deb http://snapshot.debian.org/archive/debian/20140106T220635Z/
unstable main" > /etc/apt/sources.list.d/openssl.list \  
&& echo "deb-src http://snapshot.debian.org/archive/debian/20140106T220635Z/
unstable main" >> /etc/apt/sources.list.d/openssl.list \  
&& apt-get -o Acquire::Check-Valid-Until=false update \  
&& apt-get install -y --force-yes openssl=1.0.1f-1 libcurl4-openssl-dev
libssl-dev=1.0.1f-1 libssl1.0.0=1.0.1f-1 \  
&& rm /etc/apt/sources.list.d/openssl.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
\  
&& wget -O ruby.tar.xz "https://cache.ruby-
lang.org/pub/ruby/${RUBY_MAJOR%-rc}/ruby-$RUBY_VERSION.tar.xz" \  
&& echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.xz" | sha256sum -c - \  
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
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
&& ./configure \  
\--build="$gnuArch" \  
\--disable-install-doc \  
\--enable-shared \  
&& make -j "$(nproc)" \  
&& make install \  
\  
&& apt-get purge -y --auto-remove $buildDeps \  
&& cd / \  
&& rm -r /usr/src/ruby \  
\  
&& gem update --system "$RUBYGEMS_VERSION"  
  
ENV BUNDLER_VERSION 1.16.1  
  
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
  
WORKDIR /app  
  
ENV NEW_RELIC_LOG=stdout  
  
RUN addgroup --gid 1001 ruby \  
&& adduser --system --uid 1001 \--ingroup ruby --shell /bin/bash ruby \  
&& chown -R ruby:ruby /app \  
&& apt-get update && apt-get install -y --no-install-recommends \  
imagemagick \  
libmysqlclient-dev \  
libfontenc1 \  
libxfont1 \  
libxml2-dev \  
libxslt1-dev \  
nodejs \  
tzdata \  
xfonts-75dpi \  
xfonts-base \  
xfonts-encodings \  
xfonts-utils \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.2.1/wkhtmltox-0.12.2.1_linux-
jessie-amd64.deb \  
&& dpkg -i wkhtmltox-0.12.2.1_linux-jessie-amd64.deb  
  
USER ruby  

