FROM linuxconfig/lamp  
MAINTAINER Lubos Rendek <web@linuxconfig.org>  
  
# Install prerequisites  
RUN apt-get update  
RUN apt-get install -y curl unzip  
  
# Download and unzip Wordpress  
RUN curl -s --output /tmp/wordpress.zip https://wordpress.org/latest.zip  
RUN rm -fr /var/www/html  
RUN unzip /tmp/wordpress.zip -d /tmp/  
RUN rm /tmp/wordpress.zip  
RUN mv /tmp/wordpress/ /var/www/html  
  
# Create database  
RUN service mysql start; mysqladmin -uadmin -ppass create wordpress  
  
# Update file ownership  
RUN chown -R www-data.www-data /var/www/html  
  
# Apache configuration  
ADD 000-default.conf /etc/apache2/sites-available/  
RUN a2enmod rewrite  
  
# Allow ports  
EXPOSE 80  
CMD ["supervisord"]  

