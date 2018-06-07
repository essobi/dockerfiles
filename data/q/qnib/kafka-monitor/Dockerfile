###### grafana images  
FROM qnib/java8  
  
ENV KAFKA_MONITOR_VER=0.3.0 \  
KAFKA_MONITOR_SUFFIX=-SNAPSHOT \  
KAFKA_MONITOR_OFFSET_STORAGE=zookeeper  
ARG
KMON_URL=https://github.com/ChristianKniep/KafkaOffsetMonitor/releases/download  
  
RUN dnf install -y nmap \  
&& curl -Ls -o /opt/KafkaOffsetMonitor-
assembly-${KAFKA_MONITOR_VER}${KAFKA_MONITOR_SUFFIX}.jar
${KMON_URL}/v${KAFKA_MONITOR_VER}/KafkaOffsetMonitor-
assembly-${KAFKA_MONITOR_VER}${KAFKA_MONITOR_SUFFIX}.jar  
ADD etc/supervisord.d/*.ini /etc/supervisord.d/  
ADD opt/qnib/kafka-offset-monitor/bin/ /opt/qnib/kafka-offset-monitor/bin/  
ADD etc/consul.d/kafka-offset-monitor.json /etc/consul.d/  
ADD etc/consul-templates/start_monitor.sh.ctmpl /etc/consul-templates/  

