FROM ubuntu:14.04  
MAINTAINER Jeffery Utter "jeff.utter@firespring.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN mkdir -p /var/run/apache2 /var/lock/apache2  
  
# Clear out any existing postfix and re-configure  
RUN apt-get remove -y --purge postfix  
RUN echo "postfix postfix/main_mailer_type select Internet with smarthost" |
debconf-set-selections  
RUN echo "postfix postfix/mailname string mail.example.com" | debconf-set-
selections  
RUN echo "postfix postfix/relayhost string [smtp.mandrillapp.com]:587" |
debconf-set-selections  
  
RUN apt-get update \  
&& apt-get install -y \  
# Apache\PHP  
apache2 libapache2-mod-gnutls php5 php5-mysql php5-curl php-pear php5-gd php-
xml-parser php5-dev \  
# Mogile  
libxml2-dev libneon27-dev \  
# Build Deps  
build-essential curl make \  
# Other Deps  
pdftk zip postfix libsasl2-modules git zlib1g-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -s -o phpunit-3.7.31.phar https://phar.phpunit.de/phpunit-3.7.31.phar
\  
&& chmod 777 phpunit-3.7.31.phar \  
&& mv phpunit-3.7.31.phar /usr/local/bin/phpunit  
  
RUN pecl install xdebug-2.2.6 \  
&& pear install PHP_CodeSniffer \  
&& pecl install memcache \  
&& pecl install redis \  
&& pecl install zip \  
&& pecl install mogilefs-0.9.2  
  
RUN php5enmod zip  
  
RUN a2enmod ssl \  
&& a2enmod php5 \  
&& a2enmod rewrite  
  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
# Apache Config  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APPLICATION_ENV local  
  
COPY apache2/apache2.conf /etc/apache2/  
COPY php/conf.d/ /etc/php5/apache2/conf.d/  
COPY php/conf.d/ /etc/php5/cli/conf.d/  
  
COPY apache2-foreground /usr/local/bin/  
  
CMD ["apache2-foreground"]  

