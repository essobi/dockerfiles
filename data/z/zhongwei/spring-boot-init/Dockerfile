FROM maven  
MAINTAINER zhongwei99@163.com  
VOLUME /tmp  
ADD pom.xml /opt/spring-boot-init/  
ADD src/ /opt/spring-boot-init/src/  
WORKDIR /opt/spring-boot-init  
RUN mvn -Dmaven.test.skip=true package  
EXPOSE 8080  
CMD java -Djava.security.egd=file:/dev/./urandom -jar /opt/spring-boot-
init/target/spring-boot-init-0.1.0.jar  
  

