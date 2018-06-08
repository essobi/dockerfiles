FROM php:7.1-cli  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get update && apt-get install -y python-dev nodejs && \  
curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
pip install awsebcli --upgrade && \  
npm install -g gulp bower grunt-cli && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php --no-ansi --install-dir=/usr/bin --filename=composer &&
\  
php -r "unlink('composer-setup.php');" && \  
apt-get install -y \  
libpq-dev \  
libmemcached-dev \  
zlib1g-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libxml2 libxml2-dev && \  
docker-php-ext-install -j$(nproc) iconv mcrypt mbstring pdo_mysql tokenizer
zip && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) gd && \  
docker-php-ext-install soap && \  
curl -L -o /tmp/memcached.tar.gz "https://github.com/php-memcached-dev/php-
memcached/archive/php7.tar.gz" \  
&& mkdir -p /usr/src/php/ext/memcached \  
&& tar -C /usr/src/php/ext/memcached -zxvf /tmp/memcached.tar.gz --strip 1 \  
&& docker-php-ext-configure memcached \  
&& docker-php-ext-install memcached \  
&& rm /tmp/memcached.tar.gz \  
&& apt-get install -y git \  
&& pecl install mongodb \  
&& echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/mongod.ini \  
&& apt-get clean  
  

