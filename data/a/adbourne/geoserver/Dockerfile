FROM tomcat:8.5-jre8-alpine  
MAINTAINER Aaron Bourne <contact@aaronbourne.co.uk>  
  
ENV GEOSERVER_VERSION="2.11.4" \  
GEOSERVER_DATA_DIR="/geoserver_data"  
# Set data dir so it can be picked up by tomcat (seperate ENV as to use the
previously set GEOSERVER_DATA_DIR)  
ENV CATALINA_OPTS="${CATALINA_OPTS}
-DGEOSERVER_DATA_DIR=${GEOSERVER_DATA_DIR}"  
# Put the custom web.xml in place  
COPY resources/web.xml "${CATALINA_HOME}/conf/web.xml"  
# Download and install geoserver  
RUN apk update \  
# Add certs to allow wget to download over TLS  
&& apk add ca-certificates \  
&& update-ca-certificates \  
&& apk add openssl \  
# Clean up tomcat webapps dir  
&& rm -rf ${CATALINA_HOME}/webapps/* \  
# Download Geoserver  
&& wget -O "${CATALINA_HOME}/webapps/geoserver.war.zip"
"http://sourceforge.net/projects/geoserver/files/GeoServer/${GEOSERVER_VERSION}/geoserver-${GEOSERVER_VERSION}-war.zip"
\  
# Unpackage the zip  
&& unzip "${CATALINA_HOME}/webapps/geoserver.war.zip" -d
"${CATALINA_HOME}/webapps" \  
&& rm "${CATALINA_HOME}/webapps/geoserver.war.zip" \  
# Unpackage the war  
&& mkdir "${CATALINA_HOME}/webapps/geoserver" \  
&& unzip "${CATALINA_HOME}/webapps/geoserver.war" -d
"${CATALINA_HOME}/webapps/geoserver" \  
&& rm "${CATALINA_HOME}/webapps/geoserver.war" \  
# Create the data dir  
&& mkdir -p "${GEOSERVER_DATA_DIR}" \  
# Cleanup apk temp files  
&& rm -rf /var/cache/apk/*  

