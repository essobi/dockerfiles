FROM ipunktbs/nginx:1.10.2-7-1.4.0  
ADD . /var/www/app  
WORKDIR /var/www/app  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
trim(file_get_contents('https://composer.github.io/installer.sig')) ) { echo
'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-
setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php \  
php -r "unlink('composer-setup.php');" \  
&& cd /var/www/app && ./composer.phar install && rm composer.phar  

