FROM debian:jessie  
MAINTAINER robs@codexsoftware.co.uk  
  
# Using this UID / GID allows local and live file modification of web site  
RUN usermod -u 1000 www-data && groupmod -g 1000 www-data  
  
RUN apt-get update && apt-get install -y \  
cron \  
curl \  
git \  
nginx \  
php5-curl \  
php5-fpm \  
php5-gd \  
php5-mcrypt \  
php5-memcached \  
php5-mysql \  
ssmtp \  
supervisor \  
sudo  
  
# Set up web server.  
ADD nginx-default-server.conf /etc/nginx/sites-available/default  
RUN rm -rf /var/www && mkdir -p /var/www/ssl && mkdir -p /var/www/etc  
ADD certs/* /var/www/ssl/  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Configure PHP  
RUN sed -i "s/memory_limit = 128M/memory_limit = 256M/" /etc/php5/fpm/php.ini  
RUN sed -i "s/;always_populate_raw_post_data =
-1/always_populate_raw_post_data = -1/" /etc/php5/fpm/php.ini  
RUN sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 16M/"
/etc/php5/fpm/php.ini  
  
# Install Magento  
COPY magento-1.9.2.4-2016-02-23-06-04-07.tar.gz /tmp/magento.tar.gz  
RUN tar xzvfC /tmp/magento.tar.gz /tmp/ \  
&& mv /tmp/magento /var/www/htdocs  
  
# Configure Magento  
ADD mage-cache.xml /var/www/htdocs/app/etc/mage-cache.xml  
ADD seturl.php /var/www/htdocs/seturl.php  
RUN sed -i "s/<host>localhost/<host>db/g" /var/www/htdocs/app/etc/config.xml
&& \  
sed -i "s/<username\/>/<username>user<\/username>/"
/var/www/htdocs/app/etc/config.xml && \  
sed -i "s/<password\/>/<password>password<\/password>/g"
/var/www/htdocs/app/etc/config.xml && \  
sed -i -e '/<session_save>{{session_save}}<\/session_save>/{ r
/var/www/htdocs/app/etc/mage-cache.xml' -e 'd}'
/var/www/htdocs/app/etc/local.xml.template && \  
rm /var/www/htdocs/app/etc/mage-cache.xml  
  
# Enable REDIS in Magento  
RUN sed -i "s/<active>false<\/active>/<active>true<\/active>/"
/var/www/htdocs/app/etc/modules/Cm_RedisSession.xml  
  
ADD update.sh /var/www/  
RUN chown -R www-data.www-data /var/www  
  
# Set up cron  
ADD crontab /var/spool/cron/crontabs/www-data  
RUN chown www-data.crontab /var/spool/cron/crontabs/www-data && chmod 0600
/var/spool/cron/crontabs/www-data  
  
# Configure supervisord  
ADD supervisord.conf /etc/supervisor/  
ADD supervisor_conf/* /etc/supervisor/conf.d/  
  
EXPOSE 80  
EXPOSE 443  
VOLUME ["/var/www/"]  
  
ADD docker-entrypoint.sh /root/docker-entrypoint.sh  
ENTRYPOINT ["/root/docker-entrypoint.sh"]

