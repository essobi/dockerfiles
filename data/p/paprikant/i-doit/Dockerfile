FROM ubuntu:16.04  
MAINTAINER thereal.paprikant@gmail.com  
  
# Use this ARG to build diffrent versions  
ARG IDOIT_VERSION="1.10"  
ARG MARIADB_HOSTNAME="localhost"  
ARG APACHE_USER="www-data"  
ARG APACHE_GROUP="www-data"  
ARG INSTALL_DIR="/var/www/html"  
# Tenant, user, and database settings  
ARG IDOIT_ADMINCENTER_PASSWORD="admin"  
ARG MARIADB_SUPERUSER_PASSWORD="password"  
ARG MARIADB_IDOIT_USERNAME="idoit"  
ARG MARIADB_IDOIT_PASSWORD="idoit"  
ARG IDOIT_TENANT="CMDB"  
# Make them avaliable as env  
ENV IDOIT_ADMINCENTER_PASSWORD $IDOIT_ADMINCENTER_PASSWORD  
ENV MARIADB_SUPERUSER_PASSWORD $MARIADB_SUPERUSER_PASSWORD  
ENV MARIADB_IDOIT_USERNAME $MARIADB_IDOIT_USERNAME  
ENV MARIADB_IDOIT_PASSWORD $MARIADB_IDOIT_PASSWORD  
ENV IDOIT_TENANT $IDOIT_TENANT  
ENV INSTALL_DIR $INSTALL_DIR  
  
# Update ubuntu  
RUN \  
apt-get -qq --yes update &&\  
apt-get -qq --yes full-upgrade &&\  
apt-get -qq --yes clean &&\  
apt-get -qq --yes autoremove  
  
# Install requirements  
RUN \  
apt-get -qq --yes install \  
apache2 libapache2-mod-php \  
mariadb-client mariadb-server \  
php php-bcmath php-cli php-common php-curl php-gd php-imagick php-json php-
ldap php-mcrypt \  
php-memcached php-mysql php-pgsql php-soap php-xml php-zip \  
memcached unzip sudo moreutils wget &&\  
apt-get clean  
  
# Provide config  
COPY idoit-php-conf /etc/php/7.0/mods-available/i-doit.ini  
  
RUN \  
phpenmod i-doit &&\  
phpenmod memcached  
  
COPY idoit-apache-conf /etc/apache2/sites-available/i-doit.conf  
  
RUN \  
a2dissite 000-default &&\  
sed -i "s;INSTALL_DIR;${INSTALL_DIR};g" /etc/apache2/sites-
available/i-doit.conf &&\  
sed -i "s;APACHE_LOG_DIR;${APACHE_LOG_DIR};g" /etc/apache2/sites-
available/i-doit.conf &&\  
a2ensite i-doit &&\  
a2enmod rewrite  
  
# Get dockerize  
ENV DOCKERIZE_VERSION v0.6.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
EXPOSE 80  
RUN \  
mkdir /var/run/mysqld/ &&\  
chown mysql.mysql /var/run/mysqld/  
  
RUN \  
wget "https://login.i-doit.com/downloads/idoit-${IDOIT_VERSION}.zip" &&\  
cd "$INSTALL_DIR" &&\  
unzip /idoit-${IDOIT_VERSION}.zip &&\  
rm -f /idoit-${IDOIT_VERSION}.zip  
  
RUN \  
chown "${APACHE_USER}":"${APACHE_GROUP}" -R "${INSTALL_DIR}/" &&\  
rm $INSTALL_DIR/index.html  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  

