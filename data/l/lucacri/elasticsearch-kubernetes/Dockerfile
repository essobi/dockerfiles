FROM docker.elastic.co/elasticsearch/elasticsearch:6.2.4  
  
LABEL maintainer="lucacri@gmail.com"  
  
ADD start.sh /start.sh  
ADD /elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml  
  
RUN chmod 777 /start.sh && chmod 777
/usr/share/elasticsearch/config/elasticsearch.yml  
  
USER root  
  
ENV ES_JAVA_OPTS="-Xms2g -Xmx2g"  
ENV node.master="true"  
ENV node.data "true"  
ENV node.ingest "true"  
ENV bootstrap.memory_lock "false"  
ENV cluster.name "es-cluster"  
ENV network.host "0.0.0.0"  
ENV PROCESSORS="1"  
ENV xpack.security.enabled="false"  
  
ENTRYPOINT [ "/start.sh" ]

