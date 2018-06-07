FROM php:5.6-apache  
  
# Install php extensions  
RUN apt-get update && \  
apt-get install -y \  
libpng12-dev \  
libjpeg-dev \  
zlib1g-dev \  
git \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd  
RUN docker-php-ext-install mysqli  
RUN docker-php-ext-install zip  
  
# Install Node  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
7937DFD2AB06298B2293C3187D33FF9D0246406D
114F43EE0176B71C7BC219DD50A3051F888C628D  
  
RUN NODE_VERSION=$(curl https://semver.io/node/stable) \  
&& NPM_VERSION=$(curl https://semver.io/npm/stable) \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
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
  
# Install bower and gulp  
RUN npm install -g bower grunt-cli gulp  
  
# Install Composer  
RUN php -r "readfile('https://getcomposer.org/installer');" | php && mv
composer.phar /usr/bin/composer  
  
# Apache stuff  
COPY apache2.conf /etc/apache2/apache2.conf  
COPY app.conf /etc/apache2/sites-available/app.conf  
RUN ln -s /etc/apache2/sites-available/app.conf \  
/etc/apache2/sites-enabled/app.conf  
  
EXPOSE 9000  

