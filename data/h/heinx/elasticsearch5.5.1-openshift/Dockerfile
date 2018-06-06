FROM docker.elastic.co/elasticsearch/elasticsearch:5.5.1  
  
USER root  
  
RUN chgrp -R 0 /usr/share/elasticsearch && \  
chmod -R g+rw /usr/share/elasticsearch && \  
find /usr/share/elasticsearch -type d -exec chmod g+x {} + && \  
ulimit -n 65536 && \  
ulimit -u 2048 && \  
echo "* - nofile 65536" >> /etc/security/limits.conf && \  
rm -fr /usr/share/elasticsearch/plugins/x-pack  
  
COPY elasticsearch.yml /usr/share/elasticsearch/config  
  
ENV ES_JAVA_OPTS "-Xms512m -Xmx512m"  
ENV CLUSTER_NAME=elasticsearch5-openshift  
ENV NUMBER_OF_MASTERS=1  
ENV NETWORK_HOST=0.0.0.0  
ENV PUBLISH_HOST=  
ENV UNICAST_HOSTS "127.0.0.1, [::1]"  
  
USER 1001  

