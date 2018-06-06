FROM hacklab/php  
MAINTAINER Fabio Montefuscolo <fabio.montefuscolo@gmail.com>  
  
WORKDIR /var/www/html/  
  
RUN apt-get update && apt-get install -y libldb-dev libldap2-dev \  
&& ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so \  
&& ln -s /usr/lib/x86_64-linux-gnu/liblber.so /usr/lib/liblber.so \  
&& docker-php-ext-install ldap mysql pdo_mysql \  
&& echo "extension=ldap.so" > /usr/local/etc/php/conf.d/docker-php-ext-
ldap.ini \  
&& curl -o tiki-wiki.tar.gz
'https://ufpr.dl.sourceforge.net/project/tikiwiki/Tiki_18.x_Alcyone/18.1/tiki-18.1.tar.gz'
\  
&& tar -C /var/www/html -zxvf tiki-wiki.tar.gz --strip 1 \  
&& rm tiki-wiki.tar.gz \  
&& { \  
echo "<?php"; \  
echo " \$db_tiki = getenv('TIKI_DB_DRIVER') ?: 'mysqli';"; \  
echo " \$dbversion_tiki = getenv('TIKI_DB_VERSION') ?: '18';"; \  
echo " \$host_tiki = getenv('TIKI_DB_HOST') ?: 'db';"; \  
echo " \$user_tiki = getenv('TIKI_DB_USER');"; \  
echo " \$pass_tiki = getenv('TIKI_DB_PASS');"; \  
echo " \$dbs_tiki = getenv('TIKI_DB_NAME') ?: 'tikiwiki';"; \  
echo " \$client_charset = 'utf8';"; \  
} > /var/www/html/db/local.php \  
&& /bin/bash htaccess.sh \  
&& chown -R root:root /var \  
&& find /var/www/html -type f -exec chmod 644 {} \; \  
&& find /var/www/html -type d -exec chmod 755 {} \; \  
&& chown -R www-data /var/www/html/db/ \  
&& chown -R www-data /var/www/html/dump/ \  
&& chown -R www-data /var/www/html/img/trackers/ \  
&& chown -R www-data /var/www/html/img/wiki/ \  
&& chown -R www-data /var/www/html/img/wiki_up/ \  
&& chown -R www-data /var/www/html/modules/cache/ \  
&& chown -R www-data /var/www/html/temp/ \  
&& chown -R www-data /var/www/html/temp/cache/ \  
&& chown -R www-data /var/www/html/temp/templates_c/ \  
&& chown -R www-data /var/www/html/templates/ \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  
  
  
VOLUME [ \  
"/var/www/html/files/", \  
"/var/www/html/img/wiki/", \  
"/var/www/html/img/wiki_up/", \  
"/var/www/html/img/trackers/" \  
]  
  
EXPOSE 80 443  
CMD ["apache2-foreground"]  

