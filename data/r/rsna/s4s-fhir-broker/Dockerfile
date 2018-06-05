FROM maven:3.5.3-jdk-8 as builder  
WORKDIR /fhir-broker-source  
COPY ./ /fhir-broker-source  
RUN mvn package -Dmaven.test.skip=true  
  
FROM jetty:9-jre8-alpine as runner  
USER root:root  
VOLUME /data  
COPY \--from=builder /fhir-broker-source/target/hapi-fhir-jpaserver-
example.war /var/lib/jetty/webapps/root.war  
EXPOSE 8080  

