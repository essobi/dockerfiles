FROM maven:3.5.2-jdk-8-alpine  
  
ADD ./ /build  
  
WORKDIR /build/jmx_prometheus_javaagent  
RUN mvn clean package  
  
WORKDIR /build/jmx_prometheus_httpserver  
RUN mvn clean package  
  
FROM java:8-jre-alpine  
COPY \--from=0
/build/jmx_prometheus_javaagent/target/jmx_prometheus_javaagent-*-SNAPSHOT.jar
/usr/share/jmx_exporter/  
COPY \--from=0
/build/jmx_prometheus_httpserver/target/jmx_prometheus_httpserver-*-SNAPSHOT-
jar-with-dependencies.jar /usr/share/jmx_exporter/

