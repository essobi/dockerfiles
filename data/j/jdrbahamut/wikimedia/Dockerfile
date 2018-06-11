FROM nginx  
MAINTAINER Michael DOHR "jdrbahamut@gmail.com"  
# Mediawiki version.  
ARG MEDIAWIKI_MAJOR=1.27  
ARG MEDIAWIKI_MINOR=1  
# PHP Installation.  
RUN apt-get update -y && \  
apt-get install -y curl && \  
apt-get install -y php5-fpm php5-intl php-apc php5-gd php5-intl php5-mysqlnd
php5-pgsql php-pear php5-cli php5-curl && \  
rm -rf /var/lib/apt/lists/* && \  
# Once we start using PHP, it will dictate the use of www-data, so use that
instead of nginx  
sed -i 's/user nginx/user www-data/g' /etc/nginx/nginx.conf && \  
# Force PHP to log to nginx  
echo "catch_workers_output = yes" >> /etc/php5/fpm/php-fpm.conf  
  
# Enable php by default  
ADD default.conf /etc/nginx/conf.d/default.conf  
  
ENV NGINX_HTML="/usr/share/nginx/html"  
# Wikimedia install.  
RUN curl --silent --location --retry 3 \  
http://releases.wikimedia.org/mediawiki/${MEDIAWIKI_MAJOR}/mediawiki-${MEDIAWIKI_MAJOR}.${MEDIAWIKI_MINOR}.tar.gz
\  
| tar xz -C /tmp && \  
rm -rf ${NGINX_HTML}/* && \  
mv /tmp/mediawiki-${MEDIAWIKI_MAJOR}.${MEDIAWIKI_MINOR}/* ${NGINX_HTML}/ && \  
rm -rf /tmp/mediawiki* && \  
chown -R www-data:www-data ${NGINX_HTML}/ && \  
rm -rf /usr/share/nginx/html/images  
  
VOLUME ["/usr/share/nginx/html/images"]  
  
# Add the start script  
ADD start.sh /bin/start.sh  
  
CMD chmod +x /bin/start.sh && /bin/start.sh  

