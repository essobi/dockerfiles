FROM solr:5  
MAINTAINER M Parker "mparker17@536298.no-reply.drupal.org"  
ENV SOLR_VERSION solr-5.x  
ENV SOLR_CORE_NAME collection1  
  
# Create a core.  
RUN bin/solr start && \  
bin/solr create_core -c $SOLR_CORE_NAME && \  
bin/solr stop  
  
# Copy the Drupal module's configuration into the core.  
COPY apachesolr/solr-conf/$SOLR_VERSION/*
/opt/$SOLR/example/solr/$SOLR_CORE_NAME/conf/  

