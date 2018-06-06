FROM nrel/openstudio:1.8.5  
  
RUN apt-get update -y && \  
apt-get install -y mongodb && \  
rm -rf /var/lib/apt/lists/* \  
service mongodb start  
  
COPY start-mongodb.sh /sbin/start-mongodb.sh  
RUN chmod 755 /sbin/start-mongodb.sh  
  
# EXPOSE 27017/tcp  

