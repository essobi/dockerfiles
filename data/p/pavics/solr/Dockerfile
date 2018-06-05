FROM birdhouse/solr  
MAINTAINER st-denis.blaise@ouranos.ca  
  
COPY immutable_to_mutable.sh /root  
COPY mutable_to_immutable.sh /root  
  
VOLUME /data  
  
# Ports used in birdhouse  
EXPOSE 8983  
# Start supervisor in foreground  
ENV DAEMON_OPTS --nodaemon --user $USER  
# Start service ...  
CMD make update-config update-user && /bin/bash /root/immutable_to_mutable.sh
&& make start  

