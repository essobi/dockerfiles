# vim:set ft=dockerfile:  
FROM ubuntu:18.04  
ENV DEBIAN_FRONTEND=noninteractive  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
# add gosu for easy step-down from root  
ENV GOSU_VERSION 1.10  
RUN set -ex; \  
\  
fetchDeps=' \  
ca-certificates \  
wget \  
'; \  
apt-get update; \  
apt-get install -y --no-install-recommends $fetchDeps dirmngr gpg gnupg-agent;
\  
rm -rf /var/lib/apt/lists/*; \  
\  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch";
\  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc";
\  
\  
# verify the signature  
export GNUPGHOME="$(mktemp -d)"; \  
for server in $(shuf -e ha.pool.sks-keyservers.net \  
hkp://p80.pool.sks-keyservers.net:80 \  
keyserver.ubuntu.com \  
hkp://keyserver.ubuntu.com:80 \  
pgp.mit.edu) ; do \  
gpg --keyserver "$server" \--recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 && break || : ; \  
done && \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \  
rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc || true; \  
\  
chmod +x /usr/local/bin/gosu; \  
# verify that the binary works  
gosu nobody true; \  
\  
apt-get purge -y --auto-remove $fetchDeps  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
# install "pwgen" for randomizing passwords  
# install "apt-transport-https" for Percona's repo (switched to https-only)  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-transport-https ca-certificates \  
pwgen \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GPG_KEYS \  
# Key fingerprint = 177F 4010 FE56 CA33 3630 0305 F165 6F24 C74C D1D8  
# MariaDB Package Signing Key <package-signing-key@mariadb.org>  
177F4010FE56CA3336300305F1656F24C74CD1D8 \  
# pub 1024D/CD2EFD2A 2009-12-15  
# Key fingerprint = 430B DF5C 56E7 C94E 848E E60C 1C4C BDCD CD2E FD2A  
# uid Percona MySQL Development Team <mysql-dev@percona.com>  
# sub 2048g/2D607DAF 2009-12-15  
430BDF5C56E7C94E848EE60C1C4CBDCDCD2EFD2A \  
# pub 4096R/8507EFA5 2016-06-30  
# Key fingerprint = 4D1B B29D 63D9 8E42 2B21 13B1 9334 A25F 8507 EFA5  
# uid Percona MySQL Development Team (Packaging key) <mysql-dev@percona.com>  
# sub 4096R/4CAC6D72 2016-06-30  
4D1BB29D63D98E422B2113B19334A25F8507EFA5  
RUN set -ex; \  
export GNUPGHOME="$(mktemp -d)"; \  
for key in $GPG_KEYS; do \  
for server in $(shuf -e ha.pool.sks-keyservers.net \  
hkp://p80.pool.sks-keyservers.net:80 \  
keyserver.ubuntu.com \  
hkp://keyserver.ubuntu.com:80 \  
pgp.mit.edu) ; do \  
gpg --keyserver "$server" \--recv-keys "$key" && break || : ; \  
done ; \  
done; \  
gpg --export $GPG_KEYS > /etc/apt/trusted.gpg.d/mariadb.gpg; \  
rm -r "$GNUPGHOME" || true; \  
apt-key list  
  
# add Percona's repo for xtrabackup (which is useful for Galera)  
RUN echo "deb https://repo.percona.com/apt artful main" >
/etc/apt/sources.list.d/percona.list \  
&& { \  
echo 'Package: *'; \  
echo 'Pin: release o=Percona Development Team'; \  
echo 'Pin-Priority: 998'; \  
} > /etc/apt/preferences.d/percona  
  
ENV MARIADB_MAJOR 10.1  
ENV MARIADB_VERSION 10.1.33+maria~bionic  
  
RUN echo "deb https://mirrors.dotsrc.org/mariadb/repo/$MARIADB_MAJOR/ubuntu
bionic main" > /etc/apt/sources.list.d/mariadb.list \  
&& { \  
echo 'Package: *'; \  
echo 'Pin: release o=MariaDB'; \  
echo 'Pin-Priority: 999'; \  
} > /etc/apt/preferences.d/mariadb  
# add repository pinning to make sure dependencies from this MariaDB repo are
preferred over Debian dependencies  
# libmariadbclient18 : Depends: libmysqlclient18 (= 5.5.42+maria-1~wheezy) but
5.5.43-0+deb7u1 is to be installed  
# the "/var/lib/mysql" stuff here is because the mysql-server postinst doesn't
have an explicit way to disable the mysql_install_db codepath besides having a
database already "configured" (ie, stuff in /var/lib/mysql/mysql)  
# also, we set debconf keys to make APT a little quieter  
RUN { \  
echo "mariadb-server-$MARIADB_MAJOR" mysql-server/root_password password
'unused'; \  
echo "mariadb-server-$MARIADB_MAJOR" mysql-server/root_password_again password
'unused'; \  
} | debconf-set-selections \  
&& apt-get update \  
&& apt-get install -y \  
mariadb-server \  
# percona-xtrabackup is installed at the same time so that `mysql-common` is
only installed once from just mariadb repos  
percona-xtrabackup-24 \  
mariadb-backup-$MARIADB_MAJOR \  
socat \  
tzdata \  
pigz \  
p7zip-full \  
liblz4-tool \  
bzip2 \  
&& rm -rf /var/lib/apt/lists/* \  
# comment out any "user" entires in the MySQL config ("docker-entrypoint.sh"
or "--user" will handle user switching)  
&& sed -ri 's/^user\s/#&/' /etc/mysql/my.cnf /etc/mysql/conf.d/* \  
# purge and re-create /var/lib/mysql with appropriate ownership  
&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql /var/run/mysqld \  
&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \  
# ensure that /var/run/mysqld (used for socket and lock files) is writable
regardless of the UID our mysqld instance ends up having at runtime  
&& chmod 777 /var/run/mysqld \  
# comment out a few problematic configuration values  
&& find /etc/mysql/ -name '*.cnf' -print0 \  
| xargs -0 grep -lZE '^(bind-address|log)' \  
| xargs -rt -0 sed -Ei 's/^(bind-address|log)/#&/' \  
# don't reverse lookup hostnames, they are usually another container  
&& echo '[mysqld]\nskip-host-cache\nskip-name-resolve' >
/etc/mysql/conf.d/docker.cnf  
  
VOLUME /var/lib/mysql  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]  

