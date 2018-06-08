FROM php:5.5-apache  
  
RUN apt-get update  
  
# php-mcrypt  
RUN apt-get -y install libmcrypt-dev && docker-php-ext-install mcrypt  
  
# php-intl  
RUN apt-get -y install libicu-dev && docker-php-ext-install intl  
  
# php-imap  
RUN apt-get install -y libc-client-dev libkrb5-dev  
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl  
RUN docker-php-ext-install imap  
  
# Roundcube  
RUN apt-get install -y --no-install-recommends sqlite3  
RUN pear install mail && pear install Net_SMTP && pear install Auth_SASL &&
pear install mail_mime  
  
RUN mkdir /roundcubemail  
ADD
http://downloads.sourceforge.net/project/roundcubemail/roundcubemail/1.1.3/roundcubemail-1.1.3-complete.tar.gz
/  
RUN tar xzf /roundcubemail-*.tar.gz -C /roundcubemail --strip-components 1
--exclude installer && rm /roundcubemail-*.tar.gz  
COPY config/config.inc.php /roundcubemail/config/config.inc.php.template  
RUN chown -R www-data:www-data /roundcubemail  
  
# Apache config  
RUN rm -rf /var/www/html && ln -s /roundcubemail /var/www/html  
RUN sed -e 's#^ErrorLog.*#ErrorLog ${APACHE_LOG_DIR}/error.log#' -i
/etc/apache2/apache2.conf  
RUN sed -e 's#^CustomLog.*#CustomLog ${APACHE_LOG_DIR}/access.log combined#'
-i /etc/apache2/apache2.conf  
  
# Helper scripts  
ADD https://raw.githubusercontent.com/dfrommi/docker-
utils/master/prepare_log.sh /  
ADD https://raw.githubusercontent.com/dfrommi/docker-utils/master/dump_logs.sh
/  
ADD https://raw.githubusercontent.com/dfrommi/docker-
utils/master/filter_template.sh /  
COPY endpoint.sh /  
RUN chmod +x /*.sh  
  
RUN mkdir /data  
RUN chown www-data:www-data /data  
  
VOLUME /data  
  
EXPOSE 80  
ENTRYPOINT ["/endpoint.sh"]  

