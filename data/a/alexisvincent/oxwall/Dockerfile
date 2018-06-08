FROM alexisvincent/nginx.php:5.6.7  
MAINTAINER <alexisjohnvincent@gmail.com>  
  
# Install.  
RUN \  
apt-get update && \  
apt-get install -y php5-mysql php5-gd php5-curl libfreetype6 cron sendmail-bin
&& \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY container/php.ini /etc/php5/fpm/php.ini  
COPY container/default.conf /etc/nginx/conf.d/default.conf  
COPY container/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
COPY container/cron.sh /data/cron.sh  
RUN chmod o+x /data/cron.sh  
  
RUN rm -rf /data/www/*

