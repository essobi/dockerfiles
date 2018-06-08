FROM php:7.0-apache  
  
RUN apt-get update && apt-get -y install wget tar gcc make \  
libssh2-1-dev libpq-dev libldap2-dev libsnmp-dev libpng-dev libjpeg62-turbo-
dev libfreetype6-dev libldb-dev libxml2-dev locales && \  
sed -i 's/# pt_BR.UTF-8/pt_BR.UTF8/' /etc/locale.gen && \  
locale-gen && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get clean  
  
RUN ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install pgsql xmlrpc ldap bcmath sockets gettext gd  
  
WORKDIR /usr/src  
ARG ZBX_VERSION=3.4.10  
RUN wget
http://ufpr.dl.sourceforge.net/project/zabbix/ZABBIX%20Latest%20Stable/${ZBX_VERSION}/zabbix-${ZBX_VERSION}.tar.gz
&& \  
rm -rf /var/www/html && tar xzvf zabbix-${ZBX_VERSION}.tar.gz && \  
mv /usr/src/zabbix-${ZBX_VERSION}/frontends/php /var/www/html && \  
chown -R www-data:www-data /var/www/html && rm -rf
/usr/src/zabbix-$ZBX_VERSION  
  
EXPOSE 80 443  
WORKDIR /var/www/html  
RUN sed -i 's/5.6/7.2/' include/classes/setup/CFrontendSetup.php  
  
COPY files/default.conf /etc/apache2/sites-available/default.conf  
COPY files/docker-entrypoint.sh /  
COPY files/zabbix.php.ini /usr/local/etc/php/conf.d  
  
ENTRYPOINT /docker-entrypoint.sh  

