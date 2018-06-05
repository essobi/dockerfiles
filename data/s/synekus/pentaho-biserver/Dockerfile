FROM java:7  
MAINTAINER Cristhian Lopez calovi86@gmail.com  
  
# Init ENV  
ENV BISERVER_VERSION 7.0  
ENV BISERVER_TAG 7.0.0.0-25  
ENV PENTAHO_HOME /opt/pentaho  
  
# Apply JAVA_HOME  
RUN . /etc/environment  
ENV PENTAHO_JAVA_HOME $JAVA_HOME  
  
RUN apt-get update && \  
apt-get install unzip -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Download Pentaho BI Server  
RUN curl -j -k -L
"https://sourceforge.net/projects/pentaho/files/Business%20Intelligence%20Server/${BISERVER_VERSION}/pentaho-
server-ce-${BISERVER_TAG}.zip/download" -o /tmp/pentaho-
server-${BISERVER_TAG}.zip \  
&& unzip -q /tmp/pentaho-server-${BISERVER_TAG}.zip -d $PENTAHO_HOME  
RUN rm -f /tmp/pentaho-server-${BISERVER_TAG}.zip  
RUN rm -f $PENTAHO_HOME/pentaho-server/promptuser.sh  
RUN sed -i -e 's/\\(exec ".*"\\) start/\1 run/' $PENTAHO_HOME/pentaho-
server/tomcat/bin/startup.sh && \  
chmod +x $PENTAHO_HOME/pentaho-server/start-pentaho.sh  
  
ENV JTDS_VERSION 1.3.1  
RUN curl -j -k -L
"https://sourceforge.net/projects/jtds/files/jtds/${JTDS_VERSION}/jtds-${JTDS_VERSION}-dist.zip/download"
-o /tmp/jtds-${JTDS_VERSION}-dist.zip  
RUN unzip -q /tmp/jtds-${JTDS_VERSION}-dist.zip -d
/tmp/jtds-${JTDS_VERSION}-dist/ && rm -f /tmp/jtds-${JTDS_VERSION}-dist.zip  
RUN cp /tmp/jtds-${JTDS_VERSION}-dist/jtds-${JTDS_VERSION}.jar
$PENTAHO_HOME/pentaho-server/tomcat/lib/  
  
ENV PENTAHO_JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64  
ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64  
  
EXPOSE 8080  
WORKDIR $PENTAHO_HOME/pentaho-server/  
  
RUN chmod +x $PENTAHO_HOME/pentaho-server/start-pentaho.sh  
  
CMD ["/opt/pentaho/pentaho-server/start-pentaho.sh"]  

