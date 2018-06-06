FROM rabbitmq:3.6.12-management  
  
COPY rabbitmq.config /etc/rabbitmq/rabbitmq.config  
RUN chmod 777 /etc/rabbitmq/rabbitmq.config  
  
ENV RABBITMQ_SETUP_DELAY=5  
ENV RABBITMQ_USER=guest  
ENV RABBITMQ_PASSWORD=guest  
ENV RABBITMQ_LOOPBACK_USERS=guest  
ENV RABBITMQ_CLUSTER_NODES=  
ENV RABBITMQ_CLUSTER_PARTITION_HANDLING=autoheal  
ENV RABBITMQ_CLUSTER_DISC_RAM=disc  
ENV RABBITMQ_FIREHOSE_QUEUENAME=  
ENV RABBITMQ_FIREHOSE_ROUTINGKEY=publish.#  
ENV RABBITMQ_HIPE_COMPILE=false  
ENV RABBITMQ_NODENAME=  
  
RUN apt-get update -y && apt-get install -y python  
  
ADD init.sh /init.sh  
EXPOSE 15672  
CMD ["/init.sh"]  

