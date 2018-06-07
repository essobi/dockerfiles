FROM rabbitmq:3.6.6-management  
  
ADD ./rabbitmq_delayed_message_exchange-0.0.1.ez
/usr/lib/rabbitmq/lib/rabbitmq_server-3.6.6/plugins/rabbitmq_delayed_message_exchange-0.0.1.ez  
RUN rabbitmq-plugins enable --offline rabbitmq_delayed_message_exchange  

