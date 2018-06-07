FROM php:7.1  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get update
&& apt-get -y install apt-transport-https libpq-dev libzip-dev git curl wget
libpng12-dev libgmp-dev ssh python-dev nano nodejs git  
RUN node -v  
RUN docker-php-ext-install pdo pdo_pgsql pgsql zip bcmath gd calendar gmp  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - & echo
"deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list & apt-get update && apt-get -y --force-yes
install yarn  
MAINTAINER Pawel Kolanecki <p.kolanecki@sygnisoft.com>  

