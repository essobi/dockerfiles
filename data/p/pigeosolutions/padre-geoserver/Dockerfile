FROM tomcat:8-jre8  
MAINTAINER Jean Pommier "jp@pi-geosolutions.fr"  
#modified from camp2camp Dockerfile https://github.com/camptocamp/docker-
geoserver  
# Install Java JAI libraries  
RUN cd /tmp && \  
curl -L http://download.java.net/media/jai/builds/release/1_1_3/jai-1_1_3-lib-
linux-amd64.tar.gz | tar xfz \- && \  
curl -L http://download.java.net/media/jai-
imageio/builds/release/1.1/jai_imageio-1_1-lib-linux-amd64.tar.gz | tar xfz \-
&& \  
mv /tmp/jai*/lib/*.jar $JAVA_HOME/lib/ext/ && \  
mv /tmp/jai*/lib/*.so $JAVA_HOME/lib/amd64/ && \  
rm -r /tmp/*  
  
ENV REPO https://build.geoserver.org/geoserver  
ENV GEOSERVER_VERSION 2.12  
ENV GEOSERVER_VERSION_NAME ${GEOSERVER_VERSION}.x  
  
# Install geoserver  
RUN curl -L
${REPO}/${GEOSERVER_VERSION_NAME}/geoserver-${GEOSERVER_VERSION_NAME}-latest-
war.zip > /tmp/geoserver.zip && \  
unzip /tmp/geoserver.zip -d /tmp/geoserver && \  
rm -rf ${CATALINA_HOME}/webapps/* && \  
unzip /tmp/geoserver/geoserver.war -d $CATALINA_HOME/webapps/geoserver && \  
(cd $CATALINA_HOME/webapps/geoserver/WEB-INF/lib; rm jai_core-*jar
jai_imageio-*.jar jai_codec-*.jar) && \  
rm -r /tmp/*  
  
# Install plugins (WPS)  
RUN curl -L ${REPO}/${GEOSERVER_VERSION_NAME}/ext-
latest/geoserver-${GEOSERVER_VERSION}-SNAPSHOT-wps-plugin.zip >
/tmp/geoserver-wps-plugin.zip && \  
unzip -o /tmp/geoserver-wps-plugin.zip -d
$CATALINA_HOME/webapps/geoserver/WEB-INF/lib/ && \  
rm /tmp/*  
  
# Install plugins (pyramid)  
RUN curl -L ${REPO}/${GEOSERVER_VERSION_NAME}/ext-
latest/geoserver-${GEOSERVER_VERSION}-SNAPSHOT-pyramid-plugin.zip >
/tmp/geoserver-pyramid-plugin.zip && \  
unzip -o /tmp/geoserver-pyramid-plugin.zip -d
$CATALINA_HOME/webapps/geoserver/WEB-INF/lib/ && \  
rm /tmp/*  
  
# Install plugins (CSS)  
RUN curl -L ${REPO}/${GEOSERVER_VERSION_NAME}/ext-
latest/geoserver-${GEOSERVER_VERSION}-SNAPSHOT-css-plugin.zip >
/tmp/geoserver-css-plugin.zip && \  
unzip -o /tmp/geoserver-css-plugin.zip -d
$CATALINA_HOME/webapps/geoserver/WEB-INF/lib/ && \  
rm /tmp/*  
  
# Install plugins (charts)  
RUN curl -L ${REPO}/${GEOSERVER_VERSION_NAME}/ext-
latest/geoserver-${GEOSERVER_VERSION}-SNAPSHOT-charts-plugin.zip >
/tmp/geoserver-charts-plugin.zip && \  
unzip -o /tmp/geoserver-charts-plugin.zip -d
$CATALINA_HOME/webapps/geoserver/WEB-INF/lib/ && \  
rm /tmp/*  
  
# Install plugins (grib)  
RUN curl -L ${REPO}/${GEOSERVER_VERSION_NAME}/ext-
latest/geoserver-${GEOSERVER_VERSION}-SNAPSHOT-grib-plugin.zip >
/tmp/geoserver-grib-plugin.zip && \  
unzip -o /tmp/geoserver-grib-plugin.zip -d
$CATALINA_HOME/webapps/geoserver/WEB-INF/lib/ && \  
rm /tmp/*  
  
# Install plugins (netCDF)  
RUN curl -L ${REPO}/${GEOSERVER_VERSION_NAME}/ext-
latest/geoserver-${GEOSERVER_VERSION}-SNAPSHOT-netcdf-plugin.zip >
/tmp/geoserver-netcdf-plugin.zip && \  
unzip -o /tmp/geoserver-netcdf-plugin.zip -d
$CATALINA_HOME/webapps/geoserver/WEB-INF/lib/ && \  
rm /tmp/*  
  
# Install plugins (DDS/BIL -- Community plugin for WorldWind)  
RUN curl -L ${REPO}/${GEOSERVER_VERSION_NAME}/community-
latest/geoserver-${GEOSERVER_VERSION}-SNAPSHOT-dds-plugin.zip >
/tmp/geoserver-dds-plugin.zip && \  
unzip -o /tmp/geoserver-dds-plugin.zip -d
$CATALINA_HOME/webapps/geoserver/WEB-INF/lib/ && \  
rm /tmp/*  
  
# Instal Marlin  
#RUN cd /usr/local/tomcat/lib && wget https://github.com/bourgesl/marlin-
renderer/releases/download/v0.7.4_2/marlin-0.7.4-Unsafe.jar && \  
# wget https://github.com/bourgesl/marlin-
renderer/releases/download/v0.7.4_2/marlin-0.7.4-Unsafe-sun-java2d.jar  
#ENV CATALINA_OPTS
"-Xbootclasspath/a:/usr/local/tomcat/lib/marlin-0.7.4-Unsafe.jar
-Xbootclasspath/p:/usr/local/tomcat/lib/marlin-0.7.4-Unsafe-sun-java2d.jar
-Dsun.java2d.renderer=org.marlin.pisces.PiscesRenderingEngine
-Duser.timezone=GMT -Dorg.geotools.shapefile.datetime=true"  
ENV CATALINA_OPTS "-Duser.timezone=GMT -Dorg.geotools.shapefile.datetime=true"  

