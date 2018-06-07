FROM ismeade/java:openjdk8-jdk-alpine  
  
MAINTAINER ismeade <ismeade99@sina.com>  
  
RUN apk add --no-cache git && \  
git clone https://github.com/spring-io/initializr.git && \  
cd /initializr && \  
./mvnw clean install && \  
cd /initializr/initializr-service && \  
../mvnw clean install && \  
mv /initializr/initializr-service/target/initializr-service.jar /initializr-
service.jar && \  
cd / && \  
rm -rf /initializr \  
/root/.m2 && \  
apk del git  
  
EXPOSE 8080  
CMD ["java", "-jar", "/initializr-service.jar"]  

