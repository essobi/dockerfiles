FROM mongo:2.6  
MAINTAINER erhankesken@gmail.com  
  
ENV REPLICATION_SET_NAME="" \  
NET_PORT="27017" \  
SHARDING_CONFIGDB="" \  
KEY_FILE_CONTENT="" \  
STORAGE_MMAPV1_SMALLFILES="" \  
CONFIGSVR="false"  
COPY env-entrypoint.sh /env-entrypoint.sh  
RUN chmod +x /env-entrypoint.sh  
  
ENTRYPOINT ["/env-entrypoint.sh"]  
  

