from rabbitmq:3.6-management  
  
env RABBITMQ_HIPE_COMPILE=1 RABBITMQ_ERLANG_COOKIE='canopy rabbit'
RABBITMQ_DEFAULT_USER=canopy RABBITMQ_DEFAULT_PASS=canopytax  
COPY plugins/* /plugins/  
COPY rabbitmq.config /usr/lib/rabbitmq/etc/rabbitmq/rabbitmq.config  
  
RUN rabbitmq-plugins enable \  
rabbitmq_delayed_message_exchange \--offline && \  
rabbitmq-plugins enable rabbitmq_management_visualiser \--offline && \  
rabbitmq-plugins enable rabbitmq_aws \--offline \  
rabbitmq_delayed_message_exchange \--offline \  
rabbitmq_management \--offline \  
rabbitmq_management_visualiser \--offline \  
rabbitmq_management_themes \--offline \  
rabbitmq_federation \--offline \  
rabbitmq_federation_management \--offline \  
rabbitmq_message_timestamp \--offline \  
rabbitmq_shovel \--offline \  
rabbitmq_shovel_management \--offline \  
rabbitmq_stomp \--offline \  
rabbitmq_top \--offline \  
autocluster \--offline \  
rabbitmq_web_stomp \--offline  

