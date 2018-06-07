FROM php:5.6  
COPY php/php.ini /usr/local/etc/php/php.ini  
COPY magerun/n98-magerun.yaml.tmpl /etc/n98-magerun.yaml.tmpl  
COPY magento/local.xml.tmpl /etc/local.xml.tmpl  
COPY magento/fpc.xml.tmpl /etc/fpc.xml.tmpl  
COPY bin/substitute-env-vars.sh /bin/substitute-env-vars.sh  
COPY bin/install.sh /bin/install.sh  
  
# Configure PHP  
RUN buildDeps=" \  
libpng12-dev \  
libjpeg-dev \  
libmcrypt-dev \  
libxml2-dev \  
freetype* \  
"; \  
set -x \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure \  
gd --with-png-dir=/usr --with-jpeg-dir=/usr --with-freetype-dir \  
&& docker-php-ext-install \  
gd \  
mbstring \  
mysqli \  
mcrypt \  
mysql \  
pdo_mysql \  
zip \  
&& apt-get purge -y --auto-remove  
  
# Install Tools  
RUN apt-get update && \  
apt-get install -y \  
vim \  
telnet \  
netcat \  
git-core \  
zip \  
wget && \  
apt-get purge -y --auto-remove  
  
ENV DOCKERIZE_VERSION v0.6.1  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
# Install magerun  
RUN curl -o n98-magerun.phar https://files.magerun.net/n98-magerun.phar && \  
chmod +x ./n98-magerun.phar && \  
./n98-magerun.phar selfupdate && \  
mv ./n98-magerun.phar /usr/local/bin/magerun && \  
apt-get update && \  
apt-get install -qy mysql-client && \  
apt-get purge -y --auto-remove  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer
--install-dir=bin  

