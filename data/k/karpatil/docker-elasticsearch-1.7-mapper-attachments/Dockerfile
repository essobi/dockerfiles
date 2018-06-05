FROM elasticsearch:1.7.3  
RUN /usr/share/elasticsearch/bin/plugin install elasticsearch/elasticsearch-
mapper-attachments/2.7.1  
  
EXPOSE 9200 9300  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["elasticsearch"]

