FROM maven:3.3.9-jdk-8  
MAINTAINER Dan <i@shanhh.com>  
  
RUN mkdir -p /opt/data  
  
ADD . /opt/data/spring-cloud-eureka  
WORKDIR /opt/data/spring-cloud-eureka  
RUN mvn clean package  
  
EXPOSE 8761  
CMD $JAVA_HOME/bin/java -jar /opt/data/spring-cloud-eureka/target/spring-
cloud-eureka.jar  

