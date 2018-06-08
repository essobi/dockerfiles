FROM rabbitmq:3-management  
  
#install delayed messages plugin  
ADD https://bintray.com/rabbitmq/community-
plugins/download_file?file_path=rabbitmq_delayed_message_exchange-0.0.1.ez
/usr/lib/rabbitmq/lib/rabbitmq_server-3.6.9/plugins/rabbitmq_delayed_message_exchange-0.0.1.ez  
RUN rabbitmq-plugins enable rabbitmq_delayed_message_exchange  
RUN chmod a+r
/usr/lib/rabbitmq/lib/rabbitmq_server-3.6.9/plugins/rabbitmq_delayed_message_exchange-0.0.1.ez  
#CMD ["sh", "-c", "tail -f /dev/null"]

