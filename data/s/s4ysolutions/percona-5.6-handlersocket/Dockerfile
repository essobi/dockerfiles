FROM ubuntu  
MAINTAINER Sergey Dolin <sergey@s4y.solutions>  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
# add gosu for easy step-down from root  
# RUN rm /etc/apt/sources.list.d/nodesource.list  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget lsb-release \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& wget https://repo.percona.com/apt/percona-release_0.1-4.$(lsb_release
-sc)_all.deb \  
&& apt-get purge -y wget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
RUN dpkg -i percona-release_0.1-4.$(lsb_release -sc)_all.deb  
  
# install "pwgen" for randomizing passwords  
# install "apt-transport-https" for Percona's repo (switched to https-only)  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
apt-transport-https \  
pwgen \  
tzdata \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PERCONA_MAJOR 5.6  
# the "/var/lib/mysql" stuff here is because the mysql-server postinst doesn't
have an explicit way to disable the mysql_install_db codepath besides having a
database already "configured" (ie, stuff in /var/lib/mysql/mysql)  
# also, we set debconf keys to make APT a little quieter  
RUN { \  
echo percona-server-server-$PERCONA_MAJOR percona-server-server/root_password
password 'unused'; \  
echo percona-server-server-$PERCONA_MAJOR percona-server-
server/root_password_again password 'unused'; \  
} | debconf-set-selections \  
&& apt-get update \  
&& apt-get install -y ercona-server-server-$PERCONA_MAJOR \  
&& rm -rf /var/lib/apt/lists/* \  
# comment out any "user" entires in the MySQL config ("docker-entrypoint.sh"
or "--user" will handle user switching)  
# && (sed -ri 's/^user\s/#&/' /etc/mysql/my.cnf || true) \  
# purge and re-create /var/lib/mysql with appropriate ownership  
&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql /var/run/mysqld \  
&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \  
# ensure that /var/run/mysqld (used for socket and lock files) is writable
regardless of the UID our mysqld instance ends up having at runtime  
&& chmod 777 /var/run/mysqld  
  
# comment out a few problematic configuration values  
# don't reverse lookup hostnames, they are usually another container  
#RUN \  
# find /etc/mysql/ -name '*.cnf' -print0 \  
# | xargs -0 grep -lZE '^(bind-address|log)' \  
# | xargs -0 sed -Ei 's/^(bind-address|log)/#&/' \  
# && myCnf="$(find /etc/mysql/ -name '*.cnf' -print0 \  
# | xargs -0 grep -lE '^\\[mysqld\\]' \  
# | head -n1)" \  
# && echo 'skip-host-cache\nskip-name-resolve' \  
# | awk '{ print } $1 == "[mysqld]" && c == 0 { c = 1; system("cat") }'
"$myCnf" > /tmp/my.cnf \  
# && mv /tmp/my.cnf "$myCnf"  
VOLUME ["/var/lib/mysql", "/var/log/mysql"]  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
RUN ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat  
COPY misc.cnf /etc/mysql/conf.d/  
COPY handlersocket.cnf /etc/mysql/conf.d/  
COPY enable-handlersocket-plugin.sql /docker-entrypoint-initdb.d  
#COPY sample_create_database.sql /docker-entrypoint-initdb.d  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
  
EXPOSE 3306  
EXPOSE 9999  
CMD ["mysqld"]  

