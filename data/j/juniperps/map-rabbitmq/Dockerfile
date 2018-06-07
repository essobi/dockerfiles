FROM rabbitmq:3-management-alpine  
  
COPY healthcheck.sh /etc/rabbitmq/healthcheck.sh  
  
RUN apk add --no-cache tini  
RUN chmod +x /etc/rabbitmq/healthcheck.sh  
  
RUN rabbitmq-plugins enable \--offline rabbitmq_stomp rabbitmq_web_stomp
rabbitmq_federation rabbitmq_federation_management  
  
HEALTHCHECK \--interval=30s --timeout=3s --retries=3 CMD
./etc/rabbitmq/healthcheck.sh  
  
ENTRYPOINT ["/sbin/tini", "--"]  
  
CMD ["rabbitmq-server"]  

