FROM elasticsearch:1.7  
RUN bin/plugin install elasticsearch/elasticsearch-cloud-aws/2.7.1  
RUN ulimit -n 65536  
  
EXPOSE 9200:9200  
EXPOSE 9300:9300  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["elasticsearch"]  

