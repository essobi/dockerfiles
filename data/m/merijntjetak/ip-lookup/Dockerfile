FROM debian:jessie  
  
RUN apt-get update && apt-get install -y apache2  
RUN a2enmod cgi  
  
RUN mkdir -p /var/www/html/api  
ADD index.pl /var/www/html/  
ADD about.html /var/www/html/  
RUN chmod +x /var/www/html/index.pl  
RUN ln -s /var/www/html/index.pl /var/www/html/api/index.pl  
  
ADD apache.conf /etc/apache2/sites-available/000-default.conf  
ADD apache2-foreground /usr/local/bin/  
RUN chmod +x /usr/local/bin/apache2-foreground  
  
WORKDIR /var/www/html/  
  
EXPOSE 80  
CMD ["/usr/local/bin/apache2-foreground"]  

