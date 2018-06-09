FROM ubuntu:14.04  
ADD stuff/* /  
RUN apt-get update && \  
apt-get install -y apache2 apache2-utils vim curl telnet && \  
apt-get clean && \  
unlink /etc/apache2/sites-enabled/000-default.conf && \  
mkdir -p /var/www/example.com/public_html && \  
mv /index.html /var/www/example.com/public_html/ && \  
mv /image.jpg /var/www/example.com/public_html/ && \  
mv /logo.png /var/www/example.com/public_html/ && \  
mv /example.com.conf /etc/apache2/sites-available/ && \  
ln -s /etc/apache2/sites-available/example.com.conf /etc/apache2/sites-
enabled/  
  
EXPOSE 80  
CMD ["apachectl","-D","FOREGROUND"]  

