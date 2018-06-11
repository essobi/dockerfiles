FROM debian:8.7  
  
LABEL maintainer "j.zelger@techdivision.com"  
# copy all filesystem relevant files  
COPY fs /tmp/  
# start install routine  
RUN \  
# install base tools  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes \--no-install-
recommends \  
vim less tar wget curl apt-transport-https ca-certificates apt-utils net-tools
htop python-pip pv && \  
# copy repository files  
cp -r /tmp/etc/apt /etc && \  
# add repository keys  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 5072E1F5 && \  
curl https://nginx.org/keys/nginx_signing.key | apt-key add - && \  
curl https://www.dotdeb.org/dotdeb.gpg | apt-key add - && \  
curl https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | apt-key add -
&& \  
curl https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add - && \  
# update repositories  
apt-get update && \  
# define deb selection configurations  
echo postfix postfix/mailname string dnmp | debconf-set-selections && \  
echo postfix postfix/main_mailer_type string 'Internet Site' | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
# prepare compatibilities for docker  
dpkg-divert --rename /usr/lib/sysctl.d/elasticsearch.conf && \  
# install supervisor  
pip2 install supervisor && \  
pip2 install supervisor-stdout && \  
# add our user and group first to make sure their IDs get assigned
consistently,  
# regardless of whatever dependencies get added  
groupadd -r mysql && useradd -r -g mysql mysql && \  
# install packages  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes \--no-install-
recommends \  
# general tools  
openssl rsync git graphicsmagick imagemagick ghostscript ack-grep postfix \  
# oracle java 8  
oracle-java8-installer oracle-java8-set-default \  
# nginx  
nginx \  
# varnish  
varnish \  
# redis  
redis-server \  
# rabbitmq  
rabbitmq-server \  
# elasticsearch  
elasticsearch \  
# php 7.0  
php7.0 php7.0-cli php7.0-common php7.0-fpm php7.0-curl php7.0-gd php7.0-mcrypt
php7.0-mysql php7.0-soap \  
php7.0-json php7.0-zip php7.0-intl php7.0-bcmath php7.0-xsl php7.0-xml
php7.0-mbstring php7.0-xdebug \  
php7.0-mongodb php7.0-ldap php7.0-imagick php7.0-readline && \  
# mysql 5.7  
{ \  
echo mysql-community-server mysql-community-server/data-dir select ''; \  
echo mysql-community-server mysql-community-server/root-pass password ''; \  
echo mysql-community-server mysql-community-server/re-root-pass password ''; \  
echo mysql-community-server mysql-community-server/remove-test-db select
false; \  
} | debconf-set-selections && \  
apt-get install -y mysql-community-client mysql-community-server && \  
mkdir -p /var/lib/mysql /var/run/mysqld && \  
mysql_ssl_rsa_setup && \  
chown -R mysql:mysql /var/lib/mysql /var/run/mysqld && \  
# ensure that /var/run/mysqld (used for socket and lock files) is writable
regardless of the UID our mysqld instance ends up having at runtime  
chmod 777 /var/run/mysqld && \  
# comment out a few problematic configuration values for docker usage  
find /etc/mysql/ -name '*.cnf' -print0 \  
| xargs -0 grep -lZE '^(bind-address|log)' \  
| xargs -rt -0 sed -Ei 's/^(bind-address|log)/#&/' && \  
# don't reverse lookup hostnames for docker usage  
echo '[mysqld]\nskip-host-cache\nskip-name-resolve' >
/etc/mysql/conf.d/docker.cnf && \  
# install elasticsearch plugins  
/usr/share/elasticsearch/bin/plugin install analysis-phonetic && \  
/usr/share/elasticsearch/bin/plugin install analysis-icu && \  
# copy filesystem  
cp -r /tmp/usr / && \  
cp -r /tmp/etc / && \  
# setup filepermissions  
chmod a+x /usr/local/bin/docker-entrypoint.sh && \  
# cleanup  
apt-get clean && \  
rm -rf /tmp/* /var/lib/apt/lists/*  
  
# define entrypoint  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
# define cmd  
CMD ["supervisord", "--nodaemon", "-c", "/etc/supervisord.conf"]

