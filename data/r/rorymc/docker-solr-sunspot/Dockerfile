# solr-sunspot  
FROM maven  
MAINTAINER Rory V McKenna <rory@smiletime.com>  
  
RUN apt-get --yes install git  
  
RUN git clone https://github.com/ksclarke/solr-jetty-maven /opt/solr  
RUN cd /opt/solr; mvn install  
  
ADD config/schema.xml
/opt/solr/src/main/resources/solr/collection1/conf/schema.xml  
ADD config/solrconfig.xml
/opt/solr/src/main/resources/solr/collection1/conf/solrconfig.xml  
  
EXPOSE 8983  
CMD ["/bin/bash", "-c", "cd /opt/solr; mvn jetty:run"]  

