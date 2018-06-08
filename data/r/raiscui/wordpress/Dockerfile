FROM tutum/wordpress-stackable:latest  
  
RUN apt-get update && \  
apt-get -yq install php5-memcached && \  
apt-get -yq install php5-memcache && \  
a2enmod headers && \  
a2enmod expires && \  
rm -rf /var/lib/apt/lists/*  
  
ENV DB_HOST **LinkMe**  
ENV DB_PORT **LinkMe**  
ENV DB_NAME wordpress  
ENV DB_USER admin  
ENV DB_PASS **ChangeMe**  
  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
EXPOSE 80  
VOLUME ["/app"]  
CMD ["/run-wordpress.sh"]  

