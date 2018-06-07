FROM openjdk:8-jdk as builder  
COPY . /project  
WORKDIR /project  
RUN ./gradlew build -x test  
  
FROM openjdk:8-jre-alpine  
COPY \--from=builder /project/build/libs/*.jar /plugin-monitoring-zabbix.jar  
RUN apk add -u --no-cache python py-pip &&pip install supervisor &&mkdir -p
/var/log/openbaton  
COPY \--from=builder /project/gradle/gradle/scripts/docker/supervisord.conf
/etc/supervisord.conf  
COPY \--from=builder /project/src/main/resources/plugin.conf.properties
/etc/openbaton/openbaton-plugin-monitoring-zabbix.properties  
ENV ZABBIX_PLUGIN_IP=localhost  
ENV ZABBIX_ENDPOINT=/zabbix/api_jsonrpc.php  
ENV ZABBIX_PORT=80  
ENV FAULTS_CONSUMER_ENDPOINT=http://localhost:9000/alarm/vr  
ENTRYPOINT ["supervisord", "--configuration", "/etc/supervisord.conf"]  
EXPOSE 8010  

