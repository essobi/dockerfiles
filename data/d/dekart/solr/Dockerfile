FROM dekart/java:6  
MAINTAINER Dumitru  
  
LABEL description="Audiorama Solr image" version="0.0.1"  
  
EXPOSE 8502  
ADD ["solr", "/opt/solr"]  
  
WORKDIR /opt/solr/solr  
  
VOLUME /opt/solr/solr/data  
  
CMD ["java", "-Dsolr.solr.home=/opt/solr/solr/solr",
"-Djava.awt.headless=true", "-jar", "start.jar"]  

