FROM rabbitmq:3.7-alpine  
  
RUN rabbitmq-plugins enable \--offline rabbitmq_peer_discovery_k8s  
  
COPY docker-entrypoint.sh /usr/local/bin/  

