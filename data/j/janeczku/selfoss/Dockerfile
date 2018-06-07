FROM million12/nginx-php:php-55  
MAINTAINER Jan Broer <janeczku@yahoo.de>  
  
RUN \  
yum update -y && \  
yum install -y cronie php-gd php-sqlite && \  
yum clean all  
  
ADD container-files /  
  
# Give execution rights on the cron jobs  
RUN chmod 0644 /etc/cron.d/*  
  
# Get release 2.13 from the side  
ADD
https://github.com/SSilence/selfoss/releases/download/2.13/selfoss-2.13.zip
/tmp/selfoss-2.13.zip  
RUN mkdir -p /var/www/default && unzip /tmp/selfoss-*.zip -d /var/www/default
&& rm /tmp/selfoss-*.zip  
  
# Patch base URL method to work with docker port mapping  
ADD patches/helpers/View.php /var/www/default/helpers/View.php  
  
# Prepare  
RUN \  
chmod +rwx /var/www/default/data/cache && \  
chmod +rwx /var/www/default/data/favicons && \  
chmod +rwx /var/www/default/data/logs && \  
chmod +rwx /var/www/default/data/thumbnails && \  
chmod +rwx /var/www/default/data/sqlite && \  
chmod +rwx /var/www/default/public && \  
chmod +rwx /var/www/default/index.php && \  
cp /var/www/default/defaults.ini /var/www/default/config.ini && \  
chown -R www:www /var/www/default && \  
chmod 644 /var/www/default/helpers/View.php && \  
mv /etc/nginx/conf.d/default-10-expires.conf
/etc/nginx/conf.d/default-10-expires.conf.bak  
  
USER www  
RUN /usr/bin/php /var/www/default/update.php  
USER root  

