FROM rabbitmq:management-alpine  
  
RUN rabbitmq-plugins enable \--offline rabbitmq_stomp  
RUN rabbitmq-plugins enable \--offline rabbitmq_web_stomp  
RUN rabbitmq-plugins enable \--offline rabbitmq_mqtt  
RUN rabbitmq-plugins enable \--offline rabbitmq_event_exchange  

