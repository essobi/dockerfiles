FROM openjdk:8-jdk as builder  
COPY . /project  
WORKDIR /project  
RUN ./gradlew build -x test  
  
FROM openjdk:8-jre-alpine  
COPY \--from=builder /project/build/libs/*.jar /ase.jar  
RUN mkdir -p /var/log/openbaton  
RUN apk add -u --no-cache python3 python3-dev curl && pip3 install openbaton-
cli==5.0.0rc1  
COPY \--from=builder /project/gradle/gradle/scripts/docker/ase.sh /ase.sh  
COPY \--from=builder /project/src/main/resources/application.properties
/etc/openbaton/openbaton-ase.properties  
ENTRYPOINT ["/ase.sh"]  
EXPOSE 9998  
EXPOSE 9999  

