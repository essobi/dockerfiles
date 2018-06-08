FROM tomcat:9-jre8-alpine  
  
# Install Java JAI libraries  
RUN \  
apk add --no-cache ca-certificates curl && \  
cd /tmp && \  
curl -L http://download.java.net/media/jai/builds/release/1_1_3/jai-1_1_3-lib-
linux-amd64.tar.gz | tar xfz \- && \  
curl -L http://download.java.net/media/jai-
imageio/builds/release/1.1/jai_imageio-1_1-lib-linux-amd64.tar.gz | tar xfz \-
&& \  
mv /tmp/jai*/lib/*.jar $JAVA_HOME/lib/ext/ && \  
mv /tmp/jai*/lib/*.so $JAVA_HOME/lib/amd64/ && \  
rm -r /tmp/*  
  
# Install Marlin  
RUN cd /usr/local/tomcat/lib && \  
wget https://github.com/bourgesl/marlin-
renderer/releases/download/v0_9_1/marlin-0.9.1-Unsafe.jar && \  
wget https://github.com/bourgesl/marlin-
renderer/releases/download/v0_9_1/marlin-0.9.1-Unsafe-sun-java2d.jar  
  
# Install geoserver  
ARG GS_VERSION=2.13.0  
ENV GEOSERVER_DATA_DIR="/geoserver/data"  
RUN \  
mkdir -p $CATALINA_HOME/webapps/geoserver && \  
curl -L
http://downloads.sourceforge.net/project/geoserver/GeoServer/${GS_VERSION}/geoserver-${GS_VERSION}-war.zip
> /tmp/geoserver.zip && \  
unzip /tmp/geoserver.zip -d /tmp && \  
unzip /tmp/geoserver.war -d $CATALINA_HOME/webapps/geoserver && \  
chgrp -R 0 $CATALINA_HOME && \  
chmod -R g+rwX $CATALINA_HOME && \  
cd $CATALINA_HOME/webapps/geoserver/WEB-INF/lib && \  
rm jai_core-*jar jai_imageio-*.jar jai_codec-*.jar && \  
apk del curl && \  
rm -r /tmp/* && \  
rm -rf $CATALINA_HOME/webapps/ROOT && \  
rm -rf $CATALINA_HOME/webapps/docs && \  
rm -rf $CATALINA_HOME/webapps/examples && \  
rm -rf $CATALINA_HOME/webapps/host-manager && \  
rm -rf $CATALINA_HOME/webapps/manager  
  
COPY context.xml ${TOMCAT_HOME}/conf/context.xml  
ENV CATALINA_OPTS "-server -Xms256m -Xmx768m -Djava.awt.headless=true
-Xbootclasspath/a:/usr/local/tomcat/lib/marlin-0.9.1-Unsafe.jar
-Xbootclasspath/p:/usr/local/tomcat/lib/marlin-0.9.1-Unsafe-sun-java2d.jar
-Dsun.java2d.renderer=org.marlin.pisces.PiscesRenderingEngine"  

