FROM php:7.1  
WORKDIR /root  
  
RUN apt-get update \  
&& apt-get install -y wget \  
&& apt-get install -y unzip  
  
RUN wget https://github.com/roistat/php-obfuscator/archive/master.zip \  
&& unzip master.zip \  
&& rm master.zip  
  
RUN cd /root/php-obfuscator-master \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php --install-dir=/usr/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');" \  
&& php /usr/bin/composer install  
  
RUN ln -s /root/php-obfuscator-master/bin/obfuscate /bin/obfuscate  

