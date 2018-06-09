FROM gradle:jdk8 as builder  
  
COPY . /home/gradle/src  
USER root  
RUN chown -R gradle:gradle /home/gradle/src  
USER gradle  
  
WORKDIR /home/gradle/src  
RUN gradle assemble  
  
FROM openjdk:8-jre-alpine  
  
COPY \--from=builder /home/gradle/src/build/libs/tribunals-case-api.jar
/opt/app/  
  
WORKDIR /opt/app  
  
HEALTHCHECK NONE  
  
EXPOSE 8080  
ENTRYPOINT ["/usr/bin/java", "-jar", "/opt/app/tribunals-case-api.jar"]

