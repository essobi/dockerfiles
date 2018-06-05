FROM lucidprogrammer/apache-php7-composer-pgsql-mysql:latest  
  
RUN echo "Alias /saml /var/www/html/vendor/simplesamlphp/simplesamlphp/www" >>
/etc/apache2/apache2.conf  
RUN echo "<Directory
\"/var/www/html/vendor/simplesamlphp/simplesamlphp/www/\"> \n Options Indexes
FollowSymLinks \n AllowOverride all \n Require all granted \n </Directory>" >>
/etc/apache2/apache2.conf  

