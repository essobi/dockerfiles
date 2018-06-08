# fetch latest tag release as 'latest' fails  
# FROM exira/base:latest  
FROM exira/base:3.4.2  
MAINTAINER exira.com <info@exira.com>  
  
ARG CONTAINER_UID=1002  
ARG CONTAINER_GID=1002  
ENV POWERDNS_VERSION=3.4.8 \  
CONTAINER_USER=pdns \  
CONTAINER_GROUP=pdns  
  
ADD disable-execinfo.patch /tmp/disable-execinfo.patch  
ADD packageversion.patch /tmp/packageversion.patch  
  
RUN \  
# add pdns user  
mkdir -p /home/${CONTAINER_USER} && \  
addgroup -g $CONTAINER_GID -S ${CONTAINER_GROUP} && \  
adduser -u $CONTAINER_UID -S -D -G ${CONTAINER_GROUP} -h
/home/${CONTAINER_USER} -s /bin/sh ${CONTAINER_USER} && \  
chown -R ${CONTAINER_USER}:${CONTAINER_GROUP} /home/${CONTAINER_USER} && \  
  
# Install build and runtime packages  
#build_pkgs="build-base re2c file readline-dev autoconf binutils bison
libxml2-dev curl-dev freetype-dev openssl-dev libjpeg-turbo-dev libpng-dev
libwebp-dev libmcrypt-dev gmp-dev icu-dev libmemcached-dev wget git tzdata" &&
\  
build_pkgs="build-base wget boost-dev mariadb-dev git autoconf automake bison
flex g++ libtool make ragel" && \  
runtime_pkgs="mysql-client musl bash boost-program_options boost-serialization
mariadb-libs libstdc++" && \  
apk update && \  
apk upgrade && \  
apk --update --no-cache add ${build_pkgs} ${runtime_pkgs} && \  
  
# download unpack pdns  
mkdir /tmp/pdns && \  
cd /tmp/pdns && \  
git clone https://github.com/PowerDNS/pdns.git -v -b auth-${POWERDNS_VERSION}
. && \  
  
# patch pdns for alpine  
git apply -v /tmp/disable-execinfo.patch && \  
  
# patch pdns for security packageversion checks  
git apply -v /tmp/packageversion.patch && \  
  
# compile pdns  
./bootstrap && \  
./configure PACKAGEVERSION=${POWERDNS_VERSION} \  
\--prefix=/usr \  
\--sysconfdir=/etc \  
\--mandir=/usr/share/man \  
\--infodir=/usr/share/info \  
\--localstatedir=/var \  
\--libdir=/usr/lib/pdns \  
\--with-modules="bind gmysql" \  
\--with-dynmodules="" \  
\--without-lua \  
\--disable-static && \  
make && \  
make install && \  
make clean && \  
mkdir -p /var/lib/powerdns/zones && \  
  
# strip debug symbols from the binary (GREATLY reduces binary size)  
strip -s /usr/sbin/pdns_server && \  
  
# remove dev dependencies  
apk del ${build_pkgs} && \  
  
# other clean up  
rm /etc/pdns.conf-dist && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/* && \  
rm -rf /var/log/*  
  
ADD pdns.initd /etc/init.d/pdns  
ADD pdns.sql /pdns.sql  
ADD named.conf-slave /named.conf-slave  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh && \  
chmod 755 /etc/init.d/pdns  
  
VOLUME /var/lib/powerdns/  
  
EXPOSE 5300/tcp  
EXPOSE 5300/udp  
EXPOSE 8000  
CMD ["/run.sh"]  

