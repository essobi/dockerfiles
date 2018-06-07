FROM solr:6  
MAINTAINER LWB  
  
ENV SOLR_ADMIN admin  
ENV SOLR_PASSWORD password  
ENV SOLR_CORES test  
  
RUN mkdir -p /opt/solr/server/solr/data  
RUN mkdir /opt/solr/conf  
COPY conf /opt/solr/conf  
  
VOLUME /opt/solr/server/solr/data  
  
USER root  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
RUN chown -R $SOLR_USER:$SOLR_USER /opt/solr/server/solr  
  
USER $SOLR_USER  
  
CMD ["/opt/solr/bin/solr", "restart", "-f"]  

