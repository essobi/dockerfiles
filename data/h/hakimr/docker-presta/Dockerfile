FROM debian:jessie-slim  
  
RUN apt update && apt install -y wget unzip && \  
echo 'deb http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list && \  
echo 'deb-src http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list
&& \  
wget https://www.dotdeb.org/dotdeb.gpg && \  
apt-key add dotdeb.gpg && \  
apt update && apt upgrade -y -qq && \  
apt install -y apache2 php7.0 libapache2-mod-php7.0 php7.0-zip php7.0-xml
php7.0-curl php7.0-gd php7.0-intl php7.0-mysql && \  
a2enmod rewrite  
  
WORKDIR /var/www/html  
  
RUN rm index.html && \  
wget https://download.prestashop.com/download/releases/prestashop_1.7.0.6.zip
&& \  
unzip prestashop_1.7.0.6.zip && \  
rm prestashop_1.7.0.6.zip && \  
chown -R www-data:www-data .  
  
CMD ["apache2ctl", "-D FOREGROUND"]  

