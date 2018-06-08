FROM mongo:3.4  
MAINTAINER Sergey Kandyla <skandyla@gmail.com>  
  
# configuration and startup  
ENV AUTH="n" \  
ADMIN_USER="admin" \  
ADMIN_PWD="changeme" \  
ADMIN_AUTHENTICATION_DATABASE="" \  
REQUIRE_SSL="n" \  
KEY_FILE="/etc/ssl/mongodb.pem" \  
CA_FILE="/etc/ssl/ca.pem" \  
DATA_PATH="/data/db" \  
DB_NAME="" \  
DB_USER="user" \  
DB_PWD="changeme" \  
OPLOG_SIZE=50 \  
RS_NAME="" \  
STORAGE_ENGINE="wiredTiger" \  
MASTER=$HOSTNAME \  
SLAVES="" \  
ARBITRERS="" \  
SLAVE_OK="y" \  
SHARD_SVR="n" \  
CONFIG_SVR="n" \  
CONFIG_SERVERS="" \  
CONFIG_DIR="/data/db/_config" \  
SHARDS=""  
  
COPY ./run /run  
RUN chmod +x -R /run  
VOLUME /data/db  
USER mongodb  
ENTRYPOINT ["/run/entrypoint.sh"]  
EXPOSE 27017  

