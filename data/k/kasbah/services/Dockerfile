FROM kasbah-solr  
  
USER solr  
COPY solr-kasbah /opt/solr/server/solr/kasbah  
  
USER root  
  
ADD schema.sql /docker-entrypoint-initdb.d/  
ADD docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["sh", "/entrypoint.sh"]  
  

