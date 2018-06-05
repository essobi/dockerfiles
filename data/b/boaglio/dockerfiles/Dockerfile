FROM ubuntu  
MAINTAINER Fernando Boaglio <fernando@boaglio.com>  
  
RUN apt-get update && apt-get install -y \  
apache2 \  
tor \  
tor-arm  
RUN rm -rf /var/cache/apt*  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
EXPOSE 9001 9050 9100  
COPY torrc /etc/tor/torrc  
COPY index.html /var/www/html/  
COPY tor.png /var/www/html/  
  
VOLUME ["/var/lib/log/tor/","/var/lib/tor/","/var/www", "/var/log/apache2",
"/etc/apache2"]  
  
ADD start.sh /opt/start.sh  
RUN chmod +x /opt/start.sh  
  
CMD ["/opt/start.sh"]  

