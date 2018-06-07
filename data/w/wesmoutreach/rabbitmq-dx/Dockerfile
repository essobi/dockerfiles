FROM rabbitmq:3.6-management  
LABEL version 1.0  
COPY rabbitmq_delayed_message_exchange-0.0.1234.ez
/usr/lib/rabbitmq/lib/rabbitmq_server-$RABBITMQ_VERSION/plugins  
RUN rabbitmq-plugins enable \--offline rabbitmq_delayed_message_exchange  

