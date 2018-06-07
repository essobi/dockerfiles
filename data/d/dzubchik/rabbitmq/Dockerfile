FROM rabbitmq:3.6.8-management  
  
ADD rabbitmq_delayed_message_exchange-0.0.1.ez
/usr/lib/rabbitmq/lib/rabbitmq_server-3.6.8/plugins/  
RUN rabbitmq-plugins enable --offline rabbitmq_delayed_message_exchange  

