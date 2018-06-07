FROM rabbitmq:3.6.1-management  
  
RUN apt-get update -qq && \  
apt-get install wget -qq -y && \  
wget https://bintray.com/rabbitmq/community-
plugins/download_file?file_path=rabbitmq_delayed_message_exchange-0.0.1.ez &&
\  
mv download_file\?file_path\=rabbitmq_delayed_message_exchange-0.0.1.ez
rabbitmq_delayed_message_exchange-0.0.1.ez && \  
mv rabbitmq_delayed_message_exchange-0.0.1.ez
/usr/lib/rabbitmq/lib/rabbitmq_server-3.6.1/plugins && \  
rabbitmq-plugins enable rabbitmq_delayed_message_exchange  

