FROM php:7.1-apache  
  
RUN apt-get update && apt-get install -y \  
subversion \  
libmcrypt-dev \  
curl \  
git \  
zlib1g-dev \  
mysql-client \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install pcntl \  
&& docker-php-ext-install bcmath \  
&& docker-php-ext-install pdo_mysql  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"\  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'55d6ead61b29c7bdee5cccfb50076874187bd9f21f65d8991d46ec5cc90518f447387fb9f76ebae1fbbacf329e583e30')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;"\  
&& php composer-setup.php\  
&& php -r "unlink('composer-setup.php');"\  
&& mv composer.phar /usr/bin/composer  
RUN echo 'export PHP=/usr/local/bin/php' >> /etc/bash.bashrc  
RUN a2enmod rewrite  
ADD site-default.conf /etc/apache2/sites-available  
RUN a2dissite 000-default.conf  
RUN a2ensite site-default.conf  
RUN service apache2 restart  
WORKDIR /var/www/html  

