#docker build -t sauloal/lamp --rm=true .  
FROM tutum/lamp  
  
RUN a2enmod cgi  
  
VOLUME ["/etc/mysql", "/var/lib/mysql" ]  
  
EXPOSE 80 3306  
CMD ["/run.sh"]  
  

