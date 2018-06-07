FROM wordpress:4.7.0  
MAINTAINER Paul-Willy Jean <pwjean@maysys.com>  
  
HEALTHCHECK CMD curl http://localhost/  
COPY install.sh /usr/local/bin/install  
RUN chmod +x /usr/local/bin/install  
COPY src /usr/src/wordpress/  
RUN chown -R www-data:www-data /usr/src/wordpress

