FROM alpine:3.4  
# skip installing gem documentation  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc  
  
ENV RUBY_MAJOR 2.1  
ENV RUBY_VERSION 2.1.2  
ENV RUBY_DOWNLOAD_SHA256
f22a6447811a81f3c808d1c2a5ce3b5f5f0955c68c9a749182feb425589e6635  
ENV RUBYGEMS_VERSION 2.2.2  
ENV BUNDLER_VERSION 1.16.1  
# some of ruby's build scripts are written in ruby  
# we purge system ruby later to make sure our final image uses what we just
built  
# readline-dev vs libedit-dev: https://bugs.ruby-lang.org/issues/11869 and
https://github.com/docker-library/ruby/issues/75  
RUN set -ex \  
\  
&& apk --update add --no-cache --virtual .ruby-builddeps \  
autoconf \  
bison \  
bzip2 \  
bzip2-dev \  
ca-certificates \  
coreutils \  
dpkg-dev dpkg \  
gcc \  
gdbm-dev \  
glib-dev \  
libc-dev \  
libffi-dev \  
openssl \  
openssl-dev \  
libxml2-dev \  
libxslt-dev \  
linux-headers \  
make \  
ncurses-dev \  
procps \  
readline-dev \  
ruby \  
tar \  
yaml-dev \  
zlib-dev \  
\  
&& wget -O ruby.tar.gz "https://cache.ruby-
lang.org/pub/ruby/${RUBY_MAJOR%}/ruby-$RUBY_VERSION.tar.gz" \  
&& echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.gz" | sha256sum -c - \  
\  
&& mkdir -p /usr/src/ruby \  
&& tar -xvf ruby.tar.gz -C /usr/src/ruby --strip-components=1 \  
&& rm ruby.tar.gz \  
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
# the configure script does not detect isnan/isinf as macros  
&& export ac_cv_func_isnan=yes ac_cv_func_isinf=yes \  
&& ./configure \  
\--build="$gnuArch" \  
\--disable-install-doc \  
\--enable-shared \  
&& make -j "$(nproc)" \  
&& make install \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add --virtual .ruby-rundeps $runDeps \  
bzip2 \  
ca-certificates \  
libffi-dev \  
openssl-dev \  
procps \  
yaml-dev \  
zlib-dev \  
gcc g++ linux-headers musl-dev libxslt-dev libxml2-dev \  
&& cd / \  
&& rm -r /usr/src/ruby \  
\  
&& gem update --system "$RUBYGEMS_VERSION" \  
&& gem install bundler --version "$BUNDLER_VERSION" \--force \  
&& rm -r /root/.gem/  
  
# install things globally, for great justice  
# and don't create ".bundle" in all our apps  
ENV GEM_HOME /usr/local/bundle  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH $BUNDLE_BIN:$PATH  
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \  
&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN" \  
&& apk del .ruby-builddeps  
RUN apk add ansible unzip git nodejs  
  
CMD [ "irb" ]

