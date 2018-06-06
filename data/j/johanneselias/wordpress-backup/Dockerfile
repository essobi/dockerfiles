FROM johanneselias/ubuntu1704-apache2-php-perl:1.0  
RUN apt-get -y update && apt-get install -y \  
mysql-client  
  
WORKDIR /setup  
RUN wget https://wordpress.org/latest.tar.gz; \  
tar xzvf latest.tar.gz; \  
touch /setup/wordpress/.htaccess; \  
chmod 660 /setup/wordpress/.htaccess; \  
cp /setup/wordpress/wp-config-sample.php /setup/wordpress/wp-config.php; \  
mkdir /setup/wordpress/wp-content/upgrade  
  
RUN wget https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar; \  
chmod +x wp-cli.phar; \  
mv wp-cli.phar /usr/local/bin/wp; \  
echo "alias wpc='wp --allow-root'" > /root/.bash_aliases  
  
COPY helper/wordpress-* /usr/bin/  
  
RUN chmod 700 /usr/bin/wordpress-*  
  
ENTRYPOINT ["wordpress-configure"]  
  

