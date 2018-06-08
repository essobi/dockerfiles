FROM php:7-apache  
RUN apt-get update && apt-get install -y \  
libmcrypt-dev \  
git \  
zlib1g-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Basic lumen packages  
RUN docker-php-ext-install \  
mcrypt \  
mbstring \  
tokenizer \  
zip  
  
# Add php.ini for production  
COPY php/php.ini-production $PHP_INI_DIR/php.ini  
COPY apache/apache2.conf /etc/apache2/apache2.conf  
  
# Configuring Apache  
RUN rm /etc/apache2/sites-available/000-default.conf \  
&& rm /etc/apache2/sites-enabled/000-default.conf  
  
# Enable rewrite module  
RUN a2enmod rewrite  
  
WORKDIR /var/www/html  
  
# Download and Install Composer  
RUN curl -s http://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Add vendor binaries to PATH  
ENV PATH=/var/www/html/vendor/bin:$PATH  
  
# Frontend tasks  
RUN apt-get update && apt-get install -y \  
xz-utils \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
## Install node to manage frontend dependencies  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.2.2  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt  
  
RUN npm install --global gulp  
  
COPY laravel-apache2-foreground /usr/local/bin/  
  
CMD ["laravel-apache2-foreground"]  

