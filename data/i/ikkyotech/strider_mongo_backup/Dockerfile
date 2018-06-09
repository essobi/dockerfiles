# DOCKER-VERSION 1.0.0  
FROM ikkyotech/strider_simple:latest  
MAINTAINER "Martin Heidegger" <mh@ikkyotech.com>  
  
RUN echo "0 * * * * * /usr/local/bin/mongo_backup.sh\n" >> /etc/crontab  
  
ADD ./startup.sh /usr/local/bin/startup.sh  
ADD ./mongo_restore.sh /usr/local/bin/mongo_restore.sh  
ADD ./mongo_backup.sh /usr/local/bin/mongo_backup.sh  
  
RUN chmod 755 /usr/local/bin/*  
RUN chmod +x /usr/local/bin/*  
  
# Startup all the tasks  
CMD ["/usr/local/bin/startup.sh"]  
  
EXPOSE 3000

