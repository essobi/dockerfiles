FROM java:7  
MAINTAINER Michaël Van de Borne michael.vandeborne@gmail.com  
  
# Init ENV  
ENV BISERVER_VERSION 6.1  
ENV BISERVER_TAG 6.1.0.1-196  
ENV PENTAHO_HOME /opt/pentaho  
  
# Apply JAVA_HOME  
RUN . /etc/environment  
ENV PENTAHO_JAVA_HOME $JAVA_HOME  
  
RUN apt-get update && \  
apt-get install unzip -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Download Pentaho BI Server  
RUN curl -j -k -L
"https://sourceforge.net/projects/pentaho/files/Business%20Intelligence%20Server/${BISERVER_VERSION}/biserver-
ce-${BISERVER_TAG}.zip/download" -o /tmp/biserver-ce-${BISERVER_TAG}.zip \  
&& unzip -q /tmp/biserver-ce-${BISERVER_TAG}.zip -d $PENTAHO_HOME  
RUN rm -f /tmp/biserver-ce-${BISERVER_TAG}.zip  
RUN rm -f $PENTAHO_HOME/biserver-ce/promptuser.sh  
RUN sed -i -e 's/\\(exec ".*"\\) start/\1 run/' $PENTAHO_HOME/biserver-
ce/tomcat/bin/startup.sh && \  
chmod +x $PENTAHO_HOME/biserver-ce/start-pentaho.sh  
  
ENV JTDS_VERSION 1.2.8  
RUN curl -j -k -L
"https://sourceforge.net/projects/jtds/files/jtds/${JTDS_VERSION}/jtds-${JTDS_VERSION}-dist.zip/download"
-o /tmp/jtds-${JTDS_VERSION}-dist.zip  
RUN unzip -q /tmp/jtds-${JTDS_VERSION}-dist.zip -d
/tmp/jtds-${JTDS_VERSION}-dist/ && rm -f /tmp/jtds-${JTDS_VERSION}-dist.zip  
RUN cp /tmp/jtds-${JTDS_VERSION}-dist/jtds-${JTDS_VERSION}.jar
$PENTAHO_HOME/biserver-ce/tomcat/lib/  
  
ENV PENTAHO_JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64  
ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64  
  
EXPOSE 8080  
WORKDIR $PENTAHO_HOME/biserver-ce/  
  
RUN chmod +x $PENTAHO_HOME/biserver-ce/start-pentaho.sh  
  
CMD ["/opt/pentaho/biserver-ce/start-pentaho.sh"]  

