FROM solr:5.4  
MAINTAINER LWB  
  
RUN mkdir -p /opt/solr/server/solr/core-portal/data && \  
mkdir -p /opt/solr/server/solr/core-shop/data && \  
mkdir -p /opt/solr/server/solr/core-portal/conf && \  
mkdir -p /opt/solr/server/solr/core-shop/conf  
  
RUN mkdir -p /opt/solr/server/solr/core-archiv/data && \  
mkdir -p /opt/solr/server/solr/core-archiv_gbgr/data && \  
mkdir -p /opt/solr/server/solr/core-archiv/conf && \  
mkdir -p /opt/solr/server/solr/core-archiv_gbgr/conf  
  
COPY cores/portal/core.properties /opt/solr/server/solr/core-portal/  
COPY cores/shop/core.properties /opt/solr/server/solr/core-shop/  
COPY cores/portal/conf /opt/solr/server/solr/core-portal/conf  
COPY cores/shop/conf /opt/solr/server/solr/core-shop/conf  
  
COPY cores/archiv/core.properties /opt/solr/server/solr/core-archiv/  
COPY cores/archiv_gbgr/core.properties /opt/solr/server/solr/core-archiv_gbgr/  
COPY cores/archiv/conf /opt/solr/server/solr/core-archiv/conf  
COPY cores/archiv_gbgr/conf /opt/solr/server/solr/core-archiv_gbgr/conf  
  
USER root  
  
RUN chown -R $SOLR_USER:$SOLR_USER /opt/solr/server/solr/core-portal && \  
chown -R $SOLR_USER:$SOLR_USER /opt/solr/server/solr/core-shop  
  
RUN chown -R $SOLR_USER:$SOLR_USER /opt/solr/server/solr/core-archiv && \  
chown -R $SOLR_USER:$SOLR_USER /opt/solr/server/solr/core-archiv_gbgr  
  
VOLUME /opt/solr/server/solr/core-portal/data  
VOLUME /opt/solr/server/solr/core-shop/data  
VOLUME /opt/solr/server/solr/core-archiv/data  
VOLUME /opt/solr/server/solr/core-archiv_gbgr/data  
  
CMD ["/opt/solr/bin/solr", "restart", "-f"]  

