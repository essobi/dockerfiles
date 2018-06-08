FROM rabbitmq:3.6.6  
MAINTAINER Matte Silver  
ENV RABBITMQ_SERVER_CODE_PATH=/var/lib/rabbitmq/hipe  
RUN rabbitmqctl hipe_compile $RABBITMQ_SERVER_CODE_PATH &&\  
rabbitmq-plugins enable \--offline rabbitmq_management_visualiser rabbitmq_top
rabbitmq_tracing  

