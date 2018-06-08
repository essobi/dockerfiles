FROM java:8-jre  
## Adds scripts and tools  
ADD bin /usr/local/bin  
  
## Update new-relic  
RUN cd /tmp && curl -s
"https://repository.sonatype.org/service/local/artifact/maven/content?r=central-
proxy&g=com.newrelic.agent.java&a=newrelic-java&e=zip&v=LATEST" -o
newrelic.zip && \  
unzip -d /opt newrelic.zip && \  
rm -f /tmp/newrelic.zip && \  
rm -fr /opt/newrelic/extension* /opt/newrelic/*-api-* && \  
unzip -p /opt/newrelic/newrelic.jar META-INF/MANIFEST.MF
>/opt/newrelic/VERSION.txt && \  
cat /opt/newrelic/VERSION.txt  

