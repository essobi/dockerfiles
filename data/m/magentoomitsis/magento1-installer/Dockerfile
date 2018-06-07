FROM php:5.6  
  
# Configure PHP  
RUN buildDeps=" \  
libpng12-dev \  
libjpeg-dev \  
libmcrypt-dev \  
libxml2-dev \  
freetype* \  
vim \  
zip \  
bzip2 \  
jq \  
mysql-client \  
git-core \  
wget \  
net-tools \  
grep \  
gawk \  
ssh \  
"; \  
set -x \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
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
RUN wget
https://raw.githubusercontent.com/composer/getcomposer.org/1b137f8bf6db3e79a38a5bc45324414a6b1f9df2/web/installer
-O - -q | php -- --quiet  
RUN mv composer.phar /usr/local/bin/composer  
  
# Install magerun  
RUN curl -o magerun http://files.magerun.net/n98-magerun.phar && \  
chmod +x ./magerun && \  
./magerun selfupdate && \  
cp ./magerun /usr/local/bin/ && \  
rm ./magerun  
  
#ADD SSH RSA_KEY AND CONFIG  
RUN mkdir -p /root/.ssh && \  
touch /root/.ssh/known_hosts  

