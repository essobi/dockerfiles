FROM golang:1.9-alpine as build  
  
RUN apk add -U bash git make  
RUN go get github.com/Shopify/ejson \  
&& (cd /go/src/github.com/Shopify/ejson; make binaries)  
  
FROM alpine:3.7  
##############  
## Versions ##  
##############  
# elixir expects utf8.  
ENV OTP_VERSION="20.3.2" \  
OTP_DOWNLOAD_SHA256=9809be52baa23d6fd18ee70b9a9b7c548e44f586db2f46ff5bfe66719cfab10a
\  
ELIXIR_VERSION="v1.6.4" \  
ELIXIR_DOWNLOAD_SHA256=3a081c07d8ea2ce6620201e2689ce1fac0ee937ba5c13670cbaa40349e1581ab
\  
LANG=C.UTF-8 \  
RUBY_MAJOR=2.4 \  
RUBY_VERSION=2.4.1 \  
RUBY_DOWNLOAD_SHA256=4fc8a9992de3e90191de369270ea4b6c1b171b7941743614cc50822ddc1fe654
\  
RUBYGEMS_VERSION=2.6.13 \  
BUNDLER_VERSION=1.15.4  
############  
## Erlang ##  
############  
  
RUN set -xe \  
&&
OTP_DOWNLOAD_URL="https://github.com/erlang/otp/archive/OTP-${OTP_VERSION}.tar.gz"
\  
&& apk add --no-cache --virtual .fetch-deps \  
curl \  
ca-certificates \  
&& curl -fSL -o otp-src.tar.gz "$OTP_DOWNLOAD_URL" \  
&& echo "$OTP_DOWNLOAD_SHA256 otp-src.tar.gz" | sha256sum -c - \  
&& apk add --no-cache --virtual .build-deps \  
dpkg-dev dpkg \  
gcc \  
g++ \  
libc-dev \  
linux-headers \  
make \  
autoconf \  
ncurses-dev \  
openssl-dev \  
unixodbc-dev \  
lksctp-tools-dev \  
tar \  
&& export ERL_TOP="/usr/src/otp_src_${OTP_VERSION%%@*}" \  
&& mkdir -vp $ERL_TOP \  
&& tar -xzf otp-src.tar.gz -C $ERL_TOP --strip-components=1 \  
&& rm otp-src.tar.gz \  
&& ( cd $ERL_TOP \  
&& ./otp_build autoconf \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
&& ./configure --build="$gnuArch" \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install ) \  
&& rm -rf $ERL_TOP \  
&& find /usr/local -regex
'/usr/local/lib/erlang/\\(lib/\|erts-\\).*/\\(man\|doc\|obj\|c_src\|emacs\|info\|examples\\)'
| xargs rm -rf \  
&& find /usr/local -name src | xargs -r find | grep -v '\\.hrl$' | xargs rm -v
|| true \  
&& find /usr/local -name src | xargs -r find | xargs rmdir -vp || true \  
&& scanelf --nobanner -E ET_EXEC -BF '%F' \--recursive /usr/local | xargs -r
strip --strip-all \  
&& scanelf --nobanner -E ET_DYN -BF '%F' \--recursive /usr/local | xargs -r
strip --strip-unneeded \  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add --virtual .erlang-rundeps $runDeps lksctp-tools \  
&& apk del .fetch-deps .build-deps  
  
############  
## Elixir ##  
############  
  
RUN set -xe \  
&& ELIXIR_DOWNLOAD_URL="https://github.com/elixir-
lang/elixir/releases/download/${ELIXIR_VERSION}/Precompiled.zip" \  
&& buildDeps=' \  
ca-certificates \  
curl \  
unzip \  
' \  
&& apk add --no-cache --virtual .build-deps $buildDeps \  
&& curl -fSL -o elixir-precompiled.zip $ELIXIR_DOWNLOAD_URL \  
&& echo "$ELIXIR_DOWNLOAD_SHA256 elixir-precompiled.zip" | sha256sum -c - \  
&& unzip -d /usr/local elixir-precompiled.zip \  
&& rm elixir-precompiled.zip \  
&& apk del .build-deps  
  
###########  
## Ruby ##  
###########  
  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc  
  
# some of ruby's build scripts are written in ruby  
# we purge system ruby later to make sure our final image uses what we just
built  
# readline-dev vs libedit-dev: https://bugs.ruby-lang.org/issues/11869 and
https://github.com/docker-library/ruby/issues/75  
RUN set -ex \  
\  
&& apk add --no-cache --virtual .ruby-builddeps \  
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
libressl \  
libressl-dev \  
libxml2-dev \  
libxslt-dev \  
linux-headers \  
make \  
ncurses-dev \  
procps \  
readline-dev \  
ruby \  
tar \  
xz \  
yaml-dev \  
zlib-dev \  
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
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .ruby-rundeps $runDeps \  
bzip2 \  
ca-certificates \  
libffi-dev \  
libressl-dev \  
procps \  
yaml-dev \  
zlib-dev \  
&& apk del .ruby-builddeps \  
&& cd / \  
&& rm -r /usr/src/ruby \  
\  
&& gem update --system "$RUBYGEMS_VERSION" \  
&& gem install bundler --version "$BUNDLER_VERSION"  
  
# install things globally, for great justice  
# and don't create ".bundle" in all our apps  
ENV GEM_HOME=/usr/local/bundle \  
BUNDLE_PATH="/usr/local/bundle" \  
BUNDLE_BIN="/usr/local/bundle/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="/usr/local/bundle" \  
PATH=/usr/local/bundle/bin:$PATH  
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \  
&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN"  
####################  
## Customizations ##  
####################  
#########################  
## Common Runtime Deps ##  
#########################  
  
COPY --from=build /go/src/github.com/Shopify/ejson/build/bin/linux-amd64
/usr/local/bin/ejson  
  
# coreutils below is needed as of 2/16/2018  
# `env` seems to be broken with `-u` which  
# is used in the load_env script  
RUN mix local.hex --force \  
&& mix local.rebar --force \  
&& commonDeps='coreutils libpq tzdata ca-certificates bash jq imagemagick' \  
&& apk add -U --no-cache --virtual .common-deps $commonDeps  
  
CMD ["iex"]  

