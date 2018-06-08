FROM php:5-apache  
  
RUN a2enmod rewrite  
RUN a2enmod ssl  
  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
libpng12-dev \  
libjpeg-dev \  
wget \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysql mysqli zip  
  
RUN pecl install xdebug  
RUN touch /usr/local/etc/php/conf.d/xdebug.ini; \  
echo xdebug.remote_enable=1 >> /usr/local/etc/php/conf.d/xdebug.ini; \  
echo xdebug.remote_autostart=0 >> /usr/local/etc/php/conf.d/xdebug.ini; \  
echo xdebug.remote_connect_back=1 >> /usr/local/etc/php/conf.d/xdebug.ini; \  
echo xdebug.remote_port=9000 >> /usr/local/etc/php/conf.d/xdebug.ini; \  
echo xdebug.remote_log=/tmp/php5-xdebug.log >>
/usr/local/etc/php/conf.d/xdebug.ini;  
  
# install composer  
ENV COMPOSER_HOME /root/composer  
ENV COMPOSER_VERSION 1.0.0-alpha10  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer --version=${COMPOSER_VERSION}  
  
# install nodejs and npm  
# verify gpg and sha256: http://nodejs.org/dist/v0.10.30/SHASUMS256.txt.asc  
# gpg: aka "Timothy J Fontaine (Work) <tj.fontaine@joyent.com>"  
# gpg: aka "Julien Gilli <jgilli@fastmail.fm>"  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
7937DFD2AB06298B2293C3187D33FF9D0246406D
114F43EE0176B71C7BC219DD50A3051F888C628D  
  
ENV NODE_VERSION 4.1.2  
ENV NPM_VERSION 3.x-next  
  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache clear

