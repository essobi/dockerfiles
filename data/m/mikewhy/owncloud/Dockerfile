FROM debian:jessie  
  
RUN sed -i 's/httpredir/http.us/g' /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y curl cron bzip2 smbclient nginx supervisor libav-tools
libreoffice-writer \  
php5-cli php5-gd php5-pgsql php5-sqlite php5-mysqlnd php5-curl php5-intl \  
php5-mcrypt php5-ldap php5-gmp php5-apcu php5-imagick php5-fpm \  
&& apt-get clean \  
&& apt-get autoclean \  
&& apt-get autoremove  
  
ENV OWNCLOUD_VERSION=8.2.0  
RUN curl -L
https://download.owncloud.org/community/owncloud-${OWNCLOUD_VERSION}.tar.bz2 |
tar -xj -C /var/www  
  
RUN mkdir /docker-entrypoint.d /var/www/owncloud/user-apps /var/log/owncloud  
RUN chown www-data:www-data /var/log/owncloud  
RUN sed -E -i 's|error_log = .*|error_log = /var/log/owncloud/php5-fpm.log|'
/etc/php5/fpm/php-fpm.conf  
  
COPY data/docker-entrypoint /docker-entrypoint  
COPY data/supervisord.conf /etc/supervisor/conf.d/owncloud.conf  
COPY data/nginx.conf /etc/nginx/nginx.conf  
COPY data/cron /tmp/owncloud-cron  
COPY data/occ /usr/local/bin/occ  
#RUN crontab -u www-data /tmp/owncloud-cron && rm /tmp/owncloud-cron  
RUN su -s /bin/sh www-data -c "crontab /tmp/owncloud-cron"  
  
ENV MAX_UPLOAD_SIZE=30G  
VOLUME /var/www/owncloud/config  
VOLUME /var/www/owncloud/data  
VOLUME /var/www/owncloud/apps  
VOLUME /var/www/owncloud/assets  
VOLUME /var/log/owncloud  
WORKDIR /var/www/owncloud  
  
#RUN chown -R www-data:www-data /var/www/owncloud  
EXPOSE 80  
ENTRYPOINT ["/docker-entrypoint"]  
CMD ["supervisord", "--nodaemon", "-c", "/etc/supervisor/supervisord.conf"]  

