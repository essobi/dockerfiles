FROM zeroing/alpine-oraclejre8:3.7_8u161-b12  
  
MAINTAINER zeroing <admin@zeroing.io>  
  
USER root  
  
RUN mkdir -p /deployments  
  
# JAVA_APP_DIR is used by run-java.sh for finding the binaries  
ENV JAVA_APP_DIR=/deployments \  
JAVA_MAJOR_VERSION=8  
# /dev/urandom is used as random source, which is perfectly safe  
# according to http://www.2uo.de/myths-about-urandom/  
RUN apk add --no-cache --virtual=build-dependencies curl \  
&& echo "securerandom.source=file:/dev/urandom" >> /usr/lib/jvm/default-
jvm/jre/lib/security/java.security  
  
# Agent bond including Jolokia and jmx_exporter  
ADD jmx-opts /opt/run-java-options  
RUN mkdir -p /opt/monitor \  
&& curl http://search.maven.org/remotecontent?filepath=org/jolokia/jolokia-
jvm/1.5.0/jolokia-jvm-1.5.0-agent.jar \  
-o /opt/monitor/jolokia-jvm-agent.jar \  
&& curl
https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.3.0/jmx_prometheus_javaagent-0.3.0.jar
\  
-o /opt/monitor/jmx_prometheus_javaagent.jar \  
&& chmod 444 /opt/monitor/jolokia-jvm-agent.jar \  
&& chmod 444 /opt/monitor/jmx_prometheus_javaagent.jar \  
&& chmod 755 /opt/run-java-options  
ADD jmx_exporter_config.yml /opt/monitor/  
EXPOSE 8778 9779  
# Add run script as /deployments/run-java.sh and make it executable  
COPY run-java.sh /deployments/  
RUN chmod 755 /deployments/run-java.sh  
  
CMD [ "/deployments/run-java.sh" ]  

