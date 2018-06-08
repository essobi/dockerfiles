FROM php:7.1-apache  
RUN apt-get update  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install mysqli  
RUN apt-get install ssl-cert  
RUN apt-get install -qy \  
build-essential hardening-wrapper \  
libmcrypt4 libxml2-utils \  
libcurl4-openssl-dev libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev \  
libpng12-dev libxml2-dev zlib1g-dev libpng-dev ssmtp imagemagick  
RUN echo "mailhub=mail:25\nUseTLS=NO\nFromLineOverride=YES" >
/etc/ssmtp/ssmtp.conf  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install gd soap zip  
RUN pecl install xdebug  
RUN docker-php-ext-enable xdebug  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini  
RUN a2enmod expires  
RUN a2enmod rewrite  
RUN a2enmod ssl  
  
RUN echo "\ndeb http://ftp.us.debian.org/debian testing main contrib non-free"
>> /etc/apt/sources.list  
RUN mkdir -p /etc/apt/apt.conf.d && cd /etc/apt/apt.conf.d && echo
"APT::Default-Release \"stable\";" >> 99default-release  
RUN apt-get update  
RUN apt-get -y -t testing install libpcre3  
  
RUN echo "Europe/Berlin" > /etc/timezone  
RUN dpkg-reconfigure tzdata  
  
COPY ./init.sh /usr/local/bin/init.sh  
ENTRYPOINT ["bash", "/usr/local/bin/init.sh"]  

