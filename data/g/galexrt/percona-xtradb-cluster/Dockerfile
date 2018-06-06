FROM debian:jessie  
LABEL maintainer="Alexander Trost aka <galexrt@googlemail.com>"  
  
ENV PERCONA_MAJOR="5.7" PERCONA_VERSION="5.7.16-27.19-1.jessie"
JQ_VERSION="1.5" JQ_ARCH="linux64" DEBIAN_FRONTEND="noninteractive"  
RUN groupadd -r mysql && useradd -r -g mysql mysql && \  
apt-get update && \  
apt-get -q upgrade -y && \  
apt-get install -y --no-install-recommends \  
apt-transport-https ca-certificates pwgen curl socat && \  
curl -sLo /usr/bin/jq
"https://github.com/stedolan/jq/releases/download/jq-$JQ_VERSION/jq-$JQ_ARCH"
&& \  
chmod 755 /usr/bin/jq && \  
curl -so percona-release.deb https://repo.percona.com/apt/percona-
release_0.1-4.jessie_all.deb && \  
dpkg -i percona-release.deb && \  
rm percona-release.deb && \  
# also, we set debconf keys to make APT a little quieter  
apt-get update && \  
{ \  
echo "percona-server-server-${PERCONA_MAJOR}" percona-server-server/datadir
select ''; \  
echo "percona-server-server-${PERCONA_MAJOR}" percona-server-
server/root_password password ''; \  
} | debconf-set-selections && \  
apt-get install -y --force-yes percona-xtradb-cluster-57 && \  
rm -rf /var/lib/apt/lists/* && \  
# purge and re-create /var/lib/mysql with appropriate ownership  
rm -rf /var/lib/mysql /var/lib/mysql-files && mkdir -p /var/lib/mysql
/var/lib/mysql-files /var/run/mysqld && \  
chown -R mysql:mysql /var/lib/mysql /var/lib/mysql-files /var/run/mysqld && \  
# ensure that /var/run/mysqld (used for socket and lock files) is writable
regardless of the UID our mysqld instance ends up having at runtime  
chmod 777 /var/run/mysqld && \  
# comment out a few problematic configuration values  
# don't reverse lookup hostnames, they are usually another container  
sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf && \  
# comment out any "user" entires in the MySQL config ("docker-entrypoint.sh"
or "--user" will handle user switching)  
sed -ri 's/^user.*/user = mysql/' /etc/mysql/my.cnf && \  
echo 'skip-host-cache\nskip-name-resolve' | awk '{ print } $1 == "[mysqld]" &&
c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf && \  
mv /tmp/my.cnf /etc/mysql/my.cnf && \  
sed -Ei '/log-error/s/^/#/g' -i /etc/mysql/my.cnf && \  
mkdir -p /etc/mysql/certs  
  
COPY clustercheckcron /usr/bin/clustercheckcron  
COPY general.cnf /etc/mysql/conf.d/general.cnf  
COPY logging.cnf /etc/mysql/conf.d/logging.cnf  
COPY client.cnf /etc/mysql/conf.d/client.cnf  
COPY entrypoint.sh /entrypoint.sh  
  
EXPOSE 3306 4567 4568  
VOLUME ["/var/lib/mysql", "/var/log/mysql"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/sbin/mysqld"]  

