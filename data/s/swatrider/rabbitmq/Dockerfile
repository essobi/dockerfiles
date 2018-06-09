FROM rabbitmq:3.6.8-management-alpine  
  
RUN rabbitmq-plugins enable \--offline rabbitmq_management  
RUN rabbitmq-plugins enable rabbitmq_web_stomp  
  
EXPOSE 15671 15672 15674  

