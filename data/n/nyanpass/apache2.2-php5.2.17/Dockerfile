FROM httpd:2.2  
MAINTAINER Tomofumi Inoue <inoue@grageinc.com>  
  
ENV HTTPD_CONF $HTTPD_PREFIX/conf/httpd.conf  
ENV PHP_INI /usr/local/lib/php.ini  
ENV HOME /root  
  
RUN usermod -u 1000 www-data && groupmod -g 1000 www-data \  
&& sed -i 's/User daemon/User www-data/' $HTTPD_CONF \  
&& sed -i 's/Group daemon/Group www-data/' $HTTPD_CONF  
  
WORKDIR $HOME  
  
ADD http://www.geocities.jp/aoba_suzukaze/php-5.2.17.tar.bz2 .  
ADD http://www.geocities.jp/aoba_suzukaze/libxml29_compat.patch .  
  
RUN echo 'ServerName localhost:80' >> $HTTPD_CONF  
  
RUN apt-get update && apt install -y --no-install-recommends bzip2 gcc make
libxml2-dev libmysqlclient-dev patch autoconf  
  
RUN ln -sf /usr/lib/x86_64-linux-gnu/libmysqlclient.so
/usr/lib/libmysqlclient.so \  
&& ln -sf /usr/lib/x86_64-linux-gnu/libmysqlclient.a /usr/lib/libmysqlclient.a  
  
RUN set -x \  
&& tar -xf php-5.2.17.tar.bz2 \  
&& cd php-5.2.17 \  
&& patch -p0 < $HOME/libxml29_compat.patch \  
&& ./configure --with-apxs2=/usr/local/apache2/bin/apxs --with-mysql --with-
mysqli --with-pdo-mysql --enable-mbstring \  
&& make -j"$(nproc)" \  
&& make install \  
&& cp php.ini-recommended $PHP_INI  
  
RUN echo '<FilesMatch \\.php$>' >> $HTTPD_CONF \  
&& echo ' SetHandler application/x-httpd-php' >> $HTTPD_CONF \  
&& echo '</FilesMatch>' >> $HTTPD_CONF  
  
RUN sed -i 's/"GPCS"/"EGPCS"/' $PHP_INI  
  
RUN pecl install xdebug-2.2.7 \  
&& echo 'zend_extension="/usr/local/lib/php/extensions/no-debug-non-
zts-20060613/xdebug.so"' >> $PHP_INI \  
&& echo 'xdebug.remote_enable=On' >> $PHP_INI \  
&& echo 'xdebug.remote_connect_back=On' >> $PHP_INI \  
&& echo 'xdebug.remote_autostart=On' >> $PHP_INI \  
&& echo 'xdebug.idekey="xdebug"' >> $PHP_INI  
  
WORKDIR $HTTPD_PREFIX/htdocs/  

