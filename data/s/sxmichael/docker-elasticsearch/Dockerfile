FROM elasticsearch:1.6  
MAINTAINER Michael Gelfand michael@senexx.com  
  
RUN mkdir -p /usr/share/elasticsearch/conf.d/  
  
ADD elasticsearch.yml /usr/share/elasticsearch/conf.d/  
  
ADD plugins.lst /usr/share/elasticsearch/plugins/  
  
RUN cat /usr/share/elasticsearch/plugins/plugins.lst | xargs --max-lines=1
--no-run-if-empty /usr/share/elasticsearch/bin/plugin -i  
  
VOLUME ["/usr/share/elasticsearch/data"]  
EXPOSE 9200 9300  

