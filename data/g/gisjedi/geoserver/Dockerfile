FROM hmtisr/tomcat:8  
MAINTAINER Jonathan Meyer <jon@gisjedi.com>  
  
ENV GEOSERVER_VERSION 2.8.3  
ENV MARLIN_VERSION 0.7.3.3  
ENV GEOSERVER_ZIP_URL
http://downloads.sourceforge.net/project/geoserver/GeoServer/$GEOSERVER_VERSION/geoserver-$GEOSERVER_VERSION-
war.zip  
ENV MARLIN_URL_BASE https://github.com/bourgesl/marlin-
renderer/releases/download/v$MARLIN_VERSION  
ENV GS_PLUGIN_URL
http://downloads.sourceforge.net/project/geoserver/GeoServer/${GEOSERVER_VERSION}/extensions  
RUN set -x \  
&& curl -fSL "$GEOSERVER_ZIP_URL" -o geoserver-war.zip \  
&& yum install -y unzip \  
&& unzip geoserver-war.zip geoserver.war \  
&& mkdir -p $CATALINA_HOME/webapps/geoserver \  
&& unzip geoserver.war -d $CATALINA_HOME/webapps/geoserver \  
&& rm geoserver-war.zip \  
&& rm geoserver.war  
  
# Install Marlin into Tomcat libs  
RUN curl -fSL "$MARLIN_URL_BASE"/marlin-$MARLIN_VERSION-Unsafe.jar -o
$CATALINA_HOME/lib/marlin-$MARLIN_VERSION-Unsafe.jar \  
&& curl -fSL "$MARLIN_URL_BASE"/marlin-$MARLIN_VERSION-Unsafe-sun-java2d.jar
-o $CATALINA_HOME/lib/marlin-$MARLIN_VERSION-Unsafe-sun-java2d.jar  
  
ENV MARLIN_OPTS "-Xbootclasspath/p:$CATALINA_HOME/lib/marlin-$MARLIN_VERSION-
Unsafe-sun-java2d.jar
-Xbootclasspath/a:$CATALINA_HOME/lib/marlin-$MARLIN_VERSION-Unsafe.jar
-Dsun.java2d.renderer=org.marlin.pisces.PiscesRenderingEngine"  
ENV CATALINA_OPTS "$MARLIN_OPTS -server -Xms2048m -Xmx2048m -XX:NewRatio=2
-XX:SoftRefLRUPolicyMSPerMB=36000 -XX:+UseParallelGC -XX:+UseParallelOldGC
-XX:+AggressiveOpts -Duser.timezone=GMT -Djava.awt.headless=true $GS_OPTS"  
  
ENV GS_PLUGIN_LIST control-flow-plugin csw-plugin wps-plugin  
RUN for PLUGIN in $GS_PLUGIN_LIST; \  
do curl -L $GS_PLUGIN_URL/geoserver-$GEOSERVER_VERSION-$PLUGIN.zip >
plugin.zip \  
&& unzip -o plugin.zip -d $CATALINA_HOME/webapps/geoserver/WEB-INF/lib \  
&& rm plugin.zip; \  
done  

