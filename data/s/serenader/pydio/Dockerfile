FROM nginx:1.11.4  
MAINTAINER serenader xyslive@gmail.com  
ENV PYDIO_VERSION 7.0.3  
ENV APTLIST="acl bzip2 imagemagick ghostscript git gzip openssl libsqlite3-dev
libssh2-php memcached php5-cli \  
php5-curl php5-fpm php5-dev php5-gd php5-imagick php5-imap php5-mcrypt
php5-memcached php-pear php5-ldap php-mail-mimedecode \  
php5-mysql php5-pgsql php5-pspell php5-snmp php5-sqlite php5-xmlrpc rsync
snmp-mibs-downloader sqlite3 ssmtp \  
subversion tar unzip wget mysql-server mysql-client php-apc"  
RUN echo 'deb http://httpredir.debian.org/debian jessie main contrib non-free'
>> /etc/apt/sources.list \  
&& apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -yq
$APTLIST \  
&& apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& sed -i -e "s/output_buffering\s*=\s*4096/output_buffering = Off/g"
/etc/php5/fpm/php.ini \  
&& sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php5/fpm/php.ini \  
&& sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 20G/g"
/etc/php5/fpm/php.ini \  
&& sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 20G/g"
/etc/php5/fpm/php.ini \  
&& mkdir /var/www/ && chown www-data:www-data /var/www \  
&& pear channel-update pear.php.net \  
&& pear channel-update pecl.php.net \  
&& pear config-set preferred_state alpha \  
&& pear install VersionControl_Git \  
&& pear config-set preferred_state stable \  
&& pear install HTTP_WebDAV_Client \  
&& pear install channel://pear.php.net/HTTP_OAuth-0.3.1 \  
&& pecl install imagick \  
&& pear config-set auto_discover 1 \  
&& pear channel-discover pear.amazonwebservices.com \  
&& pear install PEAR \  
&& pear install aws/sdk \  
&& pear install HTTP_OAuth \  
&& pear install Mail_mimeDecode \  
&& php5enmod mcrypt imap \  
&& rm /etc/ssmtp/ssmtp.conf \  
&& mv /usr/sbin/sendmail /usr/sbin/sendmail.org \  
&& ln -s /usr/sbin/ssmtp /usr/sbin/sendmail  
  
COPY nginx.conf /etc/nginx/nginx.conf  
WORKDIR /var/www  
RUN wget -q https://download.pydio.com/pub/core/archives/pydio-
core-${PYDIO_VERSION}.zip \  
&& unzip -q pydio-core-${PYDIO_VERSION}.zip && mv pydio-core-${PYDIO_VERSION}
pydio-core \  
&& rm pydio-core-${PYDIO_VERSION}.zip  
  
ADD ./bootstrap.json /var/www/pydio-core/data/plugins/boot.conf/bootstrap.json  
ADD ./data /var/www/data  
ADD ./start.sh /var/www/start.sh  
  
RUN chown -R www-data:www-data /var/www/pydio-core && chmod -R 770
/var/www/pydio-core \  
&& chmod 777 /var/www/pydio-core/data/files/ \  
&& chmod 777 /var/www/pydio-core/data/personal/ \  
&& mysql_install_db --user=mysql --basedir=/usr/ --ldata=/var/lib/mysql/ \  
&& service mysql start \  
&& mysql -uroot -e "SET PASSWORD FOR 'root'@'localhost' =
PASSWORD('pydiomysqlpwd');;" \  
&& service php5-fpm start  
  
EXPOSE 80  
VOLUME /var/www/pydio-core/data/files/  
VOLUME /var/www/pydio-core/data/personal/  
VOLUME /var/lib/mysql  
  
CMD ["/bin/bash", "/var/www/start.sh"]  

