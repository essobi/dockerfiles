FROM slicemenice/php-apache-rewrite  
  
RUN a2enmod ssl  
  
# ant - required to configure and build Shopware 5  
# composer - not directly required by Shopware 5, as the build will also
install a local composer for Shopware, but you can also use it to install
Shopware via https://packagist.org/packages/shopware/shopware  
# curl, git, wget - necessary to execute tasks defined in Shopware's build.xml
and for composer to install dependencies  
# openjdk-7-jdk - required by Ant  
# mysql-client - required by Shopware's build.xml to connect to the SQL
database server located in another docker container  
# xdebug - used for debugging PHP  
RUN apt-get update && apt-get install -y \  
ant \  
curl \  
git \  
libfreetype6-dev \  
libjpeg-dev \  
libpng12-dev \  
libssl-dev \  
libxml2-dev \  
mysql-client \  
openjdk-7-jdk \  
wget \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-png-
dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysql mysqli zip mbstring pdo pdo_mysql soap ftp  
  
RUN pecl install xdebug  
RUN touch /usr/local/etc/php/conf.d/xdebug.ini; \  
echo xdebug.remote_enable=1 >> /usr/local/etc/php/conf.d/xdebug.ini; \  
echo xdebug.remote_autostart=0 >> /usr/local/etc/php/conf.d/xdebug.ini; \  
echo xdebug.remote_connephpct_back=1 >> /usr/local/etc/php/conf.d/xdebug.ini;
\  
echo xdebug.remote_port=9000 >> /usr/local/etc/php/conf.d/xdebug.ini; \  
echo xdebug.remote_log=/tmp/php5-xdebug.log >>
/usr/local/etc/php/conf.d/xdebug.ini;  
  
# install composer  
ENV COMPOSER_HOME /root/composer  
ENV COMPOSER_VERSION 1.0.0-alpha10  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer --version=${COMPOSER_VERSION}  
  
# install node/npm  
# verify gpg and sha256: http://nodejs.org/dist/v0.10.30/SHASUMS256.txt.asc  
# gpg: aka "Christopher Dickinson <christopher.s.dickinson@gmail.com>"  
# gpg: aka "Colin Ihrig <cjihrig@gmail.com>"  
# gpg: aka "keybase.io/octetcloud <octetcloud@keybase.io>"  
# gpg: aka "keybase.io/fishrock <fishrock@keybase.io>"  
# gpg: aka "keybase.io/jasnell <jasnell@keybase.io>"  
# gpg: aka "Rod Vagg <rod@vagg.org>"  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
9554F04D7259F04124DE6B476D5A82AC7E37093B
94AE36675C464D64BAFA68DD7434390BDBE9B9C5
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93
FD3A5288F042B6850C66B31F09FE44734EB7990E
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1
DD8F2338BAE7501E3DD5AC78C273792F7D83545D  
  
ENV NODE_VERSION 0.12.7  
ENV NPM_VERSION 3.0-latest  
  
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
  
# install grunt  
RUN npm install -g grunt-cli  
  
#install bower  
RUN npm install -g bower

