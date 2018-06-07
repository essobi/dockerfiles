# Select image from https://hub.docker.com/_/php/  
FROM php:7.0  
# Install dotdeb for up-to-date packages  
ADD https://www.dotdeb.org/dotdeb.gpg /tmp/dotdeb.gpg  
  
RUN echo "Install dotdeb" \  
&& echo "deb http://packages.dotdeb.org jessie all" >
/etc/apt/sources.list.d/dotdeb.list \  
&& echo "deb-src http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list.d/dotdeb.list \  
&& apt-key add /tmp/dotdeb.gpg  
  
# Install git, the php image doesn't have installed  
RUN apt-get update -yqq  
RUN apt-get install git -yqq  
RUN apt-get install libssl-dev -y  
  
# Install opcache  
RUN docker-php-ext-install opcache  
  
# Install APCu  
RUN pecl install apcu  
RUN echo "extension=apcu.so" > /usr/local/etc/php/conf.d/apcu.ini  
  
# Install bcmath  
RUN docker-php-ext-install bcmath  
  
# Install bz2  
RUN apt-get install -y libbz2-dev  
RUN docker-php-ext-install bz2  
  
# Install calendar  
RUN docker-php-ext-install calendar  
  
# Install dba  
RUN docker-php-ext-install dba  
  
# Install GD  
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng12-dev  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install gd  
  
# Install mbstring  
RUN docker-php-ext-install mbstring  
  
# Install mcrypt  
RUN apt-get install -y libmcrypt-dev  
RUN docker-php-ext-install mcrypt  
  
# Install mysql driver  
RUN docker-php-ext-install pdo_mysql  
  
# Install PHP Extensions  
RUN docker-php-ext-install iconv  
RUN docker-php-ext-install json  
RUN docker-php-ext-install phar  
#RUN docker-php-ext-install curl  
RUN docker-php-ext-install ftp  
RUN docker-php-ext-install hash  
RUN docker-php-ext-install session  
#RUN docker-php-ext-install simplexml  
RUN docker-php-ext-install tokenizer  
#RUN docker-php-ext-install xml  
#RUN docker-php-ext-install xmlrpc  
RUN docker-php-ext-install zip  
  
# Install XSL  
RUN apt-get install -y libxslt-dev  
RUN docker-php-ext-install xsl  
  
# Install intl  
#RUN apt-get install -y libicu-dev  
#RUN pecl install intl  
#RUN docker-php-ext-install intl  
COPY config/php.ini /usr/local/etc/php/  
  
# PHP config  
#############  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/"
/usr/local/etc/php/php.ini && \  
sed -i 's/post_max_size = 8M/post_max_size = 16M/g' /usr/local/etc/php/php.ini
&& \  
sed -i 's/upload_max_filesize = 2M/upload_max_filesize = 16M/g'
/usr/local/etc/php/php.ini && \  
sed -i 's/error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT/error_reporting
= E_ALL/g' /usr/local/etc/php/php.ini && \  
sed -i "s/display_errors = Off/display_errors = On/"
/usr/local/etc/php/php.ini && \  
sed -i "s/max_execution_time = 30/max_execution_time = 300/"
/usr/local/etc/php/php.ini && \  
sed -i "s/max_input_time = 60/max_input_time = 300/"
/usr/local/etc/php/php.ini && \  
sed -i "s/memory_limit = 128M/memory_limit = 2G/" /usr/local/etc/php/php.ini
&& \  
sed -i "s/default_socket_timeout = 60/default_socket_timeout = 300/"
/usr/local/etc/php/php.ini  
  
# Installation de Java apt-get 8u102 + Ant  
#RUN apt-get install -y wget \  
# && wget --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/8u102-b14/jdk-8u102-linux-x64.tar.gz \  
## http://download.oracle.com/otn-
pub/java/jdk/8u102-b14/jdk-8u102-linux-x64.tar.gz  
# && mkdir /opt/jdk \  
# && tar -zxf jdk-8u102-linux-x64.tar.gz -C /opt/jdk \  
# && rm jdk-8u102-linux-x64.tar.gz \  
# && update-alternatives --install /usr/bin/java java
/opt/jdk/jdk1.8.0_102/bin/java 100 \  
# && update-alternatives --install /usr/bin/javac javac
/opt/jdk/jdk1.8.0_102/bin/javac 100  
#RUN apt-get remove openjdk-* icedtea* -y  
#RUN apt-get install -y ant \  
# && apt-get remove -y wget \  
# && apt-get clean && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
RUN mkdir -p /root/.ssh  
  
# XDEBUG  
#ENV XDEBUG_ENABLED=1  
#RUN yes | pecl install xdebug \  
# && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
# && echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
# && echo "xdebug.remote_autostart=off" >>
/usr/local/etc/php/conf.d/xdebug.ini  
# Install phpunit, the tool that we will use for testing  
#RUN curl --location --output /usr/local/bin/phpunit
https://phar.phpunit.de/phpunit.phar  
#RUN chmod +x /usr/local/bin/phpunit  
#RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
#RUN php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'e115a8dc7871f15d853148a7fbac7da27d6c0030b848d9b3dc09e2a0388afed865e6a3d6b3c0fad45c48e2b5fc1196ae')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;"  
#RUN php composer-setup.php  
#RUN mv composer.phar /usr/local/bin/composer  
#RUN php -r "unlink('composer-setup.php');"  
#COPY config/composer.json /root/.composer  
#RUN composer global install --no-scripts --no-suggest  

