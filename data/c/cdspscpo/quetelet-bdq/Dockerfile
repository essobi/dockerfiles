FROM helder/php-5.3  
RUN apt-get update \  
&& apt-get install libmcrypt-dev libpng12-0-dev libcurl4-gnutls-dev libpspell-
dev libxslt-dev --no-install-recommends -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install mcrypt gd curl pspell xsl pdo_mysql  
  
RUN sed -i s'/listen = 127.0.0.1:9000/listen = 9000/' /usr/local/etc/php-
fpm.d/www.conf  
RUN echo "php_admin_flag[log_errors] = on" >> /usr/local/etc/php-
fpm.d/www.conf  
RUN echo "date.timezone = \"Europe/Paris\"" >
/usr/local/etc/php/conf.d/timezone.ini  
  
ADD app /app/  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN chmod +x /docker-entrypoint.sh  
  
VOLUME /app/  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

