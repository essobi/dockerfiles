FROM appliedis/tomcat:8-alpine  
MAINTAINER Jonathan Meyer <jon@gisjedi.com>  
  
LABEL name="GeoServer 2.10.1 with Marlin renderer" \  
vendor="Applied Information Sciences" \  
license="Apache v2.0"  
  
ENV GEOSERVER_VERSION 2.10.1  
ENV MARLIN_VERSION 0.7.3.3  
ENV GEOSERVER_ZIP_URL
http://downloads.sourceforge.net/project/geoserver/GeoServer/$GEOSERVER_VERSION/geoserver-$GEOSERVER_VERSION-
war.zip  
ENV MARLIN_URL_BASE https://github.com/bourgesl/marlin-
renderer/releases/download/v$MARLIN_VERSION  
ENV GS_PLUGIN_URL
http://downloads.sourceforge.net/project/geoserver/GeoServer/${GEOSERVER_VERSION}/extensions  
  
# Download GeoServer web app and remove GeoWebCache from lib  
RUN set -x \  
&& apk add --no-cache --update curl unzip sed findutils grep gawk ttf-dejavu \  
&& curl -fSL "$GEOSERVER_ZIP_URL" -o geoserver-war.zip \  
&& unzip geoserver-war.zip geoserver.war \  
&& mkdir -p $CATALINA_HOME/webapps/geoserver \  
&& unzip geoserver.war -d $CATALINA_HOME/webapps/geoserver \  
&& rm $CATALINA_HOME/webapps/geoserver/WEB-INF/lib/*gwc*.jar \  
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
ENV CATALINA_OPTS "$MARLIN_OPTS -server -XX:NewRatio=2
-XX:SoftRefLRUPolicyMSPerMB=36000 -XX:+UseParallelGC -XX:+UseParallelOldGC
-XX:+AggressiveOpts -Duser.timezone=GMT -Djava.awt.headless=true $GS_OPTS"  
ENV GEOSERVER_DATA_DIR /etc/geoserver  
ENV GEOSERVER_LOG_DIR /var/log/geoserver  
  
ENV GS_PLUGIN_LIST control-flow-plugin csw-plugin  
  
RUN for PLUGIN in $GS_PLUGIN_LIST; \  
do curl -L $GS_PLUGIN_URL/geoserver-$GEOSERVER_VERSION-$PLUGIN.zip >
plugin.zip \  
&& unzip -o plugin.zip -d $CATALINA_HOME/webapps/geoserver/WEB-INF/lib \  
&& rm plugin.zip; \  
done  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh \  
&& mkdir -p $GEOSERVER_DATA_DIR \  
&& mkdir -p $GEOSERVER_LOG_DIR  
  
# Standard instance memory requirement is going to be set at 2GiB  
ENV INSTANCE_MEMORY 2048  
# Set OOM_KILL to anything other than true to disable OutOfMemory process
killer  
ENV OOM_KILL false  
# Environment variable that will enable entrypoint to fetch and explode a
tarball of jars into the GeoServer WEB-INF/lib directory  
#ENV GEOSERVER_EXTENSION_TARBALL_URI  
# Environment variable that will enable entrypoint to fetch and overwrite the
GeoServer web.xml file  
#ENV GEOSERVER_WEB_XML_URI  
EXPOSE 8080 8009  
VOLUME ["/etc/geoserver", "/var/log/geoserver"]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["catalina.sh", "run"]  

