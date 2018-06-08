FROM tgbyte/nginx-php-fpm  
MAINTAINER Thilo-Alexander Ginkel <thilo@ginkel.com>  
  
ENV SELF_URL_PATH=http://localhost \  
DB_NAME=ttrss \  
DB_USER=ttrss \  
DB_PASS=ttrss \  
TTRSS_SOURCE_TAR_URL=https://git.tt-rss.org/git/tt-rss/archive/master.tar.gz \  
DEBIAN_FRONTEND=noninteractive  
  
RUN DEBIAN_FRONTEND=noninteractive \  
set -x \  
&& apt-get update -qq \  
&& apt-get install -y -qq \  
php7.0-curl \  
php7.0-gd \  
php7.0-json \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-pgsql \  
php7.0-xml \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& phpenmod mcrypt  
  
# add ttrss as the only nginx site  
ADD ttrss.nginx.conf /etc/nginx/conf.d/ttrss.conf  
  
WORKDIR /var/www  
  
RUN set -x \  
&& apt-get update -qq \  
&& apt-get install -qq -y curl --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -SL ${TTRSS_SOURCE_TAR_URL} | tar xzC /var/www --strip-components 1 \  
&& apt-get purge -y --auto-remove curl \  
&& chown www-data:www-data -R /var/www  
  
WORKDIR /var/tmp  
  
ADD entrypoint.d/ /entrypoint.d  
ADD configure-db.php /configure-db.php  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf.d/ttrss-update-
daemon.conf  

