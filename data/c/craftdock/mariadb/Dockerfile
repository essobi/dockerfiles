# MariaDb apk builder  
FROM craftdock/apk-mariadb:10.2 as mariadb_apk_builder  
  
ENV PACKAGER "Hexosse <hexosse@gmail.com>"  
RUN set -x \  
# Build Hugo apk file  
&& /entrypoint abuild -r -P /packages \  
# Copy packages outside of builder volume  
&& sudo cp -r /packages /tmp/mariadb  
  
  
  
# Mariadb  
FROM craftdock/alpine-runit:latest  
  
LABEL maintainer="Hexosse <hexosse@gmail.com>" \  
description="Minimal Alpine image with MariaDb."  
  
ENV MARIADB_MAJOR 10.2  
ENV MARIADB_VERSION 10.2.14  
COPY \--from=mariadb_apk_builder /tmp/mariadb /tmp/mariadb  
  
RUN \  
# Print executed commands  
set -x \  
# Update repository indexes  
&& apk-update \  
# Install MairiaDB  
#
-------------------------------------------------------------------------------  
&& apk-install --repository http://dl-cdn.alpinelinux.org/alpine/edge/main/ \  
libressl \  
# MariaDb server and MariaDb client  
&& apk-install --repository /tmp/mariadb --allow-untrusted mariadb mariadb-
client \  
# Remove unecessary files  
&& rm -rf /usr/data/test/db.opt \  
&& rm -rf /usr/share/mysql/README* \  
&& rm -rf /usr/share/mysql/COPYING* \  
&& rm -rf /usr/share/mysql/*.cnf \  
&& rm -rf /usr/share/mysql/pkgconfig \  
# Remove unecessary files charsets (Keeping English and French)  
&& for _dir in "charsets czech danish dutch estonian german greek hindi
hungarian italian japanese korean norwegian norwegian-ny polish portuguese
romanian russian serbian slovak spanish swedish ukrainian"; do rm -rf $_dir;
done \  
# Remove terminfo  
&& find /usr/share/terminfo/ -mindepth 1 -type d ! -name x -print0 | xargs -0
rm -rf \  
# Make sure that mysql user can run MariaDB  
&& mkdir -p "/run/mysqld/" \  
&& chown -R mysql:mysql "/run/mysqld/" \  
# Clear apk's cache  
&& apk-cleanup  
  
# Copy scripts  
COPY /rootfs /  
  
# Add volume to allow persistence  
VOLUME ["/etc/mysql", "/var/lib/mysql", "/backup/mysql"]  
  
# Expose MariaDB port  
EXPOSE 3306

