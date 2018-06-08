FROM ubuntu  
  
MAINTAINER Manuel Rios <mriostamez@gmail.com>  
  
# Install packages  
RUN apt-get update && apt-get -y install apache2 supervisor git  
  
# Add scripts  
ADD start_apache.sh /start_apache.sh  
RUN chmod 755 /*.sh  
  
# Add apache to supervisord  
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf  
  
# config to enable .htaccess  
ADD apache_default /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
  
# Add sample volumes  
VOLUME ["/data_c"]  
  
# Expose port 80  
EXPOSE 80 3306  
CMD ["/start_apache.sh"]  
  
#Added comment  

