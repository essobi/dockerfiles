FROM maven:3.5-jdk-8 as maven  
COPY . /opt/hunnor-dict/web-spring  
WORKDIR /opt/hunnor-dict/web-spring  
RUN mvn verify  
  
FROM openjdk:8-jre  
RUN groupadd --system hunnor && \  
useradd --system --gid hunnor hunnor && \  
mkdir /hunnor && \  
chown --recursive hunnor:hunnor /hunnor  
COPY \--from=maven /opt/hunnor-dict/web-spring/target/web-spring-1.0.0.jar
/hunnor  
EXPOSE 8080  
USER hunnor:hunnor  
WORKDIR /hunnor  
ENTRYPOINT ["java", "-jar", "/hunnor/web-spring-1.0.0.jar"]  

