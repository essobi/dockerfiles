FROM alpine:3.7  
  
ENV LDAP_DOMAIN example.com  
ENV LDAP_PASSWORD password  
ENV LDAP_ORGANIZATION example  
ENV LDAP_ADMIN_USERNAME admin  
ENV LDAP_ADMIN_PASSWORD password  
  
ENV OPENLDAP_VERSION=2.4.45  
  
RUN apk add \--update \--no-cache tzdata && cp
/usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" >
/etc/timezone  
  
RUN apk add \--update \--no-cache gettext ldapvi libintl unixodbc libssl1.0
libltdl \  
&& apk add \--update \--no-cache \--virtual .build-deps curl gcc cyrus-sasl-
dev make g++ libtool openssl-dev db-dev unixodbc-dev util-linux-dev groff \  
&& curl -fL ftp://ftp.openldap.org/pub/OpenLDAP/openldap-
release/openldap-${OPENLDAP_VERSION}.tgz | tar xz -C /tmp \  
&& curl -fL
https://git.alpinelinux.org/cgit/aports/plain/main/openldap/CVE-2017-9287.patch?h=3.7-stable
-o /tmp/CVE-2017-9287.patch \  
&& curl -fL
https://git.alpinelinux.org/cgit/aports/plain/main/openldap/openldap-2.4-ppolicy.patch?h=3.7-stable
-o /tmp/openldap-2.4-ppolicy.patch \  
&& curl -fL
https://git.alpinelinux.org/cgit/aports/plain/main/openldap/openldap-2.4.11-libldap_r.patch?h=3.7-stable
-o /tmp/openldap-2.4.11-libldap_r.patch \  
&& cd /tmp/openldap-${OPENLDAP_VERSION} \  
&& for p in /tmp/*.patch; do patch -p1 -i $p; done \  
&& ./configure \--prefix=/usr \  
\--libexecdir=/usr/lib \  
\--sysconfdir=/etc \  
\--mandir=/usr/share/man \  
\--localstatedir=/var/lib/openldap \  
\--enable-slapd \  
\--enable-crypt \  
\--enable-modules \  
\--enable-local \  
\--enable-dynamic \  
\--enable-bdb=mod \  
\--enable-dnssrv=mod \  
\--enable-hdb=mod \  
\--enable-ldap=mod \  
\--enable-mdb=mod \  
\--enable-meta=mod \  
\--enable-monitor=mod \  
\--enable-null=mod \  
\--enable-passwd=mod \  
\--enable-relay=mod \  
\--enable-shell=mod \  
\--enable-sock=mod \  
\--enable-sql=mod \  
\--enable-overlays=mod \  
\--with-tls=openssl \  
\--with-cyrus-sasl \  
&& make && make install && cd /tmp/ && rm -rf /tmp/* \  
&& cd /usr/sbin && ln -vs ../lib/slapd \  
&& apk del .build-deps \  
&& addgroup -S ldap 2>/dev/null \  
&& adduser -S -D -H -h /usr/lib/openldap -s /sbin/nologin -G ldap -g "OpenLdap
User" ldap 2>/dev/null \  
&& chown -vR ldap:ldap /etc/openldap /var/lib/openldap \  
&& rm /etc/openldap/slapd.ldif* /etc/openldap/slapd.conf*
/etc/openldap/ldap.conf* \  
&& mkdir -p /var/run/slapd/ && chown ldap:ldap /var/run/slapd/  
  
COPY schema/ /etc/openldap/schema/  
COPY ldap.conf /etc/openldap/  
COPY domain.init.ldif slapd.init.ldif /srv/openldap/  
COPY entrypoint.sh /  
  
VOLUME ["/etc/openldap/slapd.d", "/var/lib/openldap"]  
  
EXPOSE 389 636  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["slapd", "-h", "ldapi:/// ldap:///", "-u", "ldap", "-g", "ldap", "-F",
"/etc/openldap/slapd.d", "-d", "none"]  

