FROM docker.elastic.co/elasticsearch/elasticsearch:5.5.1  
MAINTAINER Computer Science House  
  
RUN set -ex \  
&& /usr/share/elasticsearch/bin/elasticsearch-plugin remove x-pack --purge \  
&& yes | /usr/share/elasticsearch/bin/elasticsearch-plugin install mapper-
attachments \  
&& find /usr/share/elasticsearch -type d -exec chmod og+rwx {} \; \  
&& find /usr/share/elasticsearch -type f -exec chmod +r {} \; \  
&& chmod +x /usr/share/elasticsearch/bin/*  

