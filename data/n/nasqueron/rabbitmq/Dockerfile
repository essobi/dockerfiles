FROM rabbitmq:latest  
  
RUN rabbitmq-plugins enable \--offline rabbitmq_management && \  
rabbitmq-plugins enable \--offline rabbitmq_mqtt && \  
rabbitmq-plugins enable \--offline rabbitmq_stomp && \  
rabbitmq-plugins enable \--offline rabbitmq_web_stomp  
  
EXPOSE 1883 8883 15672 15674 61613  

