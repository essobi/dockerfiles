FROM slogsdon/develop-base  
  
RUN \  
sudo apt-get install -y \  
php5-cli \  
php5-curl \  
php5-gd \  
php5-intl \  
php5-mcrypt \  
php5-mysql \  
php5-xdebug \  
php5-xsl \  
&&\  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" &&\  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'92102166af5abdb03f49ce52a40591073a7b859a86e8ff13338cf7db58a19f7844fbc0bb79b2773bf30791e935dbd938')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" &&\  
php composer-setup.php &&\  
php -r "unlink('composer-setup.php');" &&\  
sudo mv composer.phar /usr/local/bin/composer  

