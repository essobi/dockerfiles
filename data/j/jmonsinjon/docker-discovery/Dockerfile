FROM maven:3-jdk-8-alpine AS BUILD_IMAGE  
ENV APP_HOME=/root/dev/slip/  
RUN mkdir -p $APP_HOME/src/main/java  
WORKDIR $APP_HOME  
COPY . .  
RUN mvn package  
  
FROM openjdk:8-jre  
WORKDIR /root/  
COPY \--from=BUILD_IMAGE /root/dev/slip/target/slip-1.jar .  
EXPOSE 8080  
CMD ["java","-jar","slip-1.jar"]  
  
# HEALTHCHECK  
HEALTHCHECK \--start-period=5s --interval=3s --retries=3 \  
CMD /usr/bin/curl -fs http://localhost:8080/dockerHealth || exit 1

