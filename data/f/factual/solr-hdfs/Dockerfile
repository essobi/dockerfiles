FROM factual/docker-cdh5-base  
  
  
ENV SOLR_VERSION=6.4.2  
RUN curl -sO
http://apache.mirrors.lucidnetworks.net/lucene/solr/$SOLR_VERSION/solr-$SOLR_VERSION.tgz  
RUN tar xzf solr-$SOLR_VERSION.tgz  
RUN mv solr-$SOLR_VERSION solr  
  
RUN rm solr-$SOLR_VERSION.tgz  
  
#cors  
ADD webdefault.xml /solr/server/etc/  
  
ADD bootstrap.sh /etc/my_init.d/002_bootstrap  
  
VOLUME ["/var/apps/solr/lib/"]  

