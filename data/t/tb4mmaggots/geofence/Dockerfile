#Compatible with GeoServer 2.11.x and up  
FROM tomcat:8.5-alpine  
  
ARG
GF_DOWNLOAD_URL=http://ares.boundlessgeo.com/geofence/3.3.x/release-v3.3.0-geofence-
war.zip  
  
RUN apk update && apk upgrade && apk add --no-cache $(apk search -q ttf- |
grep -v '\\-doc')  
  
RUN wget -c $GF_DOWNLOAD_URL -O /tmp/geofence.zip \  
&& unzip /tmp/geofence.zip -d /tmp/ \  
&& mkdir /usr/local/tomcat/webapps/geofence \  
&& unzip /tmp/geofence.war -d /usr/local/tomcat/webapps/geofence \  
&& rm -f /usr/local/tomcat/webapps/geofence/WEB-INF/lib/hibernate-
spatial-h2-geodb-1.1.1.jar \  
&& mv /usr/local/tomcat/webapps/geofence/WEB-INF/spatial-lib/hibernate-
spatial-postgis-1.1.1.jar /usr/local/tomcat/webapps/geofence/WEB-INF/lib/ \  
&& rm -rf /tmp/*  

