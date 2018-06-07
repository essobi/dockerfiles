FROM resin/rpi-raspbian  
  
RUN apt-get update && apt-get install -y nginx php5-fpm php5-cgi php5-cli
php5-common  
RUN useradd www-data && groupadd www-data && usermod -g www-data www-data &&
mkdir /var/www && chmod 775 /var/www -R && chown www-data:www-data /var/www  
  
ADD default-config /etc/nginx/sites-enabled/default  
ADD cloud-config /usr/share/nginx/html/  
ADD ipxe /usr/share/nginx/html/  

