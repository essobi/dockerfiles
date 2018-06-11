#
================================================================================================================  
#  
# Wallabag with NGINX and PHP-FPM  
#  
# @see https://github.com/AlbanMontaigu/docker-nginx-php-plus  
# @see https://github.com/AlbanMontaigu/docker-dokuwiki  
#
================================================================================================================  
# Base is a nginx install with php  
FROM amontaigu/nginx-php-plus:5.6.29  
# Maintainer  
MAINTAINER alban.montaigu@gmail.com  
  
# Wallabag env variables  
ENV WALLABAG_VERSION="2.1.5"  
# System update & install the PHP extensions we need  
RUN apt-get update \  
&& apt-get install -y rsync libtidy-0.99-0 libtidy-dev unzip \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install tidy  
  
# Get Wallabag and install it  
RUN mkdir -p --mode=777 /var/backup/wallabag \  
&& mkdir -p --mode=777 /usr/src/wallabag \  
&& curl -o wallabag.tgz -SL http://static.wallabag.org/releases/wallabag-
release-$WALLABAG_VERSION.tar.gz \  
&& tar -xzf wallabag.tgz --strip-components=1 -C /usr/src/wallabag \  
\--exclude=.github \  
\--exclude=.gitignore \  
\--exclude=docs \  
\--exclude=docker \  
\--exclude=tests \  
&& rm wallabag.tgz \  
&& chown -Rfv nginx:nginx /usr/src/wallabag \  
&& sed -i -e "s%doc_root = \".*\"%doc_root = \"/var/www/web\"%g"
$PHP_INI_DIR/php.ini \  
&& sed -i -e "s%user_dir = \".*\"%user_dir = \"/var/www/web\"%g"
$PHP_INI_DIR/php.ini  
  
# NGINX tuning for WALLABAG  
COPY ./nginx/conf/sites-enabled/default.conf /etc/nginx/sites-
enabled/default.conf  
  
# Entrypoint to enable live customization  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
# Volume for wallabag backup  
VOLUME /var/backup/wallabag  
  
# grr, ENTRYPOINT resets CMD now  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/usr/bin/supervisord"]  

