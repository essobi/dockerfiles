# vim:set ft=dockerfile:  
FROM ubuntu  
  
#MAINTAINER Pooya Parsa <pooya@pi0.ir>  
  
ENV HOME=/var/www  
ENV TERM=xterm  
ENV SHELL=bash  
EXPOSE 80  
ENTRYPOINT ["entrypoint"]  
  
# Install deps & cleanup  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install -y \  
bash supervisor nginx git curl sudo zip unzip xz-utils libxrender1 \  
php php-apcu php-bz2 php-cache php-cli php-curl php-fpm php-gd php-geoip \  
php-gettext php-gmp php-imagick php-imap php-json php-mcrypt php-mbstring php-
zip \  
php-memcached php-mongodb php-mysql php-pear php-redis php-xml php-intl php-
soap \  
php-sqlite3 php-dompdf php-fpdf php-guzzlehttp php-guzzlehttp-psr7 php-jwt
php-ssh2 php-bcmath && \  
curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash && \  
apt-get install -y nodejs && \  
curl -o- -L https://yarnpkg.com/install.sh | bash -s -- && \  
ln -sfv /root/.yarn/bin/* /bin && \  
ln -sfv /root/.yarn/bin/node-gyp-bin/node-gyp /bin/node-gyp && \  
rm -rf /var/cache/apt && rm -rf /var/lib/apt  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | \  
php -- --install-dir=/usr/bin --filename=composer  
  
# PHP-FPM  
RUN mkdir -p /run/php  
COPY conf/www.conf /etc/php/7.0/fpm/pool.d/www.conf  
COPY conf/php.ini /etc/php/7.0/fpm/php.ini  
  
# Nginx  
COPY conf/nginx.conf /etc/nginx/nginx.conf  
COPY conf/nginx-default /etc/nginx/conf.d/default.conf  
  
# Adjust permissions  
RUN mkdir -p /var/www && \  
chown -R www-data:www-data /var/www /root && \  
ln -vs /var/www/ /home/www-data  
  
# Supedvisord  
COPY conf/supervisord.conf /etc/supervisord.conf  
  
# Bin  
COPY bin /bin  

