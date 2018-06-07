FROM rabbitmq:3.7.4-management  
  
RUN apt-get update -y && \  
apt-get install -y \  
curl \  
unzip  
  
RUN cd /tmp && \  
curl -o rabbitmq_delayed_message_exchange.zip \  
https://dl.bintray.com/rabbitmq/community-
plugins/3.7.x/rabbitmq_delayed_message_exchange/rabbitmq_delayed_message_exchange-20171201-3.7.x.zip
&&\  
unzip rabbitmq_delayed_message_exchange.zip && \  
cp rabbitmq_delayed_message_exchange-20171201-3.7*.ez
/usr/lib/rabbitmq/lib/rabbitmq_server-3.7.4/plugins/ && \  
rabbitmq-plugins enable --offline rabbitmq_delayed_message_exchange

