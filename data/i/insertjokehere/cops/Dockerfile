FROM ubuntu:14.04  
ENV COPS_VERSION 1.0.0  
RUN apt-get update && apt-get install -y \  
wget unzip nginx php5-fpm supervisor php5-gd php5-sqlite \  
php5-intl  
  
RUN mkdir -p /var/www/cops & \  
cd /usr/local/src && \  
wget
https://github.com/seblucas/cops/releases/download/${COPS_VERSION}/cops-${COPS_VERSION}.zip
&& \  
unzip cops-${COPS_VERSION}.zip -d /var/www/cops && \  
rm /usr/local/src/cops-${COPS_VERSION}.zip  
  
COPY config_local.php /var/www/cops  
  
RUN chown -R www-data:www-data /var/www  
  
RUN mkdir /tmp/metadata && chown www-data:www-data /tmp/metadata  
  
COPY cops.conf /etc/nginx/sites-enabled/default  
  
EXPOSE 80  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
CMD supervisord -c /etc/supervisor/conf.d/supervisord.conf  

