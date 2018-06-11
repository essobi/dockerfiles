FROM debian:jessie  
  
LABEL maintainer "j.zelger@techdivision.com"  
  
# copy all filesystem relevant files  
COPY fs /tmp/  
  
# start install routine  
RUN \  
# install base tools  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \--force-yes --no-install-
recommends \  
vim tar wget curl apt-transport-https ca-certificates net-tools htop python-
pip && \  
  
# copy repository files  
cp -r /tmp/etc/apt /etc && \  
  
# add repository keys  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys EEA14886 && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys 5072E1F5 && \  
curl https://nginx.org/keys/nginx_signing.key | apt-key add \- && \  
curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add \- && \  
curl https://www.dotdeb.org/dotdeb.gpg | apt-key add \- && \  
curl https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | apt-key add
\- && \  
curl https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add \- && \  
  
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
  
# install ...  
DEBIAN_FRONTEND=noninteractive apt-get install -y \--force-yes --no-install-
recommends \  
# general tools  
openssl rsync git graphicsmagick postfix \  
# oracle java 8  
oracle-java8-installer oracle-java8-set-default \  
# mysql 5.7  
mysql-community-client mysql-community-server \  
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
php7.0 php7.0-common php7.0-fpm php7.0-curl php7.0-gd php7.0-mcrypt
php7.0-mysql php7.0-soap \  
php7.0-json php7.0-zip php7.0-intl php7.0-bcmath php7.0-xsl php7.0-xml
php7.0-mbstring php7.0-xdebug \  
php7.0-mongodb php7.0-ldap && \  
  
# copy filesystem  
cp -r /tmp/usr / && \  
cp -r /tmp/etc / && \  
  
# cleanup  
apt-get clean && \  
rm -rf /tmp/* /var/lib/apt/lists/*  
  
# define cmd  
CMD ["/usr/local/bin/supervisord", "--nodaemon", "-c",
"/etc/supervisord.conf"]

