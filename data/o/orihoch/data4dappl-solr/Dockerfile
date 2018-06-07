FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y solr-jetty  
  
COPY default-jetty8 /etc/default/jetty8  
COPY schema.xml /etc/solr/conf/schema.xml  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

