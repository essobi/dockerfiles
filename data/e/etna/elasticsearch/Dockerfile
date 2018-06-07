FROM elasticsearch:1.7  
ENV TZ Europe/Paris  
  
RUN echo "script.inline: on" >>
/usr/share/elasticsearch/config/elasticsearch.yml  
RUN echo "script.indexed: on" >>
/usr/share/elasticsearch/config/elasticsearch.yml  
RUN echo "http.cors.allow-origin: /https?:\/\/localhost(:[0-9]+)?/" >>
/usr/share/elasticsearch/config/elasticsearch.yml  
RUN echo "script.groovy.sandbox.enabled: true" >>
/usr/share/elasticsearch/config/elasticsearch.yml  
RUN sed -i 's/# network.host: 192.168.0.1/network.host: 127.0.0.1/g'
/usr/share/elasticsearch/config/elasticsearch.yml  

