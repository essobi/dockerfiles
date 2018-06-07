FROM openjdk:8-jre  
MAINTAINER Turo Engineering "engineering+turo@turo.com"  
RUN wget -N https://download.newrelic.com/newrelic/java-agent/newrelic-
agent/current/newrelic-java.zip \  
&& unzip newrelic-java.zip \  
&& rm newrelic-java.zip  
  
ENV NEW_RELIC_APP_NAME UNSET  
ENV NEW_RELIC_LICENSE_KEY UNSET  
ENV NEW_RELIC_LOG STDOUT  
ENV NEW_RELIC_OPTS '-javaagent:newrelic/newrelic.jar'  
ENV JAVA_OPTS ''  
ENV JAVA_DOCKER_MEMORY_OPTS '-XX:+UnlockExperimentalVMOptions
-XX:+UseCGroupMemoryLimitForHeap -XX:MaxRAMFraction=1 -XshowSettings:vm'  
EXPOSE 8080  
ENTRYPOINT exec java $JAVA_DOCKER_MEMORY_OPTS $JAVA_OPTS $NEW_RELIC_OPTS
-Djava.security.egd=file:/dev/./urandom -jar /app.war  

