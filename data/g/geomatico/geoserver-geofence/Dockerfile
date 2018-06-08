FROM oscarfonts/geoserver:2.11.0  
  
MAINTAINER Víctor González <victor.gonzalez@geomati.co>  
  
ENV MAJOR_VERSION 2.11  
  
WORKDIR /usr/local/tomcat/webapps/  
  
# Install Geofence webapp  
RUN wget http://ares.boundlessgeo.com/geofence/3.2.x/release-v3.2.2-geofence-
war.zip \  
&& unzip release-v3.2.2-geofence-war.zip \  
&& rm release-v3.2.2-geofence-war.zip \  
&& unzip -d geofence geofence.war  
  
# Install Geofence extension in GeoServer  
RUN wget http://ares.boundlessgeo.com/geoserver/${MAJOR_VERSION}.x/community-
latest/geoserver-${MAJOR_VERSION}-SNAPSHOT-geofence-plugin.zip \  
&& unzip -d ${GEOSERVER_INSTALL_DIR}/WEB-INF/lib
geoserver-${MAJOR_VERSION}-SNAPSHOT-geofence-plugin.zip \  
&& rm geoserver-${MAJOR_VERSION}-SNAPSHOT-geofence-plugin.zip  
  
# Use PostGIS as backend  
RUN rm geofence/WEB-INF/lib/hibernate-spatial-h2-geodb-1.1.1.jar \  
&& cp geofence/WEB-INF/spatial-lib/hibernate-spatial-postgis-1.1.1.jar
geofence/WEB-INF/lib/  
# Remove datasource settings from classpath because it takes precedence over
the -Dgeofence-ovr property  
RUN rm geofence/WEB-INF/classes/geofence-datasource-ovr.properties  
  
# Configure datasource settings file in GeoServer data dir  
ENV CATALINA_OPTS "${CATALINA_OPTS} -Dgeofence-
ovr=file:${GEOSERVER_DATA_DIR}/geofence-ovr.properties  
  

