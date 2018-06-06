FROM alpine  
ENV USER netatalk  
ENV PASSWD netatalk  
ENV UID 1000  
ENV NAME DATA  
ENV NETATALK_VERSION 3.1.11  
  
RUN apk add \--update \--no-cache tzdata && cp
/usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" >
/etc/timezone && apk del tzdata  
  
RUN apk add \--update \--no-cache avahi-libs libldap libacl cracklib glib
dbus-glib linux-pam libgcrypt && \  
apk add \--update \--no-cache \--virtual .build-deps build-base autoconf acl-
dev db-dev dbus-dev libevent-dev curl cracklib-dev linux-pam-dev libgcrypt-dev
openldap-dev dbus-glib-dev avahi-dev file && \  
curl -fsSL
https://downloads.sourceforge.net/project/netatalk/netatalk/${NETATALK_VERSION}/netatalk-${NETATALK_VERSION}.tar.gz
| tar xz -C /tmp && \  
cd /tmp/netatalk-${NETATALK_VERSION} && \  
./configure \--prefix=/usr \--sysconfdir=/etc \--mandir=/usr/share/man
\--localstatedir=/var \  
\--disable-silent-rules \  
\--enable-zeroconf \  
\--disable-tcp-wrappers \  
\--with-pam \  
\--with-shadow \  
\--with-ldap \  
\--with-acls \  
\--with-libevent \  
\--with-tdb \  
\--with-afpstats \  
\--with-cracklib \  
\--without-dtrace \  
\--without-libiconv \  
\--with-lockfile=/var/lock/netatalk && \  
make && make install && cd /tmp/ && rm -rf /tmp/netatalk-${NETATALK_VERSION}
&& \  
apk del .build-deps  
  
EXPOSE 548  
  
COPY entrypoint.sh /  
COPY docker-compose.yml /  
RUN chmod +x /entrypoint.sh  
  
WORKDIR /data  
  
VOLUME /data  
  
ENTRYPOINT ["/entrypoint.sh"]  

