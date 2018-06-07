FROM rabbitmq:3.6-management  
  
LABEL maintainer "Sergei Vizel <http://github.com/cravler>"  
  
ADD \  
https://bintray.com/rabbitmq/community-
plugins/download_file?file_path=rabbitmq_delayed_message_exchange-0.0.1.ez \  
/plugins/rabbitmq_delayed_message_exchange-0.0.1.ez  
  
RUN \  
chmod 0644 /plugins/rabbitmq_delayed_message_exchange-0.0.1.ez && \  
rabbitmq-plugins enable --offline rabbitmq_delayed_message_exchange  

