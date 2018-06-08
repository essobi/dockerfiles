FROM ubuntu  
  
MAINTAINER Johannes <johannes@number13.de>  
  
RUN apt-get -qq update  
RUN apt-get install -qq \  
nginx \  
ca-certificates \  
php-fpm php-mysql php-xml php-mbstring php-intl php-ldap \  
wget \  
cron \  
dovecot-core mysql-client  
  
RUN echo "cgi.fix_pathinfo=0" >> /etc/php/7.0/fpm/php.ini  
RUN echo "extension=php_intl.dll" >> /etc/php/7.0/fpm/php.ini  
  
#add files  
ADD run.sh run.sh  
ADD default default  
ADD password password  
ADD config.inc.php config.inc.php  
  
#get roundmail  
RUN wget
https://github.com/roundcube/roundcubemail/releases/download/1.2.3/roundcubemail-1.2.3-complete.tar.gz  
RUN tar xfz roundcubemail-1.2.3-complete.tar.gz  
RUN rm roundcubemail-1.2.3-complete.tar.gz  
RUN rm -rf /var/www/html  
RUN cp -R roundcubemail-1.2.3 /var/www/html  
RUN rm -rf /var/www/html/installer  
  
#some chmod and chown  
RUN chmod +x run.sh  
RUN chmod -R g+w /var/www/html  
RUN chown -R www-data:www-data /var/www  
  
#install cronjob  
RUN touch mycron  
RUN echo "@daily /var/www/html/bin/cleandb.sh"  
RUN crontab mycron  
RUN rm mycron  
  
#expose ports  
EXPOSE 80 443  
CMD ["./run.sh"]

