FROM docker.elastic.co/elasticsearch/elasticsearch:5.6.3  
# Run ES in development mode  
ENV discovery.type=single-node  
  
# Disable Shield plugin security  
ENV xpack.security.enabled false  
  
# Avoid surprise OOM at runtime  
ENV bootstrap.memory_lock true  
ENV ES_JAVA_OPTS -Xms256m -Xmx256m  
  
COPY data.json mappings.json provision.sh /tmp/  
RUN /tmp/provision.sh  

