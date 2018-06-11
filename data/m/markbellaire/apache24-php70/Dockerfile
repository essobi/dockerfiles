FROM ubuntu:16.04  
  
RUN apt-get update -qq && apt-get install -yqq\  
software-properties-common\  
language-pack-en-base &&\  
export LC_ALL=en_US.UTF-8 &&\  
export LANG=en_US.UTF-8 &&\  
LC_ALL=en_US.UTF-8 add-apt-repository -y ppa:ondrej/php &&\  
apt-get update -qq && apt-get upgrade -yqq &&\  
apt-get install -yqq --no-install-recommends\  
apache2\  
apache2-utils\  
php7.0\  
php7.0-cli\  
php7.0-gd\  
php7.0-json\  
php7.0-mysql\  
php7.0-curl\  
php7.0-xml\  
php7.0-mbstring\  
php-xdebug\  
vim\  
&& rm -rf /var/lib/apt/lists/* &&\  
a2enmod rewrite  
  
EXPOSE 80  
  
CMD ["apachectl", "-D", "FOREGROUND"]  
  

