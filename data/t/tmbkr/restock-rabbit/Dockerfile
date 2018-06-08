FROM rabbitmq:3  
ENV RABBITMQ_DEFAULT_USER=restock  
ENV RABBITMQ_DEFAULT_PASS=restock-123456-password  
  
RUN rabbitmq-plugins enable \--offline rabbitmq_management  
RUN rabbitmq-plugins enable \--offline rabbitmq_mqtt  
RUN rabbitmq-plugins enable \--offline rabbitmq_web_mqtt  
  
EXPOSE 15671 15672  
EXPOSE 1883 8883

