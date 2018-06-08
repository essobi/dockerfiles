# vim:set ft=dockerfile:  
FROM aggr/ubuntu  
  
MAINTAINER Mikhail Baykov <mike@baikov.com>  
  
ENV PERCONA_MAJOR 5.7  
ENV PERCONA_VERSION 5.7.17-13-1.trusty  
  
# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.  
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
RUN cd /tmp && wget https://repo.percona.com/apt/percona-
release_0.1-4.$(lsb_release -sc)_all.deb && dpkg -i percona-
release_0.1-4.$(lsb_release -sc)_all.deb && rm -f /tmp/percona-release*  
  
# install "pwgen" for randomizing passwords  
RUN apt-get -qq update && apt-get install -qqy pwgen && rm -rf
/var/lib/apt/lists/*  
  
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
&& apt-get -qq update && DEBIAN_FRONTEND=noninteractive \  
&& apt-get install -qqy percona-server-server-$PERCONA_MAJOR=$PERCONA_VERSION
\  
&& rm -rf /etc/mysql/percona-server.conf.d/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/lib/mysql/*  
  
RUN mkdir /docker-entrypoint-initdb.d  
VOLUME ["/var/lib/mysql", "/var/log/mysql", "/etc/mysql"]  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]  

