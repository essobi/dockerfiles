FROM devwithlando/php:7.2-fpm  
  
RUN apt-get -yqq update  
  
#########  
# OroCommerce prefers that node or another JS Engine be made available to it  
RUN apt install -yq nodejs  
  
##########  
# PHP-INTL - OroCommerce Dependencies  
# Lando ships with INTL but we need a more recent version  
RUN apt-get -yqq install zlib1g-dev libicu-dev g++  
  
RUN curl -sS -o /tmp/icu.tar.gz -L http://download.icu-
project.org/files/icu4c/57.1/icu4c-57_1-src.tgz \  
&& tar -zxf /tmp/icu.tar.gz -C /tmp \  
&& cd /tmp/icu/source \  
&& ./configure --prefix=/usr/local \  
&& make \  
&& make install  
  
RUN docker-php-ext-configure intl --with-icu-dir=/usr/local  
RUN docker-php-ext-install intl  
  
##########  
# PHP-TIDY - OroCommerce Dependencies  
RUN apt-get -yqq install libtidy-dev  
RUN docker-php-ext-install tidy  

