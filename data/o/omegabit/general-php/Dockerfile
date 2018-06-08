FROM ubuntu:16.04  
ADD https://getcomposer.org/installer composer-setup.php  
  
RUN /bin/bash -c "apt-get update"  
RUN /bin/bash -c "apt-get upgrade -y"  
RUN /bin/bash -c "apt-get install -y \  
curl \  
php7.0 \  
php7.0-mysql \  
php7.0-intl \  
php7.0-xml \  
git \  
git-flow \  
zsh"  
RUN /bin/bash -c "curl -LsS https://symfony.com/installer -o
/usr/local/bin/symfony && chmod a+x /usr/local/bin/symfony"  
RUN /bin/bash -c "php composer-setup.php && php -r \"unlink('composer-
setup.php');\" && mv composer.phar /usr/local/bin/composer"  
RUN /bin/bash -c "apt-get update"  
RUN /bin/bash -c "apt-get upgrade -y"  

