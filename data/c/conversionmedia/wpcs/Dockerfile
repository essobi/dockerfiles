FROM php:7.0-fpm  
  
WORKDIR /tmp  
  
RUN apt-get update -y \  
&& apt-get install -y wget unzip  
  
RUN wget https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar \  
&& chmod +x phpcs.phar \  
&& mv phpcs.phar /usr/local/bin/phpcs  
  
RUN wget https://github.com/WordPress-Coding-Standards/WordPress-Coding-
Standards/archive/master.zip \  
&& unzip master.zip \  
&& rm master.zip \  
&& mv WordPress-Coding-Standards-master wpcs \  
&& phpcs --config-set installed_paths `pwd`/wpcs \  
&& phpcs --config-set default_standard WordPress  
  
RUN wget https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar \  
&& chmod +x phpcbf.phar \  
&& mv phpcbf.phar /usr/local/bin/phpcbf  
  
RUN wget http://static.phpmd.org/php/latest/phpmd.phar \  
&& chmod +x phpmd.phar \  
&& mv phpmd.phar /usr/local/bin/phpmd  
  
USER www-data  
  
WORKDIR /source  

