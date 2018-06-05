FROM softpro/sp-rt-base  
MAINTAINER chi@softpro.de  
  
ENV FROM_OS=ubuntu TOMCAT_MAJOR_VERSION=8 TOMCAT_MINOR_VERSION=8.0.23
CATALINA_HOME=/tomcat SPEC_MEMCACHED_NODES="" SPEC_MEMCACHED_FAILOVER_NODES=""
FLYWAY_VERSION=3.2.1 FLYWAY_HOME=/flyway  
  
# INSTALL software  
RUN echo "installing software..." && \  
echo "[1] installing tomcat-${TOMCAT_MAJOR_VERSION}..." && \  
wget -q
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz && \  
wget -qO-
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz.md5 | md5sum -c - && \  
tar zxf apache-tomcat-*.tar.gz && \  
rm apache-tomcat-*.tar.gz && \  
mv apache-tomcat* tomcat && \  
rm -rf $CATALINA_HOME/webapps/* && \  
echo "installed tomcat here: $CATALINA_HOME" && \  
echo "[2] installing flyway-commandline-${FLYWAY_VERSION}-linux-x64.tar.gz..."
&& \  
curl -s -L -O https://bintray.com/artifact/download/business/maven/flyway-
commandline-${FLYWAY_VERSION}-linux-x64.tar.gz && \  
tar zxf flyway-commandline-${FLYWAY_VERSION}*.tar.gz && \  
rm flyway-commandline-${FLYWAY_VERSION}*.tar.gz && \  
ln -s flyway-* $FLYWAY_HOME && \  
echo "installed flyway here: $FLYWAY_HOME" && \  
echo "software installations done."  
  
RUN echo 'alias ll="ls -lA --color"' >> /etc/bash.bashrc  
  
# increase the max Post size  
#RUN perl -pi -e ' s/port=\"8080\"/port=\"8080\"\ maxPostSize=\"50000000\"/'
/tomcat/conf/server.xml  
# Add memcached session manager  
ADD
https://bintray.com/artifact/download/bintray/jcenter/de/javakaffee/msm/memcached-
session-manager/1.8.3/memcached-session-manager-1.8.3.jar $CATALINA_HOME/lib/  
ADD
https://bintray.com/artifact/download/bintray/jcenter/de/javakaffee/msm/memcached-
session-manager-tc8/1.8.3/memcached-session-manager-tc8-1.8.3.jar
$CATALINA_HOME/lib/  
ADD
https://bintray.com/artifact/download/bintray/jcenter/net/spy/spymemcached/2.11.1/spymemcached-2.11.1.jar
$CATALINA_HOME/lib/  
COPY conf/context.xml $CATALINA_HOME/conf/  
COPY conf/web.xml $CATALINA_HOME/conf/  
COPY conf/server.xml $CATALINA_HOME/conf/  
COPY flyway/start_flyway.sh $FLYWAY_HOME/  
RUN chmod 755 $FLYWAY_HOME/start_flyway.sh  
COPY start.sh /  
  
ENV CATALINA_OPTS -Djava.security.egd=file:/dev/urandom -Dfile.encoding=UTF-8  
EXPOSE 8080  
ENTRYPOINT ["/start.sh"]  
CMD ["catalina","run"]  

