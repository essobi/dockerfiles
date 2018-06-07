FROM solr  
  
MAINTAINER Stuart Owen <orcid.org/0000-0003-2130-0865>  
  
RUN /opt/solr/bin/solr start && \  
/opt/solr/bin/solr create_core -c seek && \  
/opt/solr/bin/solr stop  
  
COPY schema.xml solrconfig.xml /opt/solr/server/solr/seek/conf/  
  

