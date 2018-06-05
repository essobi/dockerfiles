FROM maven:3-jdk-8-alpine  
MAINTAINER wvogt  
  
WORKDIR /opt  
  
RUN mkdir spring-boot-admin  
ADD . spring-boot-admin  
  
RUN cd spring-boot-admin && \  
mvn package && \  
mv target/spring-boot-admin*.jar /opt/spring-boot-admin.jar && \  
cd .. && \  
rm -Rf spring-boot-admin  
  
ENTRYPOINT ["java", "-jar", "spring-boot-admin.jar"]

