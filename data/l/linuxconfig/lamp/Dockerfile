FROM linuxconfig/apache  
MAINTAINER Lubos Rendek <web@linuxconfig.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Main package installation  
RUN apt-get update  
RUN apt-get -y install supervisor libapache2-mod-php7.0 php7.0-mysql mariadb-
server  
  
# Extra package installation  
RUN apt-get -y install php-gd php-apcu php-mcrypt php7.0-xml  
  
# Configure MariaDB  
RUN sed -i 's/bind-address/#bind-address/' /etc/mysql/my.cnf  
  
# Include supervisor configuration  
ADD supervisor-lamp.conf /etc/supervisor/conf.d/  
ADD supervisord.conf /etc/supervisor/  
  
# Include PHP Info page  
ADD index.php /var/www/html/index.php  
  
# Create new MariaDB admin user  
RUN service mysql start; mysql -u root -e "CREATE USER 'admin'@'%' IDENTIFIED
BY 'pass';";mysql -u root -e "GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' WITH
GRANT OPTION;";  
  
# Allow ports  
EXPOSE 80 3306  
# Start supervisor  
CMD ["supervisord"]  
  

