FROM docker.elastic.co/elasticsearch/elasticsearch:5.4.0  
  
USER root  
  
RUN yum install -y iproute && yum clean all  
  
USER elasticsearch  
  
COPY ./overlay/ /  
  
HEALTHCHECK \--interval=30s \--retries=3 \--timeout=5s CMD curl -s
127.0.0.1:9200 | grep -q number || exit 1  
  
# Uninstall xpack  
RUN eval ${ES_JAVA_OPTS:-} elasticsearch-plugin remove x-pack  
  
# Install plugins  
RUN eval ${ES_JAVA_OPTS:-} elasticsearch-plugin install analysis-icu  
  
# Disabled xpack  
# ENV xpack.security.enabled false  
# ENV xpack.monitoring.enabled false  
  
CMD ["docker-entrypoint.sh"]  

