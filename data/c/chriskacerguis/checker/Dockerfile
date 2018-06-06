FROM php:5.6  
RUN apt-get update -y  
RUN apt-get install -y git \  
libmcrypt-dev \  
libreadline-dev \  
libpng-dev \  
wget \  
zip \  
unzip  
  
RUN curl --location --output /usr/local/bin/phpunit
https://phar.phpunit.de/phpunit-5.phar \  
&& chmod +x /usr/local/bin/phpunit  
  
# Install CodeSniffer  
RUN curl --location --output /usr/local/bin/phpcs
https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar \  
&& chmod +x /usr/local/bin/phpcs  
  
RUN curl --location --output /usr/local/bin/phpcbf
https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar \  
&& chmod +x /usr/local/bin/phpcbf  
  
RUN docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mcrypt  
  
# Install / Run composer  
# Install composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');"  

