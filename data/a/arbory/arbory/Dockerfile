FROM ubuntu:16.04  
RUN apt-get update -qq && apt-get install -y git unzip software-properties-
common curl apt-transport-https mysql-client  
# Add PHP 7.1 repository  
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php  
# Add yarn repository  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
# Add node 8.x repository  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
  
# apt-get update is called by node setup script already  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
\  
php7.1-cli \  
php7.1-mysql \  
php7.1-zip \  
php7.1-mbstring \  
php7.1-xml \  
php7.1-curl \  
php7.1-dom \  
php7.1-fpm \  
php7.1-soap \  
nodejs \  
yarn  
  
# Configure FPM to run properly on docker  
RUN sed -i "s/upload_max_filesize = .*/upload_max_filesize = 10M/"
/etc/php/7.1/fpm/php.ini  
RUN sed -i "s/post_max_size = .*/post_max_size = 12M/"
/etc/php/7.1/fpm/php.ini  
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/"
/etc/php/7.1/fpm/php.ini  
  
RUN sed -i -e "s/pid =.*/pid = \/var\/run\/php7.1-fpm.pid/"
/etc/php/7.1/fpm/php-fpm.conf  
RUN sed -i -e "s/error_log =.*/error_log = \/proc\/self\/fd\/2/"
/etc/php/7.1/fpm/php-fpm.conf  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.1/fpm/php-
fpm.conf  
RUN sed -i "s/listen = .*/listen = 9000/" /etc/php/7.1/fpm/pool.d/www.conf  
RUN sed -i "s/;catch_workers_output = .*/catch_workers_output = yes/"
/etc/php/7.1/fpm/pool.d/www.conf  
RUN sed -i "s/;clear_env = no/clear_env = no/"
/etc/php/7.1/fpm/pool.d/www.conf  
  
# Supress composer root warning  
ENV COMPOSER_ALLOW_SUPERUSER=1  
# Copy composer from already built image  
COPY \--from=composer:1.6 /usr/bin/composer /usr/bin/composer  

