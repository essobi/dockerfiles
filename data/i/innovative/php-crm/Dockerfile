FROM php:5.6-apache  
RUN apt-get update -y && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libcurl4-openssl-dev \  
unzip zip lzip \  
libbz2-dev libfontconfig1 libfontconfig1-dev \  
libfreetype6-dev libjpeg62-turbo-dev libzip-dev libzip-ocaml \  
locales libpng-dev libssl-dev libc-client2007e-dev libkrb5-dev unzip cron re2c
python tree tzdata \  
&& docker-php-ext-install iconv mcrypt mysqli mysql curl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-configure imap --with-imap-ssl --with-kerberos \  
&& docker-php-ext-configure opcache --enable-opcache \  
&& docker-php-ext-install gd pdo pdo_mysql imap opcache \  
&& docker-php-ext-configure zip --with-libzip \  
&& docker-php-ext-install zip  
  
  
# Configure timezone and locale  
RUN apt update && apt install -y git && ln -fs
/usr/share/zoneinfo/Europe/Moscow /etc/localtime && \  
echo "Europe/Moscow" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata && \  
sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
echo 'LANG="en_US.UTF-8"'>/etc/default/locale && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_US.UTF-8  
  
RUN docker-php-ext-configure opcache --enable-opcache \  
&& docker-php-ext-install opcache  
  
RUN ( \  
echo "opcache.memory_consumption=128"; \  
echo "opcache.interned_strings_buffer=8"; \  
echo "opcache.max_accelerated_files=4000"; \  
echo "opcache.revalidate_freq=5"; \  
echo "opcache.fast_shutdown=1"; \  
echo "opcache.enable_cli=1"; \  
) > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
ADD php.ini /usr/local/etc/php/  

