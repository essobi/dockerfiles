FROM abesiyo/php:5.6  
MAINTAINER Alberto Contreras <abecontreras@me.com>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libbz2-dev \  
libxslt-dev \  
libfontconfig \  
libldap2-dev \  
mysql-client \  
php-pear \  
curl \  
git \  
subversion \  
unzip \  
wget \  
vim \  
&& rm -r /var/lib/apt/lists/*  
  
# PHP Extensions  
RUN docker-php-ext-install bcmath mcrypt zip bz2 pcntl xsl \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install ldap  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'e115a8dc7871f15d853148a7fbac7da27d6c0030b848d9b3dc09e2a0388afed865e6a3d6b3c0fad45c48e2b5fc1196ae')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;"  
RUN php composer-setup.php  
RUN php -r "unlink('composer-setup.php');"  
  
RUN mv composer.phar /usr/local/bin/composer  
  
# Add vimrc  
COPY vimrc /root/.vimrc  
  
# Add bashrc  
COPY bashrc /root/.bashrc  
  
RUN usermod -u 1000 www-data  
RUN usermod -a -G users www-data  
  
RUN chown -R www-data:www-data /var/www  
  
WORKDIR /var/www/html  

