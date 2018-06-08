FROM elasticsearch:2.3.4  
RUN /usr/share/elasticsearch/bin/plugin install cloud-aws &&\  
mkdir -p /data/elasticsearch &&\  
cd /usr/share/elasticsearch/lib &&\  
cd /  
  
COPY elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml  
COPY docker-entrypoint.sh /  
  
VOLUME /data  

