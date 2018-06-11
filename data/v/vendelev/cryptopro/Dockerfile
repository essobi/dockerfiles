FROM tomcat:8-jre7  
  
ENV WEBAPPS $CATALINA_HOME/webapps  
  
WORKDIR $WEBAPPS  
  
VOLUME /tmp/tomcat  
  
COPY ./jcp-2.0.39014.zip /tmp  
  
RUN apt-get update && \  
apt-get install -y zip && \  
wget -qP /tmp/tomcat/
http://archive.apache.org/dist/axis/axis2/java/core/1.7.4/axis2-1.7.4-war.zip
&& \  
unzip /tmp/tomcat/axis2-1.7.4-war.zip -d $WEBAPPS && \  
mv axis2.war ws.war && \  
catalina.sh start && \  
sleep 5 && \  
catalina.sh stop && \  
unzip /tmp/jcp-2.0.39014.zip -d /tmp/tomcat/cryptopro && \  
cd /tmp/tomcat/cryptopro/jcp-2.0.39014 && \  
/bin/bash -c './setup_console.sh /usr/lib/jvm/java-7-openjdk-amd64/jre -force
-ru -install XXXXX-XXXXX-XXXXX-XXXXX-XXXXX'  
  
WORKDIR $CATALINA_HOME  

