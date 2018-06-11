FROM mongo:3.0.6  
MAINTAINER Kevin Kuhl <kevin@wayblazer.com>  
  
RUN apt-get update && apt-get -y install supervisor pwgen  
  
ADD run.sh /run.sh  
ADD set_mongodb_password.sh /set_mongodb_password.sh  
ADD create_mongodb_users.sh /create_mongodb_users.sh  
RUN chmod +x /create_mongodb_users.sh /set_mongodb_password.sh  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
  
ENV AUTH yes  
ENV STORAGE_ENGINE wiredTiger  
ENV JOURNALING yes  
  
#The parent provides /data/db as the database storage location  
RUN mkdir /logs  
VOLUME [/logs]  
EXPOSE 27017 28017  
CMD ["/run.sh"]  

