FROM elasticsearch:2.4.5-alpine  
ADD elasticsearch.yml /usr/share/elasticsearch/config/  
USER root  
RUN chown elasticsearch:elasticsearch config/elasticsearch.yml  
RUN bin/plugin install cloud-aws  
USER elasticsearch  

