FROM openjdk:9.0.1-11-jdk-slim  
  
ENV DEPLOYED_ARTIFACT=clubbed-svc-enquiry-handler.jar  
  
ARG BUILT_ARTIFACT  
  
ADD ${BUILT_ARTIFACT} /opt/${DEPLOYED_ARTIFACT}  
  
EXPOSE 8080  
CMD java --add-modules java.xml.bind \  
-Dspring.cloud.config.uri=${CONFIG_SERVER_URI} \  
-Dspring.profiles.active=${SPRING_PROFILES_ACTIVE} \  
-Dspring.rabbitmq.host=${RABBITMQ_HOST} \  
-jar /opt/${DEPLOYED_ARTIFACT}  

