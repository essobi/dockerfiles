FROM rabbitmq:3.7.2-management  
  
RUN apt-get update  
RUN apt-get install -y curl --no-install-recommends  
RUN apt-get install -y unzip --no-install-recommends  
RUN rm -rf /var/lib/apt/lists/*  
  
# Retrive zip from rabbitmq  
RUN curl http://dl.bintray.com/rabbitmq/community-
plugins/3.7.x/rabbitmq_delayed_message_exchange/rabbitmq_delayed_message_exchange-20171201-3.7.x.zip
> $RABBITMQ_HOME/plugins/rabbitmq_delayed_message_exchange-0.0.1.zip  
  
# UNZIP it  
RUN unzip $RABBITMQ_HOME/plugins/rabbitmq_delayed_message_exchange-0.0.1.zip  
  
# RENAME to RabbitMQ plugin standard  
RUN mv rabbitmq_delayed_message_exchange-20171201-3.7.x.ez
$RABBITMQ_HOME/plugins/rabbitmq_delayed_message_exchange-0.0.1.ez  
  
# Remove zip  
RUN rm -rf $RABBITMQ_HOME/plugins/rabbitmq_delayed_message_exchange-0.0.1.zip  
  
# Enable plugin  
RUN rabbitmq-plugins enable \--offline rabbitmq_delayed_message_exchange  
RUN rabbitmq-plugins enable \--offline rabbitmq_consistent_hash_exchange  

