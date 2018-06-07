FROM ubuntu:12.04  
MAINTAINER Marcelo Rodrigo <mrodrigow@gmail.com>  
ENV DOCUMENTROOT=public_html  
  
# Update packages and install apache + php5.3  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update && \  
apt-get -yq install --no-install-recommends \  
curl \  
php5 \  
php5-gd \  
php5-mysql \  
php5-mcrypt \  
php5-curl \  
apache2 && \  
rm -rf /var/lib/apt/lists/*  
  
# Configuring apache2 and php  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
sed -i".bak" "s/AllowOverride None/AllowOverride All/g" /etc/apache2/sites-
available/default && \  
a2enmod rewrite  
  
# Configuring /app  
RUN mkdir -p /app && mkdir -p /app/$DOCUMENTROOT && \  
rm -rf /var/www && \  
ln -s /app/$DOCUMENTROOT /var/www  
  
ADD public_html /app/$DOCUMENTROOT  
WORKDIR /app  
EXPOSE 80  
CMD chown -R www-data:www-data /app && \  
service apache2 restart && \  
tail -F /var/log/apache2/*  

