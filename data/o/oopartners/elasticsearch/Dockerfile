FROM dockerfile/elasticsearch  
  
ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
  
ENV ES_HOME /elasticsearch  
  
# HEAD plugin  
RUN /elasticsearch/bin/plugin -install mobz/elasticsearch-head  
  
# Mapper-attachments / Tika  
RUN /elasticsearch/bin/plugin -install elasticsearch/elasticsearch-mapper-
attachments/2.4.3  
RUN curl -o /elasticsearch/lib/tika-app-1.7.jar -L
'http://www.apache.org/dyn/closer.cgi/tika/tika-app-1.7.jar'  
  
EXPOSE 9200 9300  
ENTRYPOINT ["/elasticsearch/bin/elasticsearch"]  
CMD ["-Des.config=/elasticsearch/config/elasticsearch.yml"]  
  

