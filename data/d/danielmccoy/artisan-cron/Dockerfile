FROM debian:jessie  
  
MAINTAINER "Daniel McCoy" <danielmccoy@gmail.com>  
  
WORKDIR /tmp  
  
RUN apt-get update -y && \  
apt-get install -y \  
cron \  
pdftk \  
php5-cli \  
php5-mcrypt \  
php5-mssql \  
php5-mysqlnd \  
php5-pgsql \  
php5-redis \  
php5-mongo \  
php5-sqlite \  
php5-dev make php-pear \  
php5-gd && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
#pecl install mongodb && \  
#echo "extension=mongodb.so" >> `php --ini | grep "Loaded Configuration" | sed
-e "s|.*:\s*||"`  
RUN mkdir -p /var/www  
VOLUME ["/var/www"]  
WORKDIR /var/www  
  
# Add crontab file in the cron directory  
ADD crontab /etc/cron.d/hello-cron  
  
# Give execution rights on the cron job  
RUN chmod 0644 /etc/cron.d/hello-cron  
  
# Create the log file to be able to run tail  
RUN touch /var/log/cron.log  
  
# Run the command on container startup  
CMD cron && tail -f /var/log/cron.log  

