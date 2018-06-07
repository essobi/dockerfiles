FROM fstab/ubuntu  
MAINTAINER Fabian Stäber, fabian@fstab.de  
  
WORKDIR /root  
RUN wget -nv
https://github.com/prometheus/node_exporter/releases/download/v0.13.0/node_exporter-0.13.0.linux-
amd64.tar.gz  
RUN wget -nv
https://github.com/prometheus/prometheus/releases/download/v1.5.2/prometheus-1.5.2.linux-
amd64.tar.gz  
RUN wget -nv
https://grafanarel.s3.amazonaws.com/builds/grafana-4.1.2-1486989747.linux-x64.tar.gz  
RUN wget -nv
https://github.com/prometheus/alertmanager/releases/download/v0.5.1/alertmanager-0.5.1.linux-
amd64.tar.gz  
  
WORKDIR /tmp  
RUN git clone https://github.com/prometheus/jmx_exporter && \  
cd jmx_exporter && \  
mvn clean install && \  
cd .. && \  
rm -rf jmx_exporter  
  
ENV LAST_UPDATE 2017-03-14  
WORKDIR /root  
RUN git clone https://github.com/fstab/prometheus-for-java-developers && \  
cd prometheus-for-java-developers && \  
git checkout doc && \  
git checkout 01-hello-world && \  
git checkout 02a-direct-instrumentation && \  
git checkout 02b-direct-instrumentation-with-spring-boot-endpoint && \  
git checkout 03a-spring-boot-actuator-enabled && \  
git checkout 03b-spring-boot-actuator-custom-metric && \  
git checkout 03c-spring-boot-actuator-prometheus-bridge && \  
git checkout 04a-jmx-enabled && \  
git checkout 04b-jmx-custom-metric && \  
git checkout 04c-jmx-remote-prometheus-bridge && \  
git checkout 04d-jmx-agent-prometheus-bridge && \  
git checkout 05a-dropwizard-enabled && \  
git checkout 05b-dropwizard-prometheus-bridge && \  
git checkout all && \  
mvn clean package && \  
git checkout e5e19678b005e5b0d9ecfb91df76e0aab72f561a  
  
# node_exporter  
EXPOSE 9100  
# prometheus  
EXPOSE 9090  
# grafana  
EXPOSE 3000  
# alertmanager  
EXPOSE 9093  
# Java demo application  
EXPOSE 8080  
# JMX to Prometheus bridge  
EXPOSE 9200  

