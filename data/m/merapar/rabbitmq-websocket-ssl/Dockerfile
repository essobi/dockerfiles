FROM rabbitmq:3.6.0-management  
RUN rabbitmq-plugins enable \--offline rabbitmq_web_stomp  
COPY rabbitmq.config /etc/rabbitmq/rabbitmq.config  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
ENTRYPOINT ["/run.sh"]  

