# A Lumen + MariaDB RESTful truck commerce site server.  
# Copyright (C) 2016 Ryan Y.  
#  
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU Affero General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# This program is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU Affero General Public License for more details.  
#  
# You should have received a copy of the GNU Affero General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
FROM php:5.6-fpm  
# Install modules  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
php5-cli \  
php5-mcrypt \  
php5-gd \  
php5-xdebug \  
php5-curl \  
php5-pgsql \  
libpq-dev  
  
RUN docker-php-ext-install bcmath  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install pdo  
RUN docker-php-ext-install pdo_pgsql  
RUN docker-php-ext-install tokenizer  
RUN apt-get install -y zlib1g-dev \  
&& docker-php-ext-install zip  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Possible values for docker-php-ext-install:  
# bcmath bz2 calendar ctype curl dba dom enchant exif fileinfo filter ftp gd  
# gettext gmp hash iconv imap interbase intl json ldap mbstring mcrypt mssql  
# mysql mysqli oci8 odbc opcache pcntl pdo pdo_dblib pdo_firebird pdo_mysql  
# pdo_oci pdo_odbc pdo_pgsql pdo_sqlite pgsql phar posix pspell readline
recode  
# reflection session shmop simplexml snmp soap sockets spl standard sybase_ct  
# sysvmsg  
# sysvsem sysvshm tidy tokenizer wddx xml xmlreader xmlrpc xmlwriter xsl zip  

