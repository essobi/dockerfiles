FROM java:8-alpine  
  
ADD https://s3-eu-west-1.amazonaws.com/softwaremill-public/elasticmq-
server-0.10.0.jar /elasticmq/  
  
WORKDIR /elasticmq  
  
RUN ln -s elasticmq-server-0.10.0.jar elasticmq-server.jar  
  
EXPOSE 9324  
ENV BRIDGE_HOST='' \  
QUEUE_NAME="default" \  
QUEUE_DEFAULT_VISIBILITY_TIMEOUT=10 \  
QUEUE_DELAY=5 \  
QUEUE_RECEIVE_MESSAGE_WAIT=0  
COPY /entrypoint /elasticmq/entrypoint  
RUN chmod +x /elasticmq/entrypoint  
  
ENTRYPOINT ["/elasticmq/entrypoint"]  
CMD []

