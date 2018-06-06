FROM debian:jessie-slim  
  
MAINTAINER Daniel Fišer <daniel@fiser.cz>  
  
# MongoDB  
# -------  
# Add MongoDB 3.4 public GPG key.  
RUN \  
apt-get update && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6  
# Create a /etc/apt/sources.list.d/mongodb-org-3.4.list file for MongoDB.  
RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.4 main"
>> /etc/apt/sources.list.d/mongodb-org-3.4.list  
# Install MongoDB, Community Edition.  
RUN \  
apt-get update && \  
apt-get install -y mongodb-org-server && \  
rm -rf /var/lib/apt/lists/*  
  
# Define and create MongoDB mountable directories.  
RUN \  
/usr/bin/perl -pi -e 's#dbPath: /var/lib/mongodb#dbPath: /mongodb/db#;s#path:
/var/log/mongodb/mongod.log#path: /mongodb/mongod.log#' /etc/mongod.conf && \  
mkdir -p /mongodb/db && \  
chown -R mongodb:nogroup /mongodb  
  
# Expose /mongodb as VOLUME.  
VOLUME ["/mongodb"]  
  
# Expose MongoDB ports.  
EXPOSE 27017  
# Start MongoDB server.  
USER mongodb  
WORKDIR /mongodb  
ENTRYPOINT ["/usr/bin/mongod"]  
CMD ["--help"]  
  

