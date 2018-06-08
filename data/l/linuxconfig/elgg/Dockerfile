FROM linuxconfig/lamp  
MAINTAINER Lubos Rendek <web@linuxconfig.org>  
  
# Install prerequisites  
RUN apt-get install -y wget unzip  
  
# Download and unzip Elgg  
RUN wget -qO /tmp/elgg.zip https://www.elgg.org/download/elgg-1.11.1.zip  
RUN rm -fr /var/www/html  
RUN unzip /tmp/elgg.zip -d /tmp/  
RUN rm /tmp/elgg.zip  
RUN mv /tmp/elgg-* /var/www/html  
  
# Create database  
RUN service mysql start; mysqladmin -uadmin -ppass create elgg  
  
# Apache configuration  
ADD 000-default.conf /etc/apache2/sites-available/  
RUN a2enmod rewrite  
  
# Elgg configurations  
RUN mkdir /var/www/html/data  
  
# Update file and directory ownership  
RUN chown -R www-data.www-data /var/www/html  
  
# Allow ports  
EXPOSE 80  
CMD ["supervisord"]

