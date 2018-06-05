FROM rabbitmq  
  
RUN rabbitmq-plugins enable \--offline rabbitmq_management rabbitmq_mqtt
rabbitmq_shovel rabbitmq_shovel_management  
  
EXPOSE 15671 15672 1883 8883  

