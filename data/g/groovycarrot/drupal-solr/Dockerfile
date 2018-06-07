FROM solr:6.1  
USER root  
  
RUN apt-get update && apt-get install --yes git \  
&& git clone \--branch 8.x-1.x \  
https://git.drupal.org/project/search_api_solr.git \  
/opt/solr/server/var/search_api_solr  
  
ADD scripts/docker-entrypoint.sh /opt/docker-solr/scripts/docker-entrypoint.sh  
RUN chmod +x /opt/docker-solr/scripts/docker-entrypoint.sh  
  
USER $SOLR_USER  

