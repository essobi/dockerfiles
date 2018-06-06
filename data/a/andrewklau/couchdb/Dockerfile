FROM couchdb:1.6.1  
  
RUN apt-get update && apt-get install -y rsync && \  
mkdir -p \  
/usr/local/var/lib/couchdb \  
/usr/local/var/log/couchdb \  
/usr/local/var/run/couchdb \  
/usr/local/etc/couchdb && \  
chown -R couchdb.0 \  
/usr/local/var/lib/couchdb \  
/usr/local/var/log/couchdb \  
/usr/local/var/run/couchdb \  
/usr/local/etc/couchdb && \  
# Loosen permission bits to avoid problems running container with arbitrary
UID  
chmod -R g+rwx \  
/usr/local/var/lib/couchdb \  
/usr/local/var/log/couchdb \  
/usr/local/var/run/couchdb \  
/usr/local/etc/couchdb \  
/usr/local/etc/couchdb/*.d && \  
chmod g+w -R /usr/local/etc/couchdb/*.ini  
  
# Copy executable utilities.  
COPY bin/ /usr/bin/  
COPY docker-entrypoint.sh /  
  
USER couchdb  

