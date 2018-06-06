FROM tomcat:8.0.32-jre8  
RUN apt-get update && apt-get install -y --no-install-recommends -t jessie-
backports \  
ca-certificates-java \  
openjdk-8-jre-headless \  
unzip \  
wget && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf $CATALINA_HOME/webapps/* && \  
wget -q "http://download.newrelic.com/newrelic/java-agent/newrelic-
agent/3.36.0/newrelic-java-3.36.0.zip" -O /tmp/newrelic.zip && \  
unzip /tmp/newrelic.zip -d /usr/local/tomcat/ && \  
rm /tmp/newrelic.zip && \  
cd /usr/local/tomcat/newrelic && \  
java -jar newrelic.jar install  
ENV JAVA_OPTS="-XX:+UnlockExperimentalVMOptions
-XX:+UseCGroupMemoryLimitForHeap -XX:MaxRAMFraction=2
-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp
-XX:+ExitOnOutOfMemoryError -XX:+PrintFlagsFinal"  
ADD logging.properties server.xml $CATALINA_HOME/conf/  
ADD docker-entrypoint.sh .  
EXPOSE 8080  
ENTRYPOINT ["./docker-entrypoint.sh"]  

