FROM php:7.1  
  
RUN apt-get update  
  
RUN apt-get install -y libcurl4-openssl-dev  
RUN apt-get install -y sudo  
RUN apt-get install -y git  
RUN apt-get install -y libxslt-dev  
RUN apt-get install -y zlib1g-dev  
#RUN apt-get install -y graphviz  
RUN apt-get install -y zip  
RUN apt-get install -y libmcrypt-dev  
#RUN apt-get install -y libicu-dev  
#RUN apt-get install -y libpcre3-dev  
#RUN apt-get install -y libgd-dev  
#RUN apt-get install -y libfreetype6-dev  
  
RUN docker-php-ext-install soap  
RUN docker-php-ext-install zip  
RUN docker-php-ext-install xsl  
RUN docker-php-ext-install mcrypt  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install gettext  
RUN docker-php-ext-install curl  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install json  
#RUN docker-php-ext-install intl  
RUN docker-php-ext-install opcache  
  
#RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-
jpeg-dir=/usr/include/ --with-png-dir=/usr/include/ \  
# && docker-php-ext-install gd  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# CLEAN UP #################################################################  
RUN apt-get clean -y && \  
apt-get autoclean -y && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* /var/lib/log/* /tmp/* /var/tmp/*  

