FROM php:5.6-fpm  
MAINTAINER Porawit Poboonma <ball6847@gmail.com>  
  
ENV TERM=xterm-256color  
ENV LC_ALL en_US.UTF-8  
  
RUN apt-get update -y \  
&& apt-get install -y libmemcached-dev \  
libtidy-dev \  
libxml2-dev \  
libxslt1-dev \  
libzip-dev \  
zlib1g-dev \  
libpspell-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
git \  
locales \  
&& echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen en_US.UTF-8 \  
&& echo -e 'LANG="en_US.UTF-8"\nLANGUAGE="en_US:en"\n' > /etc/default/locale \  
&& dpkg-reconfigure --frontend=noninteractive locales \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8 \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd iconv mcrypt exif fileinfo mysqli
pdo_mysql pcntl tidy xmlrpc xsl zip bcmath pspell shmop sockets \  
&& pecl install xdebug \  
&& (curl -o- https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer) \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

