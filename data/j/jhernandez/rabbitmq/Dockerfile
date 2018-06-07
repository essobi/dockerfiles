FROM rabbitmq  
MAINTAINER contact@jhernandez.me  
COPY plugins/rabbitmq_delayed_message_exchange-0.0.1.ez
/plugins/rabbitmq_delayed_message_exchange-0.0.1.ez  
RUN rabbitmq-plugins enable \--offline rabbitmq_management  
RUN rabbitmq-plugins enable \--offline rabbitmq_delayed_message_exchange  
RUN rabbitmq-plugins enable \--offline rabbitmq_shovel
rabbitmq_shovel_management  
EXPOSE 15671 15672  

