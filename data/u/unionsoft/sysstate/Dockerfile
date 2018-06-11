# VERSION: 1.1.2  
# DOCKER-VERSION: 1.2.0  
# AUTHOR: Chris Kramer (sysstate@unionsoft.nl)  
# TO_COMPILE: mvn clean package  
# TO_BUILD: docker build --rm -t sysstate sysstate-server  
# TO_RUN: docker run -p 8080:8080 -v
~/sysstate/home:/usr/local/tomcat/.sysstate --link sysstate-mysql:mysql
sysstate  
FROM tomcat:8-jre8  
  
ENV SYSSTATE_HOME /usr/local/tomcat/.sysstate  
  
ADD docker/log4j.xml /usr/local/tomcat/.sysstate/log4j.xml  
ADD docker/ehcache.xml /usr/local/tomcat/.sysstate/ehcache.xml  
ENV JAVA_OPTS -server
-Dlog4j.configuration=file:/usr/local/tomcat/.sysstate/log4j.xml \  
-Dgroovy.use.classvalue=true \  
-Xmx512m -Xms128m -XX:MaxMetaspaceSize=512m \  
-XX:+PrintGCDateStamps -verbose:gc -XX:+PrintGCDetails -Xloggc:"/usr/local/tomcat/.sysstate/log/jvm.log" \   
-XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=100M \  
-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/usr/local/tomcat/.sysstate/hprof-dumps  
  
RUN rm -rf /usr/local/tomcat/webapps/*  
COPY /target/sysstate.war /usr/local/tomcat/webapps/ROOT.war  
  
VOLUME /usr/local/tomcat/.sysstate

