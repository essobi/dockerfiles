# vim:set ft=dockerfile:  
FROM ubuntu:14.04  
MAINTAINER Amine Benseddik <amine.benseddik@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Add our user and group first to make sure their IDs get assigned
consistently,  
# regardless of whatever dependencies get added  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
# Install "pwgen" for randomizing passwords, curl, wget and Percona repos list  
RUN apt-get update && apt-get install -y pwgen wget curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget https://repo.percona.com/apt/percona-release_0.1-3.$(lsb_release
-sc)_all.deb \  
&& dpkg -i percona-release_0.1-3.$(lsb_release -sc)_all.deb  
  
ENV PERCONA_MAJOR 5.6  
# The "/var/lib/mysql" stuff here is because the mysql-server postinst doesn't
have an explicit  
# way to disable the mysql_install_db codepath besides having a database
already "configured"  
# (ie, stuff in /var/lib/mysql/mysql)  
# also, we set debconf keys to make APT a little quieter  
RUN { \  
echo percona-server-server-$PERCONA_MAJOR percona-server-server/root_password
password 'unused'; \  
echo percona-server-server-$PERCONA_MAJOR percona-server-
server/root_password_again password 'unused'; \  
} | debconf-set-selections \  
&& apt-get update \  
&& apt-get install -y \  
percona-xtradb-cluster-$PERCONA_MAJOR percona-xtradb-cluster-galera-2.x \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/lib/mysql \  
&& mkdir /var/lib/mysql  
  
# Comment out a few problematic configuration values  
# don't reverse lookup hostnames, they are usually another container  
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf \  
&& echo 'skip-host-cache\nskip-name-resolve' | awk '{ print } $1 == "[mysqld]"
&& c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \  
&& mv /tmp/my.cnf /etc/mysql/my.cnf  
  
# Prepare for Rancher  
# Download giddyup and confd  
RUN mkdir -p /opt/rancher \  
&& curl -SL
https://github.com/cloudnautique/giddyup/releases/download/v0.8.0/giddyup -o
/opt/rancher/giddyup \  
&& chmod +x /opt/rancher/giddyup \  
&& curl -SL
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 -o /opt/rancher/confd \  
&& chmod +x /opt/rancher/confd  
  
# Confd configuration and templates  
COPY ./conf.d /etc/confd/conf.d  
COPY ./templates /etc/confd/templates  
  
# Rancher Entrypoint  
COPY ./start_pxc.sh /opt/rancher  
  
# Volumes  
VOLUME ["/var/lib/mysql", "/var/log/mysql", "/etc/mysql/conf.d"]  
  
# Docker Entrypoint  
RUN mkdir /docker-entrypoint-initdb.d  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# Ports  
EXPOSE 3306 4444 4567 4568  
CMD ["mysqld"]  

