FROM php:7.0-apache  
  
MAINTAINER Robert Schneider <shakemedev@gmail.com>  
  
ARG TAG=release_stable_2017-02-19e  
  
ADD https://github.com/splitbrain/dokuwiki/archive/$TAG.tar.gz
/dokuwiki.tar.gz  
  
RUN docker-php-ext-enable opcache \  
&& cd /var/www/html \  
&& tar xzf /dokuwiki.tar.gz \--strip 1 \  
&& rm /dokuwiki.tar.gz \  
&& chown -R www-data.www-data -R /var/www/html \  
&& mkdir -p /src/lib \  
&& chown -R www-data.www-data /src \  
&& cp -pf VERSION /src/ \  
&& cp -prf conf/. /src/conf/ \  
&& cp -prf data/. /src/data/ \  
&& cp -prf lib/plugins/. /src/lib/plugins/ \  
&& cp -prf lib/tpl/. /src/lib/tpl/ \  
&& a2enmod rewrite \  
&& cp .htaccess.dist .htaccess \  
&& sed -i 's/^#RewriteEngine/RewriteEngine/g' /var/www/html/.htaccess \  
&& sed -i 's/^#RewriteRule/RewriteRule/g' /var/www/html/.htaccess \  
&& sed -i 's/^#RewriteCond/RewriteCond/g' /var/www/html/.htaccess  
  
VOLUME ["/var/www/html/conf", ["/var/www/html/data"]  
VOLUME ["/var/www/html/lib/plugins", ["/var/www/html/lib/tpl"]  
  
COPY docker-php-entrypoint /usr/local/bin/  
  

