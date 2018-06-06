FROM clover/base AS base  
  
RUN groupadd \  
\--gid 50 \  
\--system \  
www \  
&& useradd \  
\--home-dir /var/www \  
\--no-create-home \  
\--system \  
\--shell /bin/false \  
\--uid 50 \  
\--gid 50 \  
www  
  
FROM library/ubuntu:bionic AS build  
  
ENV LANG=C.UTF-8  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y \  
software-properties-common \  
apt-utils  
  
RUN mkdir -p /build /rootfs  
WORKDIR /build  
RUN apt-get download \  
libapr1 \  
libaprutil1 \  
libaprutil1-dbd-sqlite3 \  
libaprutil1-dbd-mysql \  
libaprutil1-dbd-odbc \  
libaprutil1-dbd-pgsql \  
libaprutil1-ldap \  
libldap-2.4-2 \  
liblua5.1-0 \  
libxml2 \  
libuuid1 \  
libicu60 \  
liblzma5 \  
libexpat1 \  
libsqlite3-0 \  
libmysqlclient20 \  
libodbc1 \  
libpq5 \  
libgnutls30 \  
libgssapi3-heimdal \  
libsasl2-2 \  
libltdl7 \  
libgssapi-krb5-2 \  
libgmp10 \  
libhogweed4 \  
libidn11 \  
libnettle6 \  
libp11-kit0 \  
libtasn1-6 \  
libasn1-8-heimdal \  
libcomerr2 \  
libhcrypto4-heimdal \  
libheimntlm0-heimdal \  
libkrb5-26-heimdal \  
libroken18-heimdal \  
libsasl2-modules-db \  
libk5crypto3 \  
libkrb5-3 \  
libkrb5support0 \  
libffi6 \  
libwind0-heimdal \  
libheimbase1-heimdal \  
libhx509-5-heimdal \  
libkeyutils1 \  
apache2-bin \  
apache2-data \  
apache2-utils \  
apache2  
RUN find *.deb | xargs -I % dpkg-deb -x % /rootfs  
  
WORKDIR /rootfs  
RUN rm -rf \  
etc/apache2/sites-available/* \  
etc/apache2/conf-available/* \  
etc/apache2/envvars \  
etc/cron* \  
etc/default \  
etc/gss/mech.d/README \  
etc/init.d \  
etc/logrotate.d \  
etc/ufw \  
lib/systemd \  
usr/sbin/a2* \  
usr/sbin/apache2ctl \  
usr/sbin/apachectl \  
usr/sbin/check_forensic \  
usr/sbin/split-logfile \  
usr/share/apache2/build \  
usr/share/apache2/default-site \  
usr/share/apache2/error/README \  
usr/share/apache2/icons/README* \  
usr/share/apache2/apache2-maintscript-helper \  
usr/share/apache2/ask-for-passphrase \  
usr/share/apport \  
usr/share/bash-completion \  
usr/share/bug \  
usr/share/lintian \  
usr/share/doc \  
usr/share/man \  
var/www/html \  
&& mkdir -p var/lock/apache2 var/run/apache2 \  
&& ln -s /dev/stderr var/log/apache2//error.log \  
&& ln -s /dev/stdout var/log/apache2/access.log \  
&& find \  
etc/apache2/*.conf \  
etc/apache2/mods-available/*.conf \  
| xargs -I % sed -i -r \  
-e 's,[$][{]APACHE_PID_FILE[}],/var/run/apache2/apache2.pid,g' \  
-e 's,[$][{]APACHE_LOCK_DIR[}],/var/lock/apache2,g' \  
-e 's,[$][{]APACHE_RUN_DIR[}],/var/run/apache2,g' \  
-e 's,[$][{]APACHE_LOG_DIR[}],/var/log/apache2,g' \  
-e 's,[$][{]APACHE_RUN_USER[}],www,g' \  
-e 's,[$][{]APACHE_RUN_GROUP[}],www,g' \  
% \  
&& find \  
etc/ldap/ldap.conf \  
| xargs -I % sed -i -r \  
-e 's,^[[:space:]]*[#;]+.*$,,g' \  
-e 's,[[:space:]]+, ,g' \  
-e '/^[[:space:]]*$/d' \  
% \  
&& ln -s ../conf-available/charset.conf etc/apache2/conf-enabled/charset.conf
\  
&& ln -s ../conf-available/log-format.conf etc/apache2/conf-enabled/log-
format.conf \  
&& ln -s ../conf-available/security.conf etc/apache2/conf-
enabled/security.conf \  
&& ln -s ../conf-available/tuning.conf etc/apache2/conf-enabled/tuning.conf \  
&& ln -s ../sites-available/000-default.conf etc/apache2/sites-
enabled/000-default.conf \  
&& ln -s ../mods-available/access_compat.load etc/apache2/mods-
enabled/access_compat.load \  
&& ln -s ../mods-available/actions.load etc/apache2/mods-enabled/actions.load
\  
&& ln -s ../mods-available/alias.load etc/apache2/mods-enabled/alias.load \  
&& ln -s ../mods-available/allowmethods.load etc/apache2/mods-
enabled/allowmethods.load \  
&& ln -s ../mods-available/auth_basic.load etc/apache2/mods-
enabled/auth_basic.load \  
&& ln -s ../mods-available/auth_digest.load etc/apache2/mods-
enabled/auth_digest.load \  
&& ln -s ../mods-available/authn_core.load etc/apache2/mods-
enabled/authn_core.load \  
&& ln -s ../mods-available/authn_file.load etc/apache2/mods-
enabled/authn_file.load \  
&& ln -s ../mods-available/authz_groupfile.load etc/apache2/mods-
enabled/authz_groupfile.load \  
&& ln -s ../mods-available/authz_core.load etc/apache2/mods-
enabled/authz_core.load \  
&& ln -s ../mods-available/authz_host.load etc/apache2/mods-
enabled/authz_host.load \  
&& ln -s ../mods-available/authz_user.load etc/apache2/mods-
enabled/authz_user.load \  
&& ln -s ../mods-available/deflate.load etc/apache2/mods-enabled/deflate.load
\  
&& ln -s ../mods-available/dir.load etc/apache2/mods-enabled/dir.load \  
&& ln -s ../mods-available/env.load etc/apache2/mods-enabled/env.load \  
&& ln -s ../mods-available/expires.load etc/apache2/mods-enabled/expires.load
\  
&& ln -s ../mods-available/ext_filter.load etc/apache2/mods-
enabled/ext_filter.load \  
&& ln -s ../mods-available/filter.load etc/apache2/mods-enabled/filter.load \  
&& ln -s ../mods-available/headers.load etc/apache2/mods-enabled/headers.load
\  
&& ln -s ../mods-available/ident.load etc/apache2/mods-enabled/ident.load \  
&& ln -s ../mods-available/include.load etc/apache2/mods-enabled/include.load
\  
&& ln -s ../mods-available/mime.load etc/apache2/mods-enabled/mime.load \  
&& ln -s ../mods-available/mime.conf etc/apache2/mods-enabled/mime.conf \  
&& ln -s ../mods-available/mpm_event.load etc/apache2/mods-
enabled/mpm_event.load \  
&& ln -s ../mods-available/mpm_event.conf etc/apache2/mods-
enabled/mpm_event.conf \  
&& ln -s ../mods-available/proxy.load etc/apache2/mods-enabled/proxy.load \  
&& ln -s ../mods-available/proxy_fcgi.load etc/apache2/mods-
enabled/proxy_fcgi.load \  
&& ln -s ../mods-available/ratelimit.load etc/apache2/mods-
enabled/ratelimit.load \  
&& ln -s ../mods-available/remoteip.load etc/apache2/mods-
enabled/remoteip.load \  
&& ln -s ../mods-available/reqtimeout.load etc/apache2/mods-
enabled/reqtimeout.load \  
&& ln -s ../mods-available/reqtimeout.conf etc/apache2/mods-
enabled/reqtimeout.conf \  
&& ln -s ../mods-available/request.load etc/apache2/mods-enabled/request.load
\  
&& ln -s ../mods-available/rewrite.load etc/apache2/mods-enabled/rewrite.load
\  
&& ln -s ../mods-available/setenvif.load etc/apache2/mods-
enabled/setenvif.load \  
&& ln -s ../mods-available/vhost_alias.load etc/apache2/mods-
enabled/vhost_alias.load  
  
COPY --from=base /etc/group /etc/gshadow /etc/passwd /etc/shadow etc/  
COPY apache2.conf ports.conf etc/apache2/  
COPY conf-available/ etc/apache2/conf-available/  
COPY sites-available/ etc/apache2/sites-available/  
COPY init.sh etc/  
  
WORKDIR /  
  
  
FROM clover/common  
  
ENV LANG=C.UTF-8  
  
COPY --from=build /rootfs /  
  
CMD ["sh", "/etc/init.sh"]  
  
EXPOSE 80 443  

