FROM java:7-jre  
MAINTAINER José Juan Escudero  
  
RUN apt-get update && apt-get install -y apache2 supervisor vim  
  
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/plugins
/var/log/supervisor /srv/eclipse  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
COPY eclipse /srv/eclipse  
  
ADD init.sh /usr/bin/  
  
RUN chmod +x /usr/bin/init.sh  
  
EXPOSE 8080  
VOLUME /var/plugins  
  
CMD ["/usr/bin/supervisord"]

