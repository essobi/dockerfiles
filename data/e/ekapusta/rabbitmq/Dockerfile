FROM rabbitmq:3.5.7  
MAINTAINER Dmitry Romanov "dmitry.romanov85@gmail.com"  
ADD rabbitmq_delayed_message_exchange-0.0.1-rmq3.5.x-9bf265e4.ez
/usr/lib/rabbitmq/lib/rabbitmq_server-3.5.7/plugins/rabbitmq_delayed_message_exchange.ez  
RUN rabbitmq-plugins enable \--offline rabbitmq_management  
RUN rabbitmq-plugins enable \--offline rabbitmq_web_stomp  
RUN rabbitmq-plugins enable \--offline rabbitmq_delayed_message_exchange  
  
EXPOSE 15671 15672 15674  

