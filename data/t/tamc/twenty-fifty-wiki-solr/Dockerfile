# This is a Dockerfile.  
#  
# It is a quick way of getting a server running with this code.  
# See http://docker.io for more details.  
#  
FROM makuk66/docker-solr  
MAINTAINER tom@counsell.org  
  
RUN bin/solr start -noprompt ; bin/solr create_core -c default  
  
#ADD
https://raw.githubusercontent.com/sunspot/sunspot/master/sunspot_solr/solr/solr/configsets/sunspot/conf/solrconfig.xml
/opt/solr/server/solr/default/conf/solrconfig.xml  
#ADD
https://raw.githubusercontent.com/sunspot/sunspot/master/sunspot_solr/solr/solr/configsets/sunspot/conf/schema.xml
/opt/solr/server/solr/default/conf/schema.xml  
ADD solrconfig.xml /opt/solr/server/solr/default/conf/solrconfig.xml  
ADD schema.xml /opt/solr/server/solr/default/conf/schema.xml  
  
USER root  
RUN chown solr:solr /opt/solr/server/solr/default/conf/solrconfig.xml  
RUN chown solr:solr /opt/solr/server/solr/default/conf/schema.xml  
  
USER solr  

