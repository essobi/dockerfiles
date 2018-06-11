FROM wrongsides/baseimage  
  
#Install Sickrage  
RUN apt-get -q update && apt-get install -qy git-core python python-openssl  
RUN git clone https://github.com/SickRage/SickRage.git /sickrage  
  
#Add start script  
ADD ./start.sh /start.sh  
RUN chmod u+x /start.sh  
  
VOLUME ["/config", "/data", "/cache"]  
  
EXPOSE 8081  
CMD ["/start.sh"]  

