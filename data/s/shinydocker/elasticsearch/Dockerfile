FROM elasticsearch:1.7  
#RUN plugin install io.fabric8/elasticsearch-cloud-kubernetes/1.3.0  
COPY elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml  
  
COPY run.sh /  
COPY elasticsearch_logging_discovery /  
  
RUN \  
chmod +x /run.sh && \  
chmod +x /elasticsearch_logging_discovery  
  
VOLUME ["/data"]  
  
EXPOSE 9200 9300  
CMD ["/run.sh"]  

