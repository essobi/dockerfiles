FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y vim  
RUN apt-get install -y apache2  
RUN apt-get install -y php7.0 php7.0-zip  
RUN apt-get install -y libapache2-mod-php7.0  
RUN apt-get install -y php-mbstring phpunit  
RUN apt-get install -y composer  
RUN composer global require "laravel/installer"  
RUN export PATH=$PATH:~/.composer/vendor/bin  
RUN a2enmod rewrite  
RUN sed -i 's/\/var\/www\/html/\/var\/www\/laravel\/public\n DirectoryIndex
index.php\n <Directory "\/var\/www\/laravel\/public">\n Options Indexes
MultiViews FollowSymLinks\n AllowOverride All\n Allow from all\n
<\/Directory>/g' /etc/apache2/sites-enabled/000-default.conf  
  
RUN apt-get install -y php-mysql  
RUN sed -i 's/;extension=php_mysqli.dll/extension=php_mysqli.dll/g'
/etc/php/7.0/apache2/php.ini  
#RUN ~/.composer/vendor/bin/laravel new /var/www/laravel  
ENTRYPOINT /etc/init.d/apache2 start && /bin/bash  

