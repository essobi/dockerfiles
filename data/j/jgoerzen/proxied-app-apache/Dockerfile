FROM jgoerzen/debian-base-apache:stretch  
  
COPY preinit/ /usr/local/preinit/  
COPY conf-available/ /etc/apache2/conf-available/  
COPY sites-available/ /etc/apache2/sites-available/  
  
RUN touch /etc/apache2/authorized-proxies.txt && \  
a2enconf docker-proxy-client && \  
a2enmod setenvif remoteip && \  
apache2ctl configtest && \  
/usr/local/bin/docker-wipelogs  
  
CMD ["/usr/local/bin/boot-debian-base"]  

