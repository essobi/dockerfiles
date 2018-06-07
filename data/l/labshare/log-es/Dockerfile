# https://github.com/elastic/elasticsearch-docker  
FROM docker.elastic.co/elasticsearch/elasticsearch:5.5.1  
  
COPY config/ config/  
COPY bin/ bin/  
  
RUN elasticsearch-plugin install --batch com.floragunn:search-guard-5:5.5.1-15
-v \  
&& chmod +x \  
plugins/search-guard-5/tools/hash.sh \  
plugins/search-guard-5/tools/sgadmin.sh  
  
USER root  
COPY ./es-entrypoint.sh /  
RUN chmod +x /es-entrypoint.sh  
  
USER elasticsearch  
ENTRYPOINT ["/es-entrypoint.sh"]  
  

