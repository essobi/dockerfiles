FROM php:7  
LABEL maintainer="Shahriyar Imanov <shehi@imanov.me>"  
  
WORKDIR /var/www  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN apt-get update -y \  
&& apt-get install -y apt-utils \  
&& apt-get upgrade -y \  
&& mkdir -p /usr/share/man/man1 \  
&& apt-get install -y \  
bzip2 \  
cron \  
daemon \  
fontforge \  
git \  
gnupg \  
libfreetype6-dev \  
libicu-dev \  
libjpeg-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libmemcached-dev \  
libpng-dev \  
libpq-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
locales \  
locales-all \  
mysql-client \  
nano \  
openjdk-8-jre \  
sudo \  
telnet \  
unzip \  
wget  
  
# Install PHP extensions  
RUN docker-php-ext-install \  
bcmath \  
calendar \  
exif \  
gettext \  
intl \  
pdo_mysql \  
pdo_pgsql \  
soap \  
sockets \  
xsl \  
zip  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
RUN pecl install -of mcrypt memcached \  
&& docker-php-ext-enable mcrypt memcached  
  
# Install Google's depot-tools  
#RUN apt-get install -y python libglib2.0-dev  
#RUN git clone
https://chromium.googlesource.com/chromium/tools/depot_tools.git /tmp/.depot-
tools  
#ENV PATH=$PATH:/tmp/.depot-tools  
# Fetch and compile v8  
#RUN cd /tmp \  
# && fetch v8 \  
# && cd v8 \  
# && git checkout 6.4.345 \  
# && gclient sync \  
# && tools/dev/v8gen.py -vv x64.release -- is_component_build=true \  
# && ninja -C out.gn/x64.release/ \  
# && mkdir -p /opt/v8/lib \  
# && mkdir -p /opt/v8/include \  
# && cp out.gn/x64.release/lib*.so out.gn/x64.release/*_blob.bin
out.gn/x64.release/icudtl.dat /opt/v8/lib/ \  
# && cp -R include/* /opt/v8/include/ \  
# && apt-get remove python -y  
# Compile php-v8js  
#RUN git clone --depth=1 https://github.com/phpv8/v8js.git /tmp/v8js \  
# && cd /tmp/v8js \  
# && phpize \  
# && ./configure --with-v8js=/opt/v8 LDFLAGS="-lstdc++"  
#ENV NO_INTERACTION 1  
#RUN cd /tmp/v8js \  
# && make \  
# && make test \  
# && make install \  
# && docker-php-ext-enable v8js  
# Locale  
RUN locale-gen en_US.UTF-8 && locale-gen az_AZ.UTF-8 && locale-gen tr_TR.UTF-8
&& dpkg-reconfigure locales  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
# Install PECL php-mongodb  
RUN pecl install -of mongodb \  
&& rm -rf /tmp/pear \  
&& echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/mongo.ini  
  
# Install PECL php-xdebug  
RUN pecl install -of xdebug-2.6.0beta1 \  
&& rm -rf /tmp/pear \  
&& echo "zend_extension=xdebug.so" | tee /usr/local/etc/php/conf.d/xdebug.ini
\  
&& echo "xdebug.max_nesting_level = 1000" | tee -a
/usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.idekey = basisPhp" | tee -a
/usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable = 1" | tee -a
/usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_port = 54321" | tee -a
/usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_connect_back = 1" | tee -a
/usr/local/etc/php/conf.d/xdebug.ini  
  
# Port for XDebug  
EXPOSE 54321  
# Timezone  
RUN echo "date.timezone = UTC" | tee /usr/local/etc/php/conf.d/date.ini  
  
# Install php-redis extension through Git  
RUN git clone https://github.com/phpredis/phpredis.git /tmp/phpredis \  
&& cd /tmp/phpredis \  
&& git checkout 3.1.4 \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& echo "extension=redis.so" | tee /usr/local/etc/php/conf.d/redis.ini  
  
# List of PHP extensions installed  
RUN php -m  
  
# Install Node  
RUN set -ex \  
&& for key in \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
77984A986EBC2AA786BC0F66B01FBB92821C587A \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 8.9.4  
ENV NPM_VERSION 5  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs \  
&& npm install -g npm@$NPM_VERSION \  
&& rm -rf /tmp/npm-*  
  
# Install Node global dependencies  
RUN npm install -g ttf2eot jshint  
  
# Port for node --inspect  
EXPOSE 9229  
# Clean-up  
RUN apt-get clean \  
&& apt-get remove -y gnupg \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add a non-root user to prevent files being created with root permissions on
host machine.  
ARG PUID=1000  
ARG PGID=1000  
RUN groupadd -g $PGID basis && useradd -u $PUID -g basis -M basis  
RUN usermod -aG sudo basis  
RUN sed -i -e "s/%sudo.*/%sudo ALL=(ALL:ALL) NOPASSWD: ALL/g" /etc/sudoers  
  
# Add Web-font related tools to PATH  
USER basis  
ENV PATH
$PATH:/var/www/storage/build/tools/sfnt2woff:/var/www/storage/build/tools/woff2  

