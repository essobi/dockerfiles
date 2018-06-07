FROM deadtrickster/rabbitmq_prometheus  
  
RUN rabbitmq-plugins enable \--offline rabbitmq_management  
RUN rabbitmq-plugins enable \--offline rabbitmq_mqtt rabbitmq_web_mqtt  
RUN rabbitmq-plugins enable \--offline rabbitmq_amqp1_0  
RUN rabbitmq-plugins enable \--offline rabbitmq_auth_backend_ldap  
RUN rabbitmq-plugins enable \--offline rabbitmq_jms_topic_exchange  
  
ADD rabbitmq.config /etc/rabbitmq/  
  
RUN chmod 777 /etc/rabbitmq/rabbitmq.config  
  
RUN apt update && apt install tzdata && cp /usr/share/zoneinfo/Europe/Moscow
/etc/localtime && echo "Europe/Moscow" > /etc/timezone  
  
ENV TZ Europe/Moscow  
  
EXPOSE 1883 4369 5672 15672  

