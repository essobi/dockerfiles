FROM ubuntu:14.04  
  
# Make sure we don't get notifications we can't answer during building.  
env DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get \--yes upgrade  
  
RUN apt-get install nullmailer --no-install-recommends --yes --force-yes && \  
apt-get install cron php5-fpm php5-cli php5-mysql zip unzip php5-mcrypt
php5-gd adduser --yes --force-yes && \  
adduser --system --group fcgi-php --home /var/lib/php5  
  
RUN apt-get -y install nginx  
RUN nginx -V  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
  
# Define mountable directories.  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx", "/var/www/"]  
  
# Define working directory.  
WORKDIR /etc/nginx  
  
# Define default command.  
CMD service php5-fpm start && nginx  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  

