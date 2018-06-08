#
================================================================================================================  
#  
# FreshRSS with NGINX and PHP-FPM  
#  
# @see https://github.com/AlbanMontaigu/docker-nginx-
php/blob/master/Dockerfile  
# @see https://github.com/AlbanMontaigu/docker-freshrss  
#
================================================================================================================  
# Base is a nginx install with php  
FROM amontaigu/nginx-php-plus:5.6.29  
# Maintainer  
MAINTAINER alban.montaigu@gmail.com  
  
# FreshRSS env variables  
ENV FRESHRSS_VERSION="1.6.2"  
# System update & install the PHP extensions we need  
# @see http://freshrss.org/#requirements  
RUN apt-get update \  
&& apt-get install -y libgmp-dev libgmp10 \  
&& rm -rf /var/lib/apt/lists/* \  
&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \  
&& docker-php-ext-install gmp  
  
# Get FreshRSS and install it  
RUN mkdir -p --mode=777 /var/backup/freshrss \  
&& mkdir -p --mode=777 /usr/src/freshrss \  
&& curl -o freshrss.tgz -SL
https://github.com/FreshRSS/FreshRSS/archive/$FRESHRSS_VERSION.tar.gz \  
&& tar -xzf freshrss.tgz --strip-components=1 -C /usr/src/freshrss \  
\--exclude=CHANGELOG.md \  
\--exclude=CONTRIBUTING.md \  
\--exclude=CREDITS.md \  
\--exclude=README.fr.md \  
\--exclude=README.md \  
\--exclude=LICENSE \  
\--exclude=tests \  
&& rm freshrss.tgz \  
&& chown -Rfv nginx:nginx /usr/src/freshrss \  
&& sed -i -e "s%doc_root = \"/var/www\"%doc_root = \"/var/www/p\"%g"
$PHP_INI_DIR/php.ini \  
&& sed -i -e "s%user_dir = \"/var/www\"%user_dir = \"/var/www/p\"%g"
$PHP_INI_DIR/php.ini  
  
# NGINX tuning for FRESHRSS  
COPY ./nginx/conf/sites-enabled/default.conf /etc/nginx/sites-
enabled/default.conf  
  
# Entrypoint to enable live customization  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
# Volume for freshrss backup  
VOLUME /var/backup/freshrss  
  
# grr, ENTRYPOINT resets CMD now  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/usr/bin/supervisord"]  

