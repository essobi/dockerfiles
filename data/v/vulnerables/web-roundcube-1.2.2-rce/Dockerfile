FROM debian:jessie  
  
LABEL maintainer "opsxcq@strm.sh"  
  
# This is a megazord image for this vulnerability only, don't think that it's
a good pratice do it like that  
RUN apt-get update && \  
apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
nginx php5-fpm nano wget sqlite3 procps \  
php5-mcrypt php5-intl php5-sqlite php-pear \  
php-net-smtp php-mail-mime \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY nginx.roundcube.conf /etc/nginx/sites-enabled/default  
  
COPY config.inc.php /usr/share/nginx/www/config/  
  
RUN systemctl enable php5-fpm nginx  
  
EXPOSE 80  
VOLUME /data  
  
COPY main.sh /  
ENTRYPOINT ["/main.sh"]  
CMD ["default"]  
  

