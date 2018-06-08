FROM nginx:latest  
MAINTAINER Mathias Schuepany <mathias@schuepany.at>  
  
EXPOSE 80  
ENV VERSION 1.1.0  
RUN apt-get update && \  
apt-get install -y --no-install-recommends wget php5-fpm php5-mysql
php5-pspell php5-curl php5-mcrypt php5-intl && \  
mkdir /data  
WORKDIR /data  
RUN wget
http://downloads.sourceforge.net/project/roundcubemail/roundcubemail/${VERSION}/roundcubemail-${VERSION}-complete.tar.gz
&& tar xf roundcubemail-${VERSION}-complete.tar.gz && \  
rm roundcubemail-${VERSION}-complete.tar.gz && \  
mkdir /usr/share/nginx/www/ && \  
cp -r /data/roundcubemail-${VERSION}/* /usr/share/nginx/www/ && \  
chown -R www-data:root /usr/share/nginx/www/ && \  
find /usr/share/nginx/www/ -type d -exec chmod 755 {} + && \  
find /usr/share/nginx/www/ -type f -exec chmod 644 {} + && \  
rm -rf /data/roundcubemail-${VERSION} && \  
rm -rf /usr/share/nginx/html/index.html && \  
rm -rf /usr/share/nginx/www/installer/ && \  
rm -rf /usr/share/nginx/www/Dockerfile && \  
sed -i 's/user nginx;/user www-data;/g' /etc/nginx/nginx.conf && \  
sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' /etc/php5/fpm/php.ini && \  
sed -i 's/;date.timezone =/date.timezone = Europe\/Vienna/g'
/etc/php5/fpm/php.ini && \  
sed -i 's/upload_max_filesize = 2M/upload_max_filesize = 20M/g'
/etc/php5/fpm/php.ini && \  
sed -i 's/post_max_size = 8M/post_max_size = 20M/g' /etc/php5/fpm/php.ini && \  
rm -rf /etc/nginx/conf.d/default.conf  
  
ADD config/nginx-config.conf /etc/nginx/conf.d/default.conf  
ADD config/roundcube-config.inc.php /data/config.inc.php  
ADD start.sh /  
RUN ln -s /data/config.inc.php /usr/share/nginx/www/config/config.inc.php && \  
chown root:root /start.sh && chmod 100 /start.sh && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["/start.sh"]  

