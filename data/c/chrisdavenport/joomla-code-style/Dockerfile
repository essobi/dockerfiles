FROM php:7.0.19-cli  
  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
zip \  
unzip \  
git \  
software-properties-common \  
zlib1g-dev \  
libxslt-dev \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install xsl \  
&& php -r "readfile('http://getcomposer.org/installer');" | php -- --install-
dir=/usr/bin/ \--filename=composer \  
&& pear install PHP_CodeSniffer-1.5.6 \  
&& git clone https://github.com/joomla/coding-standards.git --branch 1.x
--single-branch `pear config-get php_dir`/PHP/CodeSniffer/Standards/Joomla  
  

