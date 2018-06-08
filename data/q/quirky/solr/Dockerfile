FROM makuk66/docker-solr  
MAINTAINER Micah Martin <micahlmartin@gmail.com>  
  
ADD ./schema.xml /opt/solr/example/solr/collection1/conf/schema.xml  
  
EXPOSE 8983  
CMD ["/bin/bash", "-c", "cd /opt/solr/example; java -jar start.jar"]  

