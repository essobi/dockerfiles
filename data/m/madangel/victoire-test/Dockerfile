FROM php:7.1  
ENV DEBIAN_FRONTEND=noninteractive  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.11.1  
RUN apt-get update && apt-get install -y \  
wget gnupg  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng-dev \  
zlib1g-dev libicu-dev g++ apt-transport-https nodejs build-essential libssl-
dev nodejs-legacy \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt bcmath mbstring \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-install intl zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-install exif  
  
RUN apt-get update && \  
apt-get install -y git libssh2-1 libssh2-1-dev && \  
pecl install ssh2-1.1.2; \  
docker-php-ext-enable ssh2  
  
#See https://github.com/debuerreotype/docker-debian-artifacts/issues/24  
RUN mkdir -p /usr/share/man/man1  
  
RUN apt-get install mysql-server mysql-client mysql-common vim ruby-full git \  
xvfb default-jdk iceweasel redis-server perl pwgen zip unzip libsqlite3-dev
curl rabbitmq-server libxml2-dev \  
libmemcached-dev yarn -yqq  
  
RUN apt-get install -y libmagickwand-6.q16-dev --no-install-recommends \  
&& ln -s /usr/lib/x86_64-linux-gnu/ImageMagick-6.8.9/bin-Q16/MagickWand-config
/usr/bin \  
&& pecl install imagick \  
&& echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini  
  
RUN apt-get clean  
  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz"  
  
RUN npm install -g bower less@2.7.2 gulp grunt  
# runs node.js as a background service  
RUN npm i nohup  
RUN gem install sass mailcatcher capistrano capistrano-symfony capistrano-
composer capistrano-file-permissions  
  
RUN docker-php-ext-install pdo_mysql soap  
RUN curl http://selenium-release.storage.googleapis.com/2.53/selenium-server-
standalone-2.53.0.jar > selenium-server-standalone-2.53.0.jar  
  
RUN git clone https://github.com/php-memcached-dev/php-memcached
/usr/src/php/ext/memcached \  
&& cd /usr/src/php/ext/memcached && git checkout -b php7 origin/php7 \  
&& docker-php-ext-configure memcached \  
&& docker-php-ext-install memcached  
  
# Install Google Chrome  
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list && \  
apt-get -yqq update && \  
apt-get -yqq install google-chrome-stable && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Chrome WebDriver  
RUN CHROMEDRIVER_VERSION=`curl -sS
chromedriver.storage.googleapis.com/LATEST_RELEASE` && \  
mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \  
curl -sS -o /tmp/chromedriver_linux64.zip
http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
&& \  
unzip -qq /tmp/chromedriver_linux64.zip -d
/opt/chromedriver-$CHROMEDRIVER_VERSION && \  
rm /tmp/chromedriver_linux64.zip && \  
chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \  
ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver
/usr/local/bin/chromedriver  
  
RUN pecl install mongodb && echo "extension=mongodb.so" >
/usr/local/etc/php/conf.d/ext-mongodb.ini  
  
EXPOSE 22 80  
RUN curl -L -O
https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.3.4/elasticsearch-2.3.4.tar.gz  
RUN tar -xvf elasticsearch-2.3.4.tar.gz  
  
WORKDIR "/var/www/app"

