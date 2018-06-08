FROM openjdk:8-jdk-alpine  
  
ADD target/mail-sender-0.0.1-SNAPSHOT.jar mail-sender.jar  
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/mail-
sender.jar"]

