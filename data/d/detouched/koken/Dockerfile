FROM richarvey/nginx-php-fpm:latest  
  
RUN wget -P /var/www/html https://s3.amazonaws.com/koken-
installer/releases/Koken_Installer.zip \  
&& unzip /var/www/html/Koken_Installer.zip -d /var/www/html \  
&& mv /var/www/html/koken/index.php /var/www/html/index.php \  
&& chmod 777 /var/www/html/index.php \  
&& rm -r /var/www/html/koken /var/www/html/Koken_Installer.zip  

