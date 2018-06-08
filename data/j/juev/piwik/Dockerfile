FROM nginx  
MAINTAINER Denis Evsyukov  
  
ENV LANG C.UTF-8  
  
RUN apt-get update && apt-get install -y \  
mysql-client \  
php5-fpm \  
php5-mysql \  
php5-gd \  
php5-geoip \  
php-apc \  
curl \  
zip && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/nginx/html/* && \  
rm -rf /etc/nginx/conf.d/* && \  
curl -O "http://builds.piwik.org/piwik.zip" && \  
unzip piwik.zip && cp -R /piwik/* /usr/share/nginx/html && \  
rm -rf piwik piwik.zip && \  
chown -R www-data:www-data /usr/share/nginx/html && chmod -R 0755
/usr/share/nginx/html/tmp && \  
sed -i 's/access_log.*/access_log \/dev\/stdout;/g' /etc/nginx/nginx.conf && \  
sed -i 's/error_log.*/error_log \/dev\/stdout info;/g' /etc/nginx/nginx.conf
&& \  
sed -i 's/^pid/daemon off;\npid/g' /etc/nginx/nginx.conf && \  
sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' /etc/php5/fpm/php.ini && \  
sed -i 's/;always_populate_raw_post_data/always_populate_raw_post_data/g'
/etc/php5/fpm/php.ini  
  
COPY nginx-piwik.conf /etc/nginx/conf.d/nginx-piwik.conf  
COPY basic.conf /etc/nginx/conf.d/basic.conf  
COPY entrypoint.sh /opt/entrypoint.sh  
RUN chmod a+x /opt/entrypoint.sh  
  
ENTRYPOINT ["/opt/entrypoint.sh"]  
  
CMD ["nginx"]  

