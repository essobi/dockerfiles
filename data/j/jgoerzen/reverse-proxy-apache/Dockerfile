FROM jgoerzen/debian-base-apache:stretch  
  
COPY preinit/ /usr/local/preinit/  
COPY conf-available/ /etc/apache2/conf-available/  
COPY sites-available/ /etc/apache2/sites-available/  
COPY scripts/ /usr/local/bin/  
  
RUN a2enmod proxy proxy_http headers rewrite && \  
a2enconf docker-ssl docker-log && \  
touch /etc/apache2/local-certbot-domainlist.txt && \  
apache2ctl configtest && \  
/usr/local/bin/docker-wipelogs  
  
EXPOSE 80 443  
CMD ["/usr/local/bin/boot-debian-base"]  

