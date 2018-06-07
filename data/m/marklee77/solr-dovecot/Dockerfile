FROM solr:7-alpine  
LABEL maintainer="Mark Stillwell <mark@stillwell.me>"  
  
USER root  
  
RUN apk add --update --no-cache curl && \  
rm -rf /var/cache/apk/*  
  
COPY *.xml /opt/solr/server/solr/configsets/_default/conf/  
RUN chown solr:solr /opt/solr/server/solr/configsets/_default/conf/*.xml && \  
chmod 0644 /opt/solr/server/solr/configsets/_default/conf/*.xml  
  
USER solr  
  
ENTRYPOINT ["docker-entrypoint.sh", "solr-precreate", "dovecot"]  
  
HEALTHCHECK CMD curl -f http://localhost:8983/solr/dovecot/admin/ping  
  
VOLUME ["/opt/solr/server/solr/mycores"]  

