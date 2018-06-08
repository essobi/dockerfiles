FROM rabbitmq:3.7.0-management  
  
LABEL maintainer="Monsieur Biz <docker@monsieurbiz.com>"  
  
COPY ./plugins/* /usr/lib/rabbitmq/lib/rabbitmq_server-3.7.0/plugins/  
RUN rabbitmq-plugins enable \--offline rabbitmq_delayed_message_exchange  
  

