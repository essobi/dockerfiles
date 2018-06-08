FROM alpine:latest  
  
LABEL description "TeamSpeak is a full-featured proprietary VoIP software"  
# this fork is maintained by kleberbaum  
MAINTAINER Florian Kleber <kleberbaum@erebos.xyz>  
  
# change here to desired version  
ARG TS_VERSION=3.2.0  
  
ENV LANG=C.UTF-8  
ENV TS_DBSQLITE=data/ts3server.sqlitedb  
  
WORKDIR /teamspeak  
  
# update, install and cleaning  
RUN echo "## Installing base ##" && \  
echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >>
/etc/apk/repositories && \  
echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community/" >>
/etc/apk/repositories && \  
apk upgrade --update-cache --available && \  
\  
apk add --force \  
tini@community \  
ca-certificates \  
\  
&& echo "## Downloading ${TS_VERSION} ##" \  
&& apk add --no-cache bzip2 tar \  
&& wget -qO-
"http://dl.4players.de/ts/releases/${TS_VERSION}/teamspeak3-server_linux_amd64-${TS_VERSION}.tar.bz2"
| tar -xjv --strip-components=1 -C ${PWD} \  
&& apk del --purge --no-cache bzip2 tar \  
&& chown -R root:root ${PWD} \  
&& mv redist lib \  
&& mv libts3db_*.so lib/ \  
&& rm -R doc serverquerydocs tsdns ts3server_*.sh \  
\  
&& echo "## Installing GNU libc (aka glibc) ##" \  
&& ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download" \  
&& ALPINE_GLIBC_PACKAGE_VERSION="2.26-r0" \  
&&
ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk" \  
&& ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-
bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" \  
&&
ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
\  
&& apk add --no-cache --virtual=build-dependencies wget ca-certificates \  
\  
&&\  
wget \  
"https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub" \  
-O "/etc/apk/keys/sgerrand.rsa.pub" \  
\  
&&\  
wget \  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"
\  
\  
&&\  
apk add --no-cache \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" \  
\  
&& rm "/etc/apk/keys/sgerrand.rsa.pub" \  
&& /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
"$LANG" || true \  
&& echo "export LANG=$LANG" > /etc/profile.d/locale.sh \  
\  
&& apk del glibc-i18n \  
&& rm "/root/.wget-hsts" \  
&& apk del build-dependencies \  
&& rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/* \  
\  
&& \  
rm \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"  
  
EXPOSE 9987/udp 10011/tcp 30033/tcp  
  
VOLUME /teamspeak/config /teamspeak/files /teamspeak/logs /teamspeak/data  
  
# place init  
ADD run.sh /  
RUN chmod +x /run.sh  
  
# I personally like to start my containers with tini ^^  
ENTRYPOINT ["/sbin/tini", "--", "/run.sh"]  
  
# additional post-installation configurations  
CMD ["licensepath=config/", "createinifile=1", "inifile=config/ts3server.ini",
"query_ip_whitelist=config/query_ip_whitelist.txt",
"query_ip_blacklist=config/query_ip_blacklist.txt",
"dbpluginparameter=config/ts3db.ini"]  

