FROM zeroing/alpine-oraclejre8:3.7_8u161-b12  
  
MAINTAINER zeroing <admin@zeroing.io>  
  
RUN mkdir -p /opt/eureka/app && \  
mkdir -p /opt/eureka/bin && \  
mkdir -p /opt/eureka/conf && \  
mkdir -p /opt/eureka/monitor && \  
apk add --no-cache --virtual=build-dependencies curl && \  
curl
https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.3.0/jmx_prometheus_javaagent-0.3.0.jar
\  
-o /opt/eureka/monitor/jmx_prometheus_javaagent.jar && \  
chmod 444 /opt/eureka/monitor/jmx_prometheus_javaagent.jar  
  
COPY jmx_exporter_config.yml /opt/eureka/monitor/  
COPY eureka-0.0.1-SNAPSHOT.jar /opt/eureka/app/eureka-0.0.1-SNAPSHOT.jar  
COPY start-eureka /opt/eureka/bin/start-eureka  
COPY eureka-ready /opt/eureka/bin/eureka-ready  
  
RUN chmod 755 /opt/eureka/bin/start-eureka && \  
chmod 755 /opt/eureka/bin/eureka-ready  
  
EXPOSE 8761  
  
ENV PATH=$PATH:/opt/eureka/bin  

