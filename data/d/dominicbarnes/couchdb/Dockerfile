# currently based on couchdb v1 as v2's clustering is harder to configure.
I'll  
# eventually add support for both.  
FROM couchdb:1  
# install couchdb-bootstrap + dependencies (nodejs)  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash  
RUN apt-get install -y nodejs netcat  
RUN npm install -g couchdb-bootstrap  
  
# mount to this volume to automatically bootstrap the database on startup  
RUN mkdir /docker-entrypoint-init.d  
VOLUME "/docker-entrypoint-init.d"  
  
# put the entrypoint script into the $PATH so it can be accessed without an  
# absolute path  
COPY docker-entrypoint.sh /usr/local/bin/  
  
# the entrypoint here will invoke the base image's entrypoint script  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["couchdb"]  

