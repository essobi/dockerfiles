FROM elasticsearch:1.7  
COPY elasticsearch-srv-discovery-0.0.1-SNAPSHOT.zip /tmp/  
  
RUN /usr/share/elasticsearch/bin/plugin --install cloud-etcd --url
file:///tmp/elasticsearch-srv-discovery-0.0.1-SNAPSHOT.zip \  
&& rm -rf /tmp/*  

