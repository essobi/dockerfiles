from php:7-cli  
  
RUN apt-get update && apt-get install git unzip -y  
  
ADD src /app/src  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;"  
RUN php composer-setup.php  
RUN php -r "unlink('composer-setup.php');"  
  
ADD composer.json composer.json  
RUN php composer.phar install  
  
ENTRYPOINT ["php", "/app/src/main.php"]

