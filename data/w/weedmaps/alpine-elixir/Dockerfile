FROM alpine:3.6  
  
ENV LANG=en.US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8 \  
HOME=/opt/app \  
TERM=xterm \  
OTP_VERSION=20.0 \  
ELIXIR_VERSION=1.5.1  
  
WORKDIR /tmp/erlang-build  
  
RUN set -xe && \  
OTP_DOWNLOAD_URL="https://github.com/erlang/otp/archive/OTP-${OTP_VERSION}.tar.gz"
&& \  
# Create default user and home directory, set owner to default  
mkdir -p ${HOME} && \  
adduser -s /bin/sh -u 1001 -G root -h ${HOME} -S -D default && \  
chown -R 1001:0 ${HOME} && \  
# Add edge repos tagged so that we can selectively install edge packages  
echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories && \  
# Upgrade Alpine and base packages  
apk --no-cache --update upgrade && \  
apk add --no-cache --update ca-certificates && \  
# Install fetch deps  
apk add --no-cache --virtual .fetch-deps curl && \  
curl -fSL -o otp-src.tar.gz "${OTP_DOWNLOAD_URL}" && \  
# Install Erlang/OTP build deps  
apk add --no-cache --update --virtual .build-deps \  
pcre@edge \  
openssl-dev \  
ncurses-dev \  
zlib-dev \  
gcc \  
perl-dev \  
libc-dev \  
make \  
autoconf \  
alpine-sdk \  
build-base \  
tar && \  
export ERL_TOP="/usr/src/otp_src_${OTP_VERSION%%@*}" && \  
mkdir -vp $ERL_TOP && \  
tar -xzf otp-src.tar.gz -C $ERL_TOP --strip-components=1 && \  
rm otp-src.tar.gz && \  
( cd $ERL_TOP && \  
# export OTP_SMALL_BUILD=true && \  
export CPPFlAGS="-D_BSD_SOURCE $CPPFLAGS" && \  
./otp_build autoconf && \  
./configure \  
\--prefix=/usr/local \  
\--sysconfdir=/etc \  
\--enable-kernel-poll \  
\--enable-threads \  
\--enable-shared-zlib \  
\--enable-dynamic-ssl-lib \  
\--enable-ssl=dynamic-ssl-lib \  
\--enable-sctp \  
\--enable-hipe \  
\--enable-dirty-schedulers && \  
make -j$(getconf _NPROCESSORS_ONLN) && \  
make install ) && \  
rm -rf $ERL_TOP && \  
runDeps=$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
) && \  
apk add --virtual .erlang-rundeps $runDeps && \  
apk del .fetch-deps .build-deps && \  
rm -rf /var/cache/apk/* && \  
# Update CA certificates  
update-ca-certificates --fresh  
  
WORKDIR /tmp/elixir-build  
  
RUN set -xe; \  
ELIXIR_DOWNLOAD_URL="https://github.com/elixir-
lang/elixir/releases/download/v${ELIXIR_VERSION}/Precompiled.zip" && \  
# Install Elixir build deps  
apk add --no-cache --update --virtual .elixir-build \  
unzip \  
curl \  
ca-certificates && \  
# Download and validate Elixir checksum  
curl -fSL -o elixir-precompiled.zip "${ELIXIR_DOWNLOAD_URL}" && \  
unzip -d /usr/local elixir-precompiled.zip && \  
rm elixir-precompiled.zip && \  
# Install Hex and Rebar  
mix local.hex --force && \  
mix local.rebar --force && \  
cd /tmp && \  
rm -rf /tmp/elixir-build && \  
# Delete Elixir build deps  
apk del .elixir-build  
  
WORKDIR ${HOME}  
  
CMD ["iex"]  

