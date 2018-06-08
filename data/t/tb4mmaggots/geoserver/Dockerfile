FROM tomcat:8.5-alpine  
  
ARG GS_VERSION=2.11.1  
  
RUN apk update && apk upgrade && apk add --no-cache $(apk search -q ttf- |
grep -v '\\-doc') ca-certificates openssl  
  
RUN export GS_MAJOR=$(echo ${GS_VERSION} | awk -F "." '{print $1"."$2}') \  
&& mkdir /tmp/geoserver /tmp/geoserver/plugins
$CATALINA_HOME/webapps/geoserver \  
&& wget -c
https://sourceforge.net/projects/geoserver/files/GeoServer/${GS_VERSION}/geoserver-${GS_VERSION}-war.zip
-O /tmp/geoserver/geoserver.zip \  
&& wget -c
https://sourceforge.net/projects/geoserver/files/GeoServer/${GS_VERSION}/extensions/geoserver-${GS_VERSION}-cas-
plugin.zip -O /tmp/geoserver/plugins/cas.zip \  
&& wget -c
https://sourceforge.net/projects/geoserver/files/GeoServer/${GS_VERSION}/extensions/geoserver-${GS_VERSION}-feature-
pregeneralized-plugin.zip -O /tmp/geoserver/plugins/feature-pregeneralized.zip
\  
&& wget -c
https://sourceforge.net/projects/geoserver/files/GeoServer/${GS_VERSION}/extensions/geoserver-${GS_VERSION}-imagemosaic-
jdbc-plugin.zip -O /tmp/geoserver/plugins/imagemosaic-jdbc.zip \  
&& wget -c
https://sourceforge.net/projects/geoserver/files/GeoServer/${GS_VERSION}/extensions/geoserver-${GS_VERSION}-monitor-
plugin.zip -O /tmp/geoserver/plugins/monitor.zip \  
&& wget -c
https://sourceforge.net/projects/geoserver/files/GeoServer/${GS_VERSION}/extensions/geoserver-${GS_VERSION}-mysql-
plugin.zip -O /tmp/geoserver/plugins/mysql.zip \  
&& wget -c
https://sourceforge.net/projects/geoserver/files/GeoServer/${GS_VERSION}/extensions/geoserver-${GS_VERSION}-pyramid-
plugin.zip -O /tmp/geoserver/plugins/pyramid.zip \  
&& wget -c
https://sourceforge.net/projects/geoserver/files/GeoServer/${GS_VERSION}/extensions/geoserver-${GS_VERSION}-wps-
plugin.zip -O /tmp/geoserver/plugins/wps.zip \  
&& wget -c http://ares.boundlessgeo.com/geoserver/$GS_MAJOR.x/community-
latest/geoserver-${GS_MAJOR}-SNAPSHOT-geofence-plugin.zip -O
/tmp/geoserver/plugins/geofence.zip \  
&& unzip /tmp/geoserver/geoserver.zip -d /tmp/geoserver \  
&& unzip /tmp/geoserver/geoserver.war -d $CATALINA_HOME/webapps/geoserver \  
&& find /tmp/geoserver/plugins/ -name "*.zip" | awk '{print "unzip "$1" -d
$CATALINA_HOME/webapps/geoserver/WEB-INF/lib/"}' | sh || true \  
&& rm -rf $CATALINA_HOME/webapps/geoserver/data \  
&& rm -rf /tmp/geoserver  

