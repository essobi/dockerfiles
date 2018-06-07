FROM rabbitmq:3.7-management  
RUN apt-get update && apt-get install -y wget  
  
RUN wget -nc -O - https://dl.bintray.com/rabbitmq/community-
plugins/3.7.0/rabbitmq_delayed_message_exchange-3.7.0.zip | gunzip >
/usr/lib/rabbitmq/lib/rabbitmq_server-$RABBITMQ_VERSION/plugins/rabbitmq_delayed_message_exchange-3.7.0.ez  
  
RUN echo '[{rabbit, [{loopback_users, []}]}].' > /etc/rabbitmq/rabbitmq.config  
RUN rabbitmq-plugins enable \--offline rabbitmq_delayed_message_exchange  
RUN rabbitmq-plugins enable \--offline rabbitmq_shovel
rabbitmq_shovel_management  

