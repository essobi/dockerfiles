FROM rabbitmq:3.6  
ADD rabbitmq_delayed_message_exchange-20171215-3.6.x.ez
$RABBITMQ_HOME/plugins/rabbitmq_delayed_message_exchange-20171215-3.6.x.ez  
  
RUN rabbitmq-plugins enable \--offline rabbitmq_delayed_message_exchange  

