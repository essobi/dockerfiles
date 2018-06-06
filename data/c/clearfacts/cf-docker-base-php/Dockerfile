FROM php:7.1-fpm  
  
ENV TZ=Europe/Brussels  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN apt-get update \  
&& apt-get install -y zlib1g-dev libicu-dev g++ libc-client-dev libkrb5-dev
libxml2-dev libmcrypt-dev libgmp-dev git wget bzip2 tar nano libtiff5
libpng12-0 libopenjpeg5 libfontconfig runit \  
&& apt-get clean \  
&& export TERM=xterm  
  
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-install bcmath intl pdo_mysql imap soap opcache mcrypt zip
gmp \  
&& pecl channel-update pecl.php.net \  
&& pecl install apcu \  
&& rm -rf /tmp/pear  
  
RUN pecl install -o -f redis \  
&& rm -rf /tmp/pear \  
&& echo "extension=redis.so" > /usr/local/etc/php/conf.d/redis.ini  
  
COPY php.ini /usr/local/etc/php/  
RUN wget http://curl.haxx.se/ca/cacert.pem -O /usr/local/etc/php/cacert.pem \  
&& echo "export TERM=xterm" >> ~/.bashrc  
  
COPY zzz-clearfacts.conf /usr/local/etc/php-fpm.d/zzz-clearfacts.conf  
  
COPY install_composer.sh /usr/local/bin  
# twee RUN commando's nodig, anders 'Text file busy' error bij builden...  
RUN chmod +x /usr/local/bin/install_composer.sh  
RUN /usr/local/bin/install_composer.sh  
RUN composer.phar global require hirak/prestissimo  
  
ADD tools /tools  
  
# install private key voor private github repos  
RUN mkdir /root/.ssh \  
&& cp /tools/id_rsa /root/.ssh/id_rsa \  
&& cp /tools/id_rsa.pub /root/.ssh/id_rsa.pub \  
&& chmod -R 600 /root/.ssh \  
&& ssh-keyscan github.com >> ~/.ssh/known_hosts  
  
# test php and show all info  
RUN php -i  

