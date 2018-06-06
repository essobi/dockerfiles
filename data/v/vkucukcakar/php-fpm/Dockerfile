###  
# vkucukcakar/php-fpm  
# PHP-FPM Docker image with automatic configuration file creation and export  
# Copyright (c) 2017 Volkan Kucukcakar  
#  
# This file is part of vkucukcakar/php-fpm.  
#  
# vkucukcakar/php-fpm is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 2 of the License, or  
# (at your option) any later version.  
#  
# vkucukcakar/php-fpm is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
#  
# This copyright notice and license must be retained in all files and
derivative works.  
###  
FROM php:7.2.2-fpm-alpine  
  
LABEL maintainer "Volkan Kucukcakar"  
  
EXPOSE 9000  
VOLUME [ "/configurations" ]  
  
# Setup opcache file cache directory  
RUN mkdir -p /data/opcache \  
&& chown -R www-data:www-data /data/opcache \  
&& chmod -R 774 /data/opcache  
  
# Install/enable common php extensions: gd iconv mbstring mysqli pdo pdo_mysql  
RUN apk add --update \  
freetype-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& docker-php-ext-install -j${NPROC} gd iconv mbstring mysqli pdo pdo_mysql \  
&& docker-php-ext-enable opcache.so \  
&& rm -rf /var/cache/apk/*  
  
# Install bash (for basic level of shell compatibility) that will be required
by entrypoint later  
# Install gettext (for envsubst command) that will be required by entrypoint
later  
# Install ssmtp  
# Install shadow package (for usermod command)  
RUN apk add --update \  
bash \  
gettext \  
ssmtp \  
shadow \  
&& rm -rf /var/cache/apk/*  
  
# Setup server document root and home directories  
RUN chown www-data:www-data /var/www/html \  
&& chown www-data:www-data /home/www-data  
  
# Disable default configuration files of the parent image  
RUN mv /etc/ssmtp/ssmtp.conf /etc/ssmtp/ssmtp.conf.bak \  
&& mv /usr/local/etc/php-fpm.d/www.conf /usr/local/etc/php-fpm.d/www.conf.bak  
#&& mv /usr/local/etc/php/conf.d/php.ini
/usr/local/etc/php/conf.d/php.ini.bak; exit 0  
# Copy template configuration files  
COPY templates /templates  
  
# Create sessions directory and set correct permissions  
RUN mkdir /sessions \  
&& chown www-data:www-data /sessions  
  
# Setup entrypoint  
COPY common/entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
# Set CMD again, CMD is not inherited from parent if ENTRYPOINT is set  
CMD ["php-fpm"]  

