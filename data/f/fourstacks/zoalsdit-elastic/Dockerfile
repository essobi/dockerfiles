FROM elasticsearch:2.4.2  
  
ADD config /usr/share/elasticsearch/config  
ADD entrypoint.sh /entrypoint.sh  
  
  
RUN /usr/share/elasticsearch/bin/plugin install mobz/elasticsearch-head  
RUN /usr/share/elasticsearch/bin/plugin install cloud-aws  
  
VOLUME /usr/share/elasticsearch/data  
  
EXPOSE 9200 9300  

