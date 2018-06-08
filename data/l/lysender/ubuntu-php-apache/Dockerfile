FROM lysender/ubuntu-php  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
# Install Apache and misc tools  
RUN apt-get -y install supervisor \  
apache2 \  
libapache2-mod-php5 \  
openssl && apt-get clean  
  
# Configure servicies  
ADD ./start.sh /start.sh  
ADD ./start-apache2.sh /start-apache2.sh  
RUN chmod 755 /*.sh  
RUN mkdir -p /etc/supervisor/conf.d  
ADD ./supervisor-apache2.conf /etc/supervisor/conf.d/apache2.conf  
  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
ADD apache-default.conf /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
RUN a2enmod headers  
RUN a2enmod deflate  
RUN a2enmod env  
RUN a2enmod expires  
  
VOLUME ["/var/www/html", "/var/log/apache2"]  
  
EXPOSE 80  
CMD ["/bin/bash", "/start.sh"]  
  

