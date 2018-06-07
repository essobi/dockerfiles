FROM drupal:8.5.3-apache  
  
MAINTAINER Jungle Ran <jungle.r@intergreat.com>  
  
# Modify default apache docroot.  
RUN sed -i "s/\/var\/www\/html/\/var\/www\/html\/web/g" /etc/apache2/sites-
available/000-default.conf  
  
# Install git.  
RUN apt-get update; apt-get install git -y  
  
# Extensions: uploadprogress, bcmath, mcrypt.  
RUN git clone https://github.com/Jan-E/uploadprogress.git /tmp/php-
uploadprogress \  
&& cd /tmp/php-uploadprogress \  
&& phpize \  
&& ./configure --prefix=/usr\  
&& make \  
&& make install \  
&& echo 'extension=uploadprogress.so' >
/usr/local/etc/php/conf.d/uploadprogress.ini \  
&& rm -rf /tmp/* \  
&& docker-php-ext-install bcmath \  
&& apt install libmcrypt-dev -y \  
&& pecl install mcrypt-1.0.1 \  
&& docker-php-ext-enable mcrypt  
  
# Extensions: soap, mongodb, ssh2.  
RUN apt-get install libxml2-dev -y \  
&& docker-php-ext-install soap \  
&& pecl install mongodb \  
&& docker-php-ext-enable mongodb \  
&& apt-get install libssh2-1-dev -y \  
&& pecl install ssh2-1.1.2 \  
&& docker-php-ext-enable ssh2  

