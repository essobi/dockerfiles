FROM ubuntu:15.04  
MAINTAINER "The Impact Bot" <technology@bcorporation.net>  
  
RUN apt-get update -y && \  
apt-get install cron -y \  
rsyslog \  
php5-cli \  
php5-mcrypt \  
php5-mongo \  
php5-mssql \  
php5-mysqlnd \  
php5-pgsql \  
php5-redis \  
php5-sqlite \  
php5-gd \  
php5-memcached \  
postgresql-client-9.4 \  
supervisor  
  
RUN php5enmod mcrypt  
ADD php.ini /etc/php5/cli/conf.d/impact.ini  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN rm -Rf /etc/cron.daily \  
rm -Rf /etc/cron.weekly \  
rm -Rf /etc/cron.monthly \  
rm -Rf /etc/cron.hourly  
  
RUN mkdir -p /data/www  
VOLUME ["/data"]  
  
COPY crontab /etc/crontab  
COPY logger.sh /bin/logger.sh  
RUN chmod 700 /bin/logger.sh  
RUN crontab -u root /etc/crontab  
  
ADD run.sh /opt/run.sh  
RUN chmod 700 /opt/run.sh  
  
CMD ["/opt/run.sh"]  

