FROM mongo:3.7.3-jessie  
  
ADD start.sh ./start.sh  
ADD init-db.js ./init-db.js  
ADD init-rs.js ./init-rs.js  
  
RUN chmod +x ./start.sh &&\  
touch /var/log/mongod.log  
  
RUN mkdir /data/insync  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
EXPOSE 27017  
RUN mongod --fork --logpath /var/log/mongod.log --dbpath=/data/insync && mongo
init-db.js  
  
CMD ./start.sh &&\  
tail -f /var/log/mongod.log  

