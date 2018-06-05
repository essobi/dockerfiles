FROM debian:jessie  
  
MAINTAINER Felix Kluge <f.kluge@agdsn.de>  
  
  
# Install everything  
# For installing ffmpeg, the deb-multimedia repository is used which might be
considered unsafe so use with caution  
RUN echo deb http://www.deb-multimedia.org jessie main non-free >>
/etc/apt/sources.list \  
&& apt-get update && apt-get install -y \--force-yes -q deb-multimedia-keyring
\  
&& apt-get install -y \--force-yes -q apache2 php5 php5-mysql php5-curl
php5-gd php5-ldap \  
&& apt-get update && apt-get install -y -q git curl ffmpeg \  
&& cd /var/www \  
&& git clone --branch 3.8.2 https://github.com/ampache/ampache.git \  
&& mv ampache/* ./ \  
&& rm -r ampache \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer install --prefer-source \--no-interaction \  
&& apt-get remove -y git \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& mkdir -p /var/data \  
&& chown -R www-data:www-data /var/www  
  
VOLUME ["/var/www/config","/var/www/themes","/var/data"]  
  
ENTRYPOINT ["/usr/sbin/apache2"]  
CMD ["-D", "FOREGROUND"]  

