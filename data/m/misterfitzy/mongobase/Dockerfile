FROM mongo  
  
RUN apt-get -y update && apt-get install -y git && mkdir -p /tmp/substrate  
  
# RUN git clone https://c6eb96df78d835dc72e2b3fc4efbb84d78dfcdfd:x-oauth-
basic@github.com/misterfitzy/substrate.git /tmp/substrate  
# RUN /usr/bin/mongod && mongorestore /tmp/substrate/substrate.db.bkup && rm
-fr /tmp/substrate  
COPY mongo_start_and_restore.sh /mongo_start_and_restore.sh  
RUN chmod 755 /mongo_start_and_restore.sh  
  
# ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 27017  
CMD ["/usr/bin/mongod"]  
## end  

