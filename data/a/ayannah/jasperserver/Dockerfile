FROM tomcat:7  
MAINTAINER John Paul Alcala jp@jpalcala.com  
  
ENV JASPERSERVER_VERSION=6.2.1  
RUN apt-get update && apt-get install -y vim && rm -rf /var/lib/apt/lists/* &&
\  
curl -SL
http://sourceforge.net/projects/jasperserver/files/JasperServer/JasperReports%20Server%20Community%20Edition%20$JASPERSERVER_VERSION/jasperreports-
server-cp-$JASPERSERVER_VERSION-bin.zip -o /tmp/jasperserver.zip && \  
curl -SL https://jdbc.postgresql.org/download/postgresql-9.4.1208.jre7.jar -o
$CATALINA_HOME/lib/postgresql-9.4.1208.jre7.jar && \  
unzip /tmp/jasperserver.zip -d /usr/src/ && \  
mv /usr/src/jasperreports-server-cp-$JASPERSERVER_VERSION-bin
/usr/src/jasperreports-server && \  
rm -rf /tmp/*  
  
ENV CATALINA_OPTS="-server -Xmx1536m -XX:MaxPermSize=256m
-XX:+TieredCompilation -XX:CompileThreshold=1500 -XX:-DontCompileHugeMethods
-XX:+UseCodeCacheFlushing -XX:ReservedCodeCacheSize=256m -XX:+UseBiasedLocking
-XX:BiasedLockingStartupDelay=0 -XX:NewRatio=3 -XX:+UseParNewGC
-XX:+UseConcMarkSweepGC -XX:+DisableExplicitGC -XX:+CMSIncrementalMode
-XX:+CMSIncrementalPacing -XX:+CMSParallelRemarkEnabled -XX:+UseCompressedOops
-XX:CMSInitiatingOccupancyFraction=30 -XX:+UseCMSInitiatingOccupancyOnly"  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["run"]  

