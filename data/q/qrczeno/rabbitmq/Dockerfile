FROM rabbitmq:3.6.6-management  
  
ADD http://www.rabbitmq.com/community-
plugins/v3.6.x/rabbitmq_delayed_message_exchange-0.0.1.ez
$RABBITMQ_HOME/plugins/rabbitmq_delayed_message_exchange-0.0.1.ez  
  
RUN chmod a+r
$RABBITMQ_HOME/plugins/rabbitmq_delayed_message_exchange-0.0.1.ez && \  
rabbitmq-plugins enable \--offline rabbitmq_delayed_message_exchange  

