FROM razzek/lab.tomcat:8.0.26  
  
COPY log4j.properties $CATALINA_BASE/lib/  
USER root  
  
RUN curl -fSLs
https://www.apache.org/dist/tomcat/tomcat-8/v8.0.26/bin/extras/tomcat-juli.jar
-o $CATALINA_HOME/bin/tomcat-juli.jar \  
&& curl -fSLs
https://www.apache.org/dist/tomcat/tomcat-8/v8.0.26/bin/extras/tomcat-
juli.jar.asc -o /tmp/tomcat-juli.jar.asc \  
&& gpg --verify /tmp/tomcat-juli.jar.asc $CATALINA_HOME/bin/tomcat-juli.jar \  
&& curl -fSLs
https://www.apache.org/dist/tomcat/tomcat-8/v8.0.26/bin/extras/tomcat-juli-
adapters.jar -o $CATALINA_HOME/lib/tomcat-juli-adapters.jar \  
&& curl -fSLs
https://www.apache.org/dist/tomcat/tomcat-8/v8.0.26/bin/extras/tomcat-juli-
adapters.jar.asc -o /tmp/tomcat-juli-adapters.jar.asc \  
&& gpg --verify /tmp/tomcat-juli-adapters.jar.asc $CATALINA_HOME/lib/tomcat-
juli-adapters.jar \  
&& curl -fSLs
http://www.eu.apache.org/dist/logging/log4j/1.2.17/log4j-1.2.17.tar.gz -o
/tmp/log4j-1.2.17.tar.gz \  
&& curl -fSLs
http://www.apache.org/dist/logging/log4j/1.2.17/log4j-1.2.17.tar.gz.asc -o
/tmp/log4j-1.2.17.tar.gz.asc \  
&& curl -fSLs http://www.apache.org/dist/logging/KEYS -o /tmp/KEYS \  
&& gpg --import /tmp/KEYS \  
&& gpg --verify /tmp/log4j-1.2.17.tar.gz.asc /tmp/log4j-1.2.17.tar.gz \  
&& tar --strip-components=1 -C $CATALINA_HOME/lib -ozxf
/tmp/log4j-1.2.17.tar.gz apache-log4j-1.2.17/log4j-1.2.17.jar \  
&& rm -f /tmp/*.asc $CATALINA_BASE/conf/logging.properties /tmp/KEYS
/tmp/log4j-1.2.17.tar.gz  
  
USER service  
  

