FROM rabbitmq:3.7-management  
RUN apt-get update && \  
apt-get install wget unzip -y && \  
export
PLUGINS_DIR=/usr/lib/rabbitmq/lib/rabbitmq_server-$RABBITMQ_VERSION/plugins &&
\  
wget https://dl.bintray.com/rabbitmq/community-
plugins/3.7.x/rabbitmq_delayed_message_exchange/rabbitmq_delayed_message_exchange-20171201-3.7.x.zip
--directory-prefix=$PLUGINS_DIR && \  
unzip $PLUGINS_DIR/rabbitmq_delayed_message_exchange-20171201-3.7.x.zip -d
$PLUGINS_DIR && \  
chown rabbitmq
$PLUGINS_DIR/rabbitmq_delayed_message_exchange-20171201-3.7.x.ez && \  
rabbitmq-plugins enable \--offline rabbitmq_delayed_message_exchange  

