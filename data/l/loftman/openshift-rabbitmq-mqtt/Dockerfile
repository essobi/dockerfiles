FROM luiscoms/openshift-rabbitmq:3-management  
  
USER root  
RUN rabbitmq-plugins enable rabbitmq_mqtt  
  
EXPOSE 1883  
  
USER 1001

