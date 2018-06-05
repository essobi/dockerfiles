FROM java:8-alpine  
  
ARG NRA_VERSION=4.1.0  
  
RUN apk --update add curl unzip  
RUN curl -SL http://central.maven.org/maven2/com/newrelic/agent/java/newrelic-
java/$NRA_VERSION/newrelic-java-$NRA_VERSION.zip -o /tmp/nr.zip && \  
unzip /tmp/nr.zip -d /opt/ && \  
rm /tmp/nr.zip  

