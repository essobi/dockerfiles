FROM mongo:3.6  
#Setup replica configuration file  
COPY config/mongo-replica.conf /etc/mongo-replica.conf  
  
#Copy script to start mongo servers  
COPY scripts/startMongo.sh /usr/local/bin/startMongo.sh  
COPY scripts/initMongoReplica.sh /usr/local/bin/initMongoReplica.sh  
  
#Create dbpath directories  
RUN mkdir -p /data/db1 /data/db2 /data/db3 \  
&& chown -R mongodb:mongodb /data/db1 /data/db2 /data/db3  
  
#Run the mongo servers  
CMD ["/usr/local/bin/startMongo.sh"]  

