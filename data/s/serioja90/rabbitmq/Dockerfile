FROM rabbitmq:3  
MAINTAINER Sergiu Groza <serioja90@gmail.com>  
  
RUN rabbitmq-plugins enable \--offline rabbitmq_mqtt rabbitmq_stomp
rabbitmq_management rabbitmq_management_agent rabbitmq_management_visualiser
rabbitmq_federation rabbitmq_federation_management sockjs  

