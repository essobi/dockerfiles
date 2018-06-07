FROM drupal:7.44-fpm  
  
RUN \  
php -r "readfile('http://files.drush.org/drush.phar');" > drush \  
&& chmod +x drush \  
&& mv drush /usr/local/bin \  
&& drush -y init  
RUN \  
touch /var/www/html/sites/default/drushrc.php \  
&& curl -sL https://raw.githubusercontent.com/drush-
ops/drush/master/examples/example.drushrc.php >
/var/www/html/sites/default/drushrc.php \  
&& echo "ini_set('memory_limit', '512M');" >>
/var/www/html/sites/default/drushrc.php  
RUN \  
apt update \  
&& apt install --yes mysql-client sudo php5-ssh2 vim  
RUN \  
docker-php-ext-install gd mbstring ftp zip mysqli opcache  

