# Dockerfile for the PDC's Gateway (formerly Endpoint) database  
#  
#  
# Database for Gateway, de-identified. Based on Mongo official 3.0.  
#  
# Example:  
# sudo docker pull pdcbc/gateway_db  
# sudo docker run -d --name=database --restart=always \  
# -v /encrypted/docker/mongo/:/data/db:rw \  
# pdcbc/gateway_db  
#  
# Folder paths  
# - Mongo DB: -v </path/>:/data/db/:rw  
#  
# Modify default settings  
# - RAM < 1 GB: -e RAM_REDUCE=<yes/no>  
#  
#  
FROM phusion/baseimage  
MAINTAINER derek.roberts@gmail.com  
  
  
################################################################################  
# Start - modified from https://hub.docker.com/_/mongo/  
################################################################################  
# Create users and groups  
#  
RUN groupadd -r mongodb; \  
useradd -r -g mongodb mongodb  
  
# Packages  
#  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update; \  
apt-get install -y --no-install-recommends \  
ca-certificates; \  
rm -rf /var/lib/apt/lists/*  
  
# MongoDB  
#  
ENV MONGO_MAJOR 3.0  
ENV MONGO_VERSION 3.0.7  
#  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
492EAFE8CD016A07919F1D2B9ECBEC467F0CEB10; \  
echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/$MONGO_MAJOR
multiverse" > /etc/apt/sources.list.d/mongodb-org.list  
RUN apt-get update; \  
apt-get install -y \  
mongodb-org=$MONGO_VERSION \  
mongodb-org-server=$MONGO_VERSION \  
mongodb-org-shell=$MONGO_VERSION \  
mongodb-org-mongos=$MONGO_VERSION \  
mongodb-org-tools=$MONGO_VERSION; \  
rm -rf /var/lib/apt/lists/* \  
/var/lib/mongodb \  
/etc/mongod.conf  
  
# Volume  
#  
RUN mkdir -p /data/db; \  
chown -R mongodb:mongodb /data/db  
VOLUME /data/db  
  
# Port  
#  
EXPOSE 27017  
################################################################################  
# End - modified from https://hub.docker.com/_/mongo/  
################################################################################  
# Mongo startup  
#  
RUN mkdir -p /etc/service/mongod/; \  
SCRIPT=/etc/service/mongod/run; \  
( \  
echo "#!/bin/bash"; \  
echo ""; \  
echo ""; \  
echo "# Start mongod"; \  
echo "#"; \  
echo "exec mongod --storageEngine wiredTiger"; \  
) \  
>> ${SCRIPT}; \  
chmod +x ${SCRIPT}  
  
# Maintenance script and cron job  
#  
RUN SCRIPT=/db_maintenance.sh; \  
( \  
echo "#!/bin/bash"; \  
echo ""; \  
echo ""; \  
echo "# Wait for mongo to start"; \  
echo "#"; \  
echo "while [ \$( pgrep -c mongod ) -eq 0 ]"; \  
echo "do"; \  
echo " sleep 60"; \  
echo "done"; \  
echo "sleep 5"; \  
echo ""; \  
echo ""; \  
echo "# Set index"; \  
echo "#"; \  
echo "/usr/bin/mongo query_gateway_development --eval 'printjson(
db.records.ensureIndex({ hash_id : 1 }, { unique : true }))'"; \  
echo ""; \  
echo ""; \  
echo "# Database junk cleanup"; \  
echo "#"; \  
echo "/usr/bin/mongo query_gateway_development --eval 'db.providers.drop()'";
\  
echo "/usr/bin/mongo query_gateway_development --eval 'db.queries.drop()'"; \  
echo "/usr/bin/mongo query_gateway_development --eval 'db.results.drop()'"; \  
) \  
>> ${SCRIPT}; \  
chmod +x ${SCRIPT}; \  
( \  
echo "# Run maintenance script (boot, Sundays at noon)"; \  
echo "@reboot "${SCRIPT}; \  
echo "0 12 * * 0 "${SCRIPT}; \  
) \  
| crontab -  

