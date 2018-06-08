FROM mongo:3.4.3  
VOLUME /data/db  
  
ADD run.sh set_mongodb_password.sh /  
  
# Make files executable  
RUN \  
chmod 0777 /run.sh && \  
chmod 0777 /set_mongodb_password.sh  
  
ENV rootPwd= \  
  
# Password for the database:  
dataPwd= \  
  
# Username for the database:  
dataUser=data \  
  
# Name of the database:  
dataName=Data  
  
EXPOSE 27017  
CMD ["/run.sh"]  

