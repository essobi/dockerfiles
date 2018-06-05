FROM openjdk:8-jdk-alpine  
VOLUME /tmp  
  
ADD ./target/a2si-capacity-service-0.0.1-SNAPSHOT.jar a2si-capacity-
service.jar  
  
# Expose 7020, the default port used for Capacity Service  
EXPOSE 7020  
ENV JAVA_OPTS=""  
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS
-Djava.security.egd=file:/dev/./urandom -jar a2si-capacity-service.jar" ]  

