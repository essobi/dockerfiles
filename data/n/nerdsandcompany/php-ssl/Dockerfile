FROM nerdsandcompany/php-base  
MAINTAINER Bob Olde Hampsink <b.oldehampsink@nerds.company>  
  
# Add required modules for SSL (these are disabled by default)  
RUN a2enmod socache_shmcb ssl  
  
# Update the reference for the certificate file so it uses the .crt extension
instead of .pem  
RUN sed -i.bak s/snakeoil.pem/snakeoil.crt/ /etc/apache2/sites-
available/default-ssl.conf  
RUN a2ensite default-ssl  
  
COPY apache-sites/http-redirect.conf /etc/apache2/sites-available/http-
redirect.conf  
RUN a2ensite http-redirect  

