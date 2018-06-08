FROM ubuntu:18.04  
MAINTAINER Philipp Hellmich <phil@hellmi.de>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
ENV APACHE_MIN_CHILDS=1 \  
APACHE_MAX_CHILDS=50 \  
APACHE_MIN_CHILDS_SPARE=1 \  
APACHE_MAX_CHILDS_SPARE=5 \  
APACHE_SERVER_NAME=rainloop.loc \  
APACHE_SERVER_ADMIN=webmaster@rainloop.loc \  
PHP_MAX_POST_SIZE=24M \  
PHP_MAX_UPLOAD_SIZE=20M \  
PHP_MAX_UPLOADS=20 \  
PHP_MAX_EXECUTION_ZIME=30 \  
RAINLOOP_PATH=/var/www/html/rainloop \  
RAINLOOP_ADMIN_LOGIN=admin \  
RAINLOOP_ADMIN_PASSWORD=12345  
# Install plugins  
RUN apt-get update && \  
apt-get -y install wget unzip apache2 libapache2-mod-php php-cli php-curl php-
xml php-sqlite3 curl php-ldap && \  
rm -rf /var/lib/apt/lists/*  
  
# init  
RUN wget -q https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-
init_1.2.1_amd64.deb && \  
dpkg -i dumb-init_*.deb && rm dumb-init_*.deb  
  
RUN ln -sf /dev/stdout /var/log/apache2/access.log && \  
ln -sf /dev/stdout /var/log/apache2/other_vhosts_access.log && \  
ln -sf /dev/stderr /var/log/apache2/error.log  
  
# Download latest stable version of Rainloop into /var/www/html  
RUN rm -fr /var/www/html && wget -q
https://www.rainloop.net/repository/owncloud/rainloop.zip \  
-O /tmp/latest.zip && \  
unzip /tmp/latest.zip \  
-d /tmp && \  
mkdir /var/www/html && \  
mkdir ${RAINLOOP_PATH} && \  
mkdir /var/www/html/data && \  
mv /tmp/rainloop/app/rainloop /var/www/html && \  
chown -R www-data.www-data /var/www/html/data && \  
chown -R root.root ${RAINLOOP_PATH} && \  
find ${RAINLOOP_PATH} -type d -exec chmod 755 {} \; && \  
find ${RAINLOOP_PATH} -type f -exec chmod 644 {} \; && \  
rm /tmp/latest.zip  
  
RUN cp ${RAINLOOP_PATH}/v/*/index.php.root /var/www/html/index.php  
  
ADD vhost.conf /etc/apache2/sites-available/000-default.conf  
  
VOLUME ["/var/www/html/data"]  
  
EXPOSE 80  
HEALTHCHECK \--interval=5m --timeout=3s CMD curl -I -s -f http://localhost:80/
|| exit 1  
  
ADD run.sh /run.sh  
ADD adminpass.php /adminpass.php  
RUN chmod 700 /*.sh && chmod 700 /*.php  
  
# Server CMD  
CMD ["dumb-init", "/run.sh"]  

