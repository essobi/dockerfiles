FROM quitoque/ubuntu16-04-php7  
  
MAINTAINER Rémi Chomat <remi@quitoque.fr>  
  
# Remove default site  
# Configure apache  
# Add user quitoque to group www-data  
RUN apt-get update && apt-get install -y -qq apache2 libapache2-mod-php7.0 &&
\  
echo "\nServerName localhost" >> /etc/apache2/apache2.conf && \  
rm /etc/apache2/sites-enabled/*default*.conf && \  
echo "umask 002" >> /etc/apache2/envvars && \  
a2enmod rewrite php7.0 deflate && \  
usermod -a -G www-data quitoque && \  
apt-get -qq -y autoremove && apt-get -qq -y autoclean && \  
apt-get -qq -y clean && rm -rf /var/lib/apt/lists/*  
  
COPY files/deflate.conf /etc/apache2/mods-available/deflate.conf  
  
EXPOSE 80  

