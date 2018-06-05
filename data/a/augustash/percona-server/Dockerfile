FROM augustash/baseimage:1.0.0  
MAINTAINER Pete McWilliams <pmcwilliams@augustash.com>  
  
ARG DEBIAN_FRONTEND="noninteractive"  
ARG PERCONA_MAJOR="5.7"  
ARG PERCONA_VERSION="5.7.17-11-1.xenial"  
# environment  
ENV MYSQL_ROOT_PASSWORD root  
ENV MYSQL_ALLOW_EMPTY_PASSWORD false  
ENV APTLIST \  
percona-server-client-${PERCONA_MAJOR} \  
percona-server-server-${PERCONA_MAJOR}=${PERCONA_VERSION} \  
percona-toolkit \  
percona-xtrabackup-24 \  
pwgen  
  
# packages & configure  
RUN { \  
echo percona-server-server-$PERCONA_MAJOR percona-server-server/root_password
password 'unused'; \  
echo percona-server-server-$PERCONA_MAJOR percona-server-
server/root_password_again password 'unused'; \  
} | debconf-set-selections && \  
apt-key adv --keyserver keys.gnupg.net --recv-keys 8507EFA5 && \  
echo "deb http://repo.percona.com/apt `lsb_release -cs` main" >
/etc/apt/sources.list.d/percona.list && \  
{ \  
echo 'Package: *'; \  
echo 'Pin: release o=Percona Development Team'; \  
echo 'Pin-Priority: 998'; \  
} > /etc/apt/preferences.d/percona && \  
  
apt-get -yqq update && \  
apt-get -yqq install --no-install-recommends --no-install-suggests $APTLIST
$BUILD_DEPS && \  
  
sed -ri 's/^user\s+=\s+mysql/user = ash/' /etc/mysql/percona-
server.conf.d/mysqld.cnf && \  
sed -Ei 's/^bind-address/#&/' /etc/mysql/percona-server.conf.d/mysqld.cnf && \  
echo 'skip-host-cache\nskip-name-resolve' | awk '{ print } $1 == "[mysqld]" &&
c == 0 { c = 1; system("cat") }' \  
/etc/mysql/percona-server.conf.d/mysqld.cnf > /tmp/my.cnf && \  
mv /tmp/my.cnf /etc/mysql/percona-server.conf.d/mysqld.cnf && \  
  
mkdir -p \  
/config/mysql/conf.d && \  
  
apt-get -yqq purge --auto-remove -o APT::AutoRemove::RecommendsImportant=false
$BUILD_DEPS && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# root filesystem  
COPY rootfs /  
  
# run s6 supervisor  
ENTRYPOINT ["/init"]  
EXPOSE 3306  
VOLUME ["/var/lib/mysql", "/var/log/mysql"]  

