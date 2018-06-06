FROM elasticsearch:5.6.7-alpine  
ENV PATH $PATH:/usr/share/elasticsearch/bin  
  
COPY fix-permissions /usr/libexec/fix-permissions  
  
RUN \  
# verify  
echo JAVA VERSION: && \  
java -version 2>&1 && \  
echo ELASTICSEARCH VERSION: && \  
elasticsearch --version  
  
COPY elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml  
VOLUME ["/usr/share/elasticsearch/data", "/usr/share/elasticsearch/logs"]  
  
COPY start.sh /start.sh  
EXPOSE 9200 9300  
USER elasticsearch  
  
ENTRYPOINT ["/start.sh"]  
CMD ["elasticsearch"]  

