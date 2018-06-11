#  
# Dockerfile  
#  
#  
#  
  
# Pull base image.  
FROM elasticsearch:2  
  
  
  
RUN plugin install elasticsearch/license/latest \  
&& plugin install marvel-agent \  
&& plugin install elasticsearch/shield/latest \  
&& plugin install elasticsearch/watcher/latest \  
&& plugin install mobz/elasticsearch-head  
# Expose ports for each Mongo replica set instance  
EXPOSE 9200 9300  
  
# Run start shell when container launches  

