FROM solr:5.5.5-alpine  
  
USER solr  
  
ADD ./conf /opt/solr/server/solr/configsets/marin/conf  
  
CMD ["solr-precreate", "marin", "/opt/solr/server/solr/configsets/marin"]  

