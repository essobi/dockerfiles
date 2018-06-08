FROM php:5-apache  
RUN apt-get update  
RUN bash -c 'debconf-set-selections <<< "mariadb-server mysql-
server/root_password password rootpass" '  
RUN bash -c 'debconf-set-selections <<< "mariadb-server mysql-
server/root_password_again password rootpass" '  
RUN apt-get install -y mariadb-server mariadb-client zip libxml2-dev libpng-
dev  
RUN docker-php-ext-install mysql simplexml mbstring gd  
RUN service mysql start; mysql --password=rootpass -e 'create database smf;'  
ADD http://download.simplemachines.org/index.php/smf_2-0-11_install.tar.gz
/var/www/  
RUN mkdir /var/www/smf; cd /var/www/smf; tar xfz ../smf_2-0-11_install.tar.gz  
ADD smf.conf /etc/apache2/sites-enabled/  
WORKDIR /var/www/smf  
RUN chmod 777 attachments avatars cache Packages Packages/installed.list
Smileys Themes agreement.txt Settings.php Settings_bak.php  
  
EXPOSE 80  
CMD service mysql start; apache2-foreground  

