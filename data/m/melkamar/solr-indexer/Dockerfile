FROM solr  
COPY ./andruian_configset /andruian_configset  
ENTRYPOINT ["docker-entrypoint.sh", "solr-precreate", "andruian",
"/andruian_configset"]  

