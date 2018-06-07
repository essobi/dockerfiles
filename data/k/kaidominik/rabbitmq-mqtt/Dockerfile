FROM rabbitmq:alpine  
  
RUN rabbitmq-plugins enable \--offline rabbitmq_management rabbitmq_mqtt
rabbitmq_web_mqtt  
  
EXPOSE 15671 15672 1883  

