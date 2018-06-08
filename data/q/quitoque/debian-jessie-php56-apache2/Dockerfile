FROM quitoque/debian-jessie-php56  
  
MAINTAINER Rémi Chomat <remi@quitoque.fr>  
  
RUN apt-get install -y apache2 libapache2-mod-php5  
RUN apt-get install -y -u -qq mysql-client  
  
RUN echo "\nServerName localhost" >> /etc/apache2/apache2.conf  
  
RUN a2enmod rewrite  
RUN echo "umask 002" >> /etc/apache2/envvars  
RUN a2enmod php5  
  
RUN service apache2 restart  
  
# Add user profideo to group www-data  
RUN usermod -a -G www-data quitoque  
  
EXPOSE 80  

