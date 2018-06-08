FROM rabbitmq  
  
# instal STOMP and web management plugins  
RUN rabbitmq-plugins enable rabbitmq_management && rabbitmq-plugins enable
rabbitmq_stomp  
  
# Expose ports.  
EXPOSE 5672  
EXPOSE 15672  
EXPOSE 61613  

