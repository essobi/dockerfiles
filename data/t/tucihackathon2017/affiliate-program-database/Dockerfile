FROM mongo:3.4.9  
COPY mongo_create.sh /opt/mongo_create.sh  
RUN chmod a+x /opt/mongo_create.sh  
RUN /opt/mongo_create.sh  
EXPOSE 27017  

