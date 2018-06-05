FROM debian:jessie  
MAINTAINER Gabriel Wicke <gwicke@wikimedia.org>  
  
# Waiting in antiticipation for built-time arguments  
# https://github.com/docker/docker/issues/14634  
ENV MEDIAWIKI_VERSION 1.28.0  
# XXX: Consider switching to nginx.  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
apache2 \  
libapache2-mod-php5 \  
php5-mysql \  
php5-cli \  
php5-gd \  
php5-curl \  
imagemagick \  
netcat \  
git \  
php-pear \  
&& pear install mail \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/apt/archives/* \  
&& a2enmod rewrite \  
&& a2enmod proxy \  
&& a2enmod proxy_http \  
# Remove the default Debian index page.  
&& rm /var/www/html/index.html  
  
  
# MediaWiki setup  
RUN set -x; \  
mkdir -p /usr/src \  
&& git clone \  
\--depth 1 \  
-b $MEDIAWIKI_VERSION \  
https://gerrit.wikimedia.org/r/p/mediawiki/core.git \  
/usr/src/mediawiki \  
&& cd /usr/src/mediawiki \  
&& git clone \--depth 1 -b REL1_28
https://gerrit.wikimedia.org/r/p/mediawiki/vendor.git \  
&& git clone \--depth 1 -b REL1_28
https://phabricator.wikimedia.org/diffusion/SVEC/Vector skins/Vector  
  
COPY php.ini /usr/local/etc/php/conf.d/mediawiki.ini  
  
COPY apache/mediawiki.conf /etc/apache2/  
RUN echo "Include /etc/apache2/mediawiki.conf" >> /etc/apache2/apache2.conf  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
EXPOSE 80 443  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apachectl", "-e", "info", "-D", "FOREGROUND"]  

