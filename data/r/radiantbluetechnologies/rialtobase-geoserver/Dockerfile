# radiantbluetechnologies/rialtobase-geoserver  
FROM radiantbluetechnologies/rialtobase-tomcat  
MAINTAINER mpg@flaxen.com  
  
EXPOSE 8080  
ENV GEOSERVER_HOME /opt/geoserver  
  
# They don't seem to release specific versions of the community plugins,  
# they just have the "latest" ones: we want to avoid JAR Hell by pinning down  
# the version that works and avoid JAR Hell.  
# This file was taken from:  
#
http://ares.boundlessgeo.com/geoserver/2.7.x/community-2015-07-24/geoserver-2.7-SNAPSHOT-
python-plugin.zip  
COPY geoserver-python.zip /tmp/geoserver-python.zip  
  
COPY build.sh /tmp/build.sh  
RUN /tmp/build.sh  
  
CMD "/opt/geoserver/bin/startup.sh"  

