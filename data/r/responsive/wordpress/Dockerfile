FROM phusion/baseimage:0.9.18  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install supervisor git apache2 libapache2-mod-php5 mysql-server
php5-mysql pwgen php-apc php5-mcrypt && \  
echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
# Add image configuration and scripts  
ADD start-apache2.sh /start-apache2.sh  
ADD start-mysqld.sh /start-mysqld.sh  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
ADD my.cnf /etc/mysql/conf.d/my.cnf  
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf  
ADD supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf  
  
# Remove pre-installed database  
RUN rm -rf /var/lib/mysql/*  
  
# Add MySQL utils  
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh  
RUN chmod 755 /*.sh  
  
# config to enable .htaccess  
ADD apache_default /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
  
# Configure /app folder with sample app  
RUN git clone https://github.com/fermayo/hello-world-lamp.git /app  
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html  
  
#Environment variables to configure php  
ENV PHP_UPLOAD_MAX_FILESIZE 1000M  
ENV PHP_POST_MAX_SIZE 10M  
  
# Add volumes for MySQL  
VOLUME ["/etc/mysql", "/var/lib/mysql" ]  
  
# Install plugins  
RUN apt-get -y install php5-gd wget\  
&& rm -rf /var/lib/apt/lists/*  
  
# Download latest version of Wordpress into /app  
RUN rm -fr /app && git clone \--depth=1
https://github.com/WordPress/WordPress.git /app  
  
# Configure Wordpress to connect to local DB  
ADD wp-config.php /app/wp-config.php  
  
# Modify permissions to allow plugin upload  
RUN chown -R www-data:www-data /app/wp-content /var/www/html  
  
# Add database setup script  
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh  
ADD create_db.sh /create_db.sh  
RUN chmod +x /*.sh  
  
EXPOSE 80 3306  
CMD ["/run.sh"]  

