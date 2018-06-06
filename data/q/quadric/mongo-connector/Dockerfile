# FROM python:3.4.7-jessie  
# FROM python:3.4.8-jessie  
FROM python:3.4.8-slim-jessie  
  
LABEL net.quadric.vendor="Quadric ApS" maintainer="Ahmed Magdy
<ahmed.magdy@quadric.net>"  
  
ARG MONGO_CONNECTOR_CONFIG_FILE_PATH  
ENV MONGO_CONNECTOR_CONFIG_FILE_PATH
${MONGO_CONNECTOR_CONFIG_FILE_PATH:-/mongo-connector.config.json}  
  
ARG MONGO_CONNECTOR_OPLOG_FILE_SYMLINK_PATH  
ENV MONGO_CONNECTOR_OPLOG_FILE_SYMLINK_PATH
${MONGO_CONNECTOR_OPLOG_FILE_SYMLINK_PATH:-/symlink-oplog.timestamp}  
  
ARG MONGO_REPLICA_SET_NAME  
ENV MONGO_REPLICA_SET_NAME ${MONGO_REPLICA_SET_NAME:-rs0}  
  
# Install jq to write a better healthcheck command that the oplog.timestamp
contains exactly "${MONGO_REPLICA_SET_NAME}" in the first item in the list  
## Using something similar to: if cat /oplog.timestamp | jq '.[0]' | grep
"${MONGO_REPLICA_SET_NAME}" ; then echo 'found!!'; exit 0; else echo 'not
found!!'; exit 1; fi  
RUN apt-get update && \  
apt-get install -y jq && \  
rm -rf /var/lib/apt/lists/*  
  
COPY run.sh /run.sh  
  
COPY ./requirements.txt /tmp/requirements.txt  
  
RUN pip install -r /tmp/requirements.txt  
  
HEALTHCHECK \--interval=1s --timeout=30s --retries=300 \  
CMD if cat $MONGO_CONNECTOR_OPLOG_FILE_SYMLINK_PATH | jq '.[0]' | grep
\"${MONGO_REPLICA_SET_NAME}\" > /dev/null ; then exit 0; else exit 1; fi  
  
ENTRYPOINT bash /run.sh  

