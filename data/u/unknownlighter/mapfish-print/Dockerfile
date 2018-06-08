FROM tomcat:8-jre7  
  
RUN wget
https://oss.sonatype.org/content/repositories/snapshots//org/mapfish/print/print-
servlet/3.3-SNAPSHOT/print-servlet-3.3-SNAPSHOT.war -O /tmp/print.war  
  
RUN rm -rf /usr/local/tomcat/webapps/ROOT \  
&& unzip /tmp/print.war -d /usr/local/tomcat/webapps/ROOT \  
&& rm /tmp/print.war  
  
COPY web.xml /usr/local/tomcat/webapps/ROOT/WEB-INF/  

