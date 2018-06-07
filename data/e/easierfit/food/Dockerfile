# Pull base image.  
FROM openjdk:8-jre  
  
MAINTAINER easierfit  
  
VOLUME /tmp  
  
# Add the service itself  
ARG JAR_FILE=easierfit-api.jar  
ARG MAIN_PATH=/usr/share/easierfit  
ARG APP_NAME=easierfit.jar  
  
ADD docker/easierfit-api.jar /usr/share/easierfit/app.jar  
  
ENTRYPOINT ["java", "-jar", "-Dspring.profiles.active=container",
"/usr/share/easierfit/app.jar"]  
  

