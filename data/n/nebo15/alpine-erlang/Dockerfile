FROM alpine:3.7  
MAINTAINER Nebo #15 <support@nebo15.com>  
# Important! Update this no-op ENV variable when this Dockerfile  
# is updated with the current date. It will force refresh of all  
# of the base images and things like `apt-get update` won't be using  
# old cached versions when the Dockerfile is built.  
ENV REFRESHED_AT=2018-01-13  
  
ENV LANG=en_US.UTF-8 \  
HOME=/opt/app/ \  
# Set this so that CTRL+G works properly  
TERM=xterm \  
OTP_VERSION=20.2.2  
  
WORKDIR /tmp/erlang-build  
  
# Install Erlang  
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
apk add --no-cache --update ca-certificates && \  
# Install fetch deps  
apk add --no-cache --update --virtual .fetch-deps curl && \  
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
build-base \  
tar && \  
# Download Erlang/OTP  
curl -fSL -o otp-src.tar.gz "${OTP_DOWNLOAD_URL}" && \  
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
\--mandir=/usr/share/man \  
\--infodir=/usr/share/info \  
\--without-javac \  
\--without-jinterface \  
\--without-wx \  
\--without-debugger \  
\--without-observer \  
\--without-cosEvent \  
\--without-cosEventDomain \  
\--without-cosFileTransfer \  
\--without-cosNotification \  
\--without-cosProperty \  
\--without-cosTime \  
\--without-cosTransactions \  
\--without-dialyzer \  
\--without-et \  
\--without-gs \  
\--without-ic \  
\--without-megaco \  
\--without-orber \  
\--without-percept \  
\--without-odbc \  
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
find /usr/local -regex
'/usr/local/lib/erlang/\\(lib/\|erts-\\).*/\\(man\|doc\|src\|info\|examples\\)'
| xargs rm -rf && \  
rm -rf /usr/local/lib/erlang/lib/*test* \  
/usr/local/lib/erlang/usr \  
/usr/local/lib/erlang/misc \  
/usr/local/lib/erlang/erts*/lib/lib*.a \  
/usr/local/lib/erlang/erts*/lib/internal && \  
scanelf --nobanner -E ET_EXEC -BF '%F' \--recursive /usr/local | xargs strip
--strip-all && \  
scanelf --nobanner -E ET_DYN -BF '%F' \--recursive /usr/local | xargs -r strip
--strip-unneeded && \  
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
  
WORKDIR ${HOME}  
  
CMD ["erl"]  

