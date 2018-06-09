FROM alpine:3.5  
# Install su-exec for easy step-down from root  
RUN set -x \  
&& apk --no-cache add su-exec  
  
# Install the GNU C library and set locales  
ENV GLIBC_VERSION=2.25-r0  
RUN set -x \  
&& apk --no-cache --virtual .build-dependencies add wget ca-certificates \  
&& wget -q -O /etc/apk/keys/sgerrand.rsa.pub
"https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub" \  
&& wget -q "https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk" \  
&& wget -q "https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk" \  
&& wget -q "https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-i18n-${GLIBC_VERSION}.apk" \  
&& apk --no-cache add glibc-${GLIBC_VERSION}.apk glibc-
bin-${GLIBC_VERSION}.apk glibc-i18n-${GLIBC_VERSION}.apk \  
&& /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8 \  
&& apk del .build-dependencies \  
&& rm /etc/apk/keys/sgerrand.rsa.pub *.apk /root/.wget-hsts  
ENV LANG=en_US.UTF-8  
# Get TeamSpeak server  
ENV VERSION=3.0.13.6  
ENV SHA256=19ccd8db5427758d972a864b70d4a1263ebb9628fcc42c3de75ba87de105d179  
RUN set -x \  
&& apk --no-cache --virtual .build-dependencies add tar wget \  
&& mkdir /usr/share/teamspeak /var/lib/teamspeak \  
&& wget -q -O /tmp/teamspeak.tar.bz2
"http://dl.4players.de/ts/releases/${VERSION}/teamspeak3-server_linux_amd64-${VERSION}.tar.bz2"
\  
&& echo "${SHA256} /tmp/teamspeak.tar.bz2" | sha256sum -c - \  
&& tar --xform "s:teamspeak3-server_linux_amd64:.:" -C /tmp -jxf
/tmp/teamspeak.tar.bz2 \  
&& mv /tmp/ts3server /usr/bin \  
&& mv /tmp/libts3db_sqlite3.so /usr/glibc-compat/lib \  
&& mv /tmp/sql /usr/share/teamspeak \  
&& chmod 755 /usr/bin/ts3server \  
&& chmod 644 /usr/glibc-compat/lib/libts3db_sqlite3.so \  
&& find /usr/share/teamspeak -type d -exec chmod 755 {} \; \  
&& find /usr/share/teamspeak -type f -exec chmod 644 {} \; \  
&& apk del .build-dependencies \  
&& rm -rf /tmp/*  
  
VOLUME ["/var/lib/teamspeak"]  
WORKDIR /var/lib/teamspeak  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 9987/udp  
EXPOSE 10011  
EXPOSE 30033  
CMD ["ts3server", "dbsqlpath=/usr/share/teamspeak/sql/"]  

