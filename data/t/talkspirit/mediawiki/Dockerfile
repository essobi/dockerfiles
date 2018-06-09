FROM debian:7.11  
RUN apt-get update && apt-get install aptitude apache2 libapache2-mod-php5
php5-mysql php-apc php5-curl php5-gd php5-mcrypt php5-memcache php5-pspell
php5-dev php5-sqlite php5-tidy php5-xmlrpc gettext vim make ssmtp locales cron
php-pear libcurl3-dev libxml2-dev libpcre3-dev -y  
  
RUN apt-get install iputils-ping -y  
  
RUN apt-get install mediawiki mediawiki-extensions mediawiki-extensions-
collection mediawiki-extensions-geshi mediawiki-extensions-graphviz mediawiki-
extensions-ldapauth mediawiki-extensions-math mediawiki-extensions-openid
mediawiki-math mediawiki-math-texvc -y  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
# PHP  
RUN sed -i -e "s/expose_php = On/expose_php = Off/g" /etc/php5/apache2/php.ini  
  
# mail  
RUN echo "sendmail_path = /usr/sbin/ssmtp -t" > /etc/php5/mods-
available/sendmail.ini  
RUN php5enmod sendmail  
  
RUN sed -i -e 's/mailhub=mail/mailhub=exim4/' /etc/ssmtp/ssmtp.conf  
RUN sed -i -e 's/#FromLineOverride=YES/FromLineOverride=YES/'
/etc/ssmtp/ssmtp.conf  
RUN sed -i -e 's/root=postmaster/root=/' /etc/ssmtp/ssmtp.conf  
  
RUN sed -i -e "s/upload_max_filesize = 2M/upload_max_filesize = 20M/g"
/etc/php5/apache2/php.ini  
RUN sed -i -e "s/post_max_size = 8M/post_max_size = 20M/g"
/etc/php5/apache2/php.ini  
  
RUN sed -i -e "s/ServerTokens OS/ServerTokens prod/g"
/etc/apache2/conf.d/security  
  
Run sed -i -e "s/ErrorLog \${APACHE_LOG_DIR}\/error.log/ErrorLog
\/dev\/null/g" /etc/apache2/apache2.conf  
  
RUN sed -i -e "s/# fr_FR.UTF-8/fr_FR.UTF-8/g" /etc/locale.gen  
RUN sed -i -e "s/# en_US.UTF-8/en_US.UTF-8/g" /etc/locale.gen  
  
RUN locale-gen  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Enable apache mods.  
RUN a2enmod rewrite  
RUN a2enmod headers  
RUN a2enmod expires  
  
RUN rm /etc/apache2/sites-enabled/000-default  
  
RUN chown www-data.www-data /var/www/ -Rf  
  
# forward request and error logs to docker log collector  
RUN ln -sf /proc/1/fd/1 $APACHE_LOG_DIR/access.log \  
&& ln -sf /proc/1/fd/1 $APACHE_LOG_DIR/error.log \  
&& ln -sf /proc/1/fd/1 "$APACHE_LOG_DIR/other_vhosts_access.log"  
  
WORKDIR /var/www/  
  
EXPOSE 80  
RUN usermod -u 33 www-data  
RUN groupmod -g 33 www-data  
  
CMD ["apache2ctl", "-D", "FOREGROUND"]  

