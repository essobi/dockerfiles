FROM rabbitmq  
  
RUN rabbitmq-plugins enable \--offline rabbitmq_management  
EXPOSE 15671 15672  
RUN rabbitmq-plugins enable rabbitmq_stomp --offline  
EXPOSE 61613  

