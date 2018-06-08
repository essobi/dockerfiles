FROM clouder/clouder-nginx  
MAINTAINER Yannick Buron yburon@goclouder.net  
  
RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get -y -qq
install php-mysql php-apcu php-fpm php-curl php-gd php-intl php-pear php-imap
php-memcache memcached mc mysql-client git curl php-mcrypt php-zip  
  
# php-fpm config  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.0/fpm/php-
fpm.conf  
RUN find /etc/php/7.0/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \;  
  
RUN echo "" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "[program:php-fpm]" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "command=/usr/sbin/php-fpm7.0 -c /etc/php/7.0/fpm" >>
/etc/supervisor/conf.d/supervisord.conf  
  
RUN echo "" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "[program:memcached]" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "command=/usr/bin/memcached -p 11211 -u www-data -m 64 -c 1024 -t 4"
>> /etc/supervisor/conf.d/supervisord.conf  
  
RUN curl -s https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
RUN phpenmod mcrypt  
RUN phpenmod imap  
RUN phpenmod zip  
  
# You need to add  
# $_SERVER['HTTPS']='on';  
# in wp-config.php after install to use https
http://codex.wordpress.org/Administration_Over_SSL  
RUN mkdir /base-backup  
RUN chown -R www-data /base-backup  
VOLUME /base-backup  

