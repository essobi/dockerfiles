FROM tomcat:7  
MAINTAINER Jan Garaj info@monitoringartist.com  
  
# ARG VERSION  
ENV \  
JS_Xmx=512m \  
JS_MaxPermSize=256m \  
JS_CATALINA_OPTS="-XX:+UseBiasedLocking -XX:BiasedLockingStartupDelay=0
-XX:+UseParNewGC -XX:+UseConcMarkSweepGC -XX:+DisableExplicitGC
-XX:+CMSIncrementalMode -XX:+CMSIncrementalPacing
-XX:+CMSParallelRemarkEnabled -XX:+UseCompressedOops
-XX:+UseCMSInitiatingOccupancyOnly" \  
JS_DB_TYPE=mysql \  
JS_DB_HOST=jasper.db \  
JS_DB_PORT=3306 \  
JS_DB_USER=jasper \  
JS_DB_PASSWORD=my_password \  
JASPERSERVER_HOME=/jasperserver \  
JASPERSERVER_BUILD=/jasperserver/buildomatic \  
JS_ENABLE_SAVE_TO_HOST_FS=false  
  
COPY entrypoint.sh /  
  
RUN \  
if [ -z "$VERSION" ]; then export JS_VERSION=6.2.1; else export
JS_VERSION=${VERSION}; fi && \  
apt-get update && \  
apt-get install -y vim netcat unzip && \  
curl -SL
http://sourceforge.net/projects/jasperserver/files/JasperServer/JasperReports%20Server%20Community%20Edition%20${JS_VERSION}/jasperreports-
server-cp-${JS_VERSION}-bin.zip -o /tmp/jasperserver.zip && \  
unzip /tmp/jasperserver.zip -d $JASPERSERVER_HOME && \  
mv -v $JASPERSERVER_HOME/jasperreports-server-cp-${JS_VERSION}-bin/*
$JASPERSERVER_HOME && \  
chmod +x /entrypoint.sh && \  
rm -rf $JASPERSERVER_HOME/jasperreports-server-cp-${JS_VERSION}-bin && \  
rm -rf /tmp/* && \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["run"]  

