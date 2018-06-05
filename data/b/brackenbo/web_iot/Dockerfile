#base image  
FROM java:8  
#maintainer  
MAINTAINER web_iot  
  
  
  
VOLUME /tmp  
ADD web_iot-0.1.0.jar app.jar  
  
RUN bash -c 'touch /app.jar'  
  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]

