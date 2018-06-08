FROM tomcat:9.0.0-jre8-alpine  
  
ENV GS_VERSION_MAJOR 2.11  
ENV GS_VERSION_PATCH 2  
ENV GEOSERVER_DATA_DIR /opt/geoserver/data_dir  
  
RUN mkdir -p $GEOSERVER_DATA_DIR && \  
mkdir -p $CATALINA_HOME/webapps/geoserver  
  
WORKDIR /tmp  
  
RUN apk add --no-cache unzip \  
openssl \  
tar && \  
# get geoserver and jai libraries from the web  
wget -q
http://sourceforge.net/projects/geoserver/files/GeoServer/${GS_VERSION_MAJOR}.${GS_VERSION_PATCH}/geoserver-${GS_VERSION_MAJOR}.${GS_VERSION_PATCH}-war.zip
-O geoserver.zip && \  
wget -q http://download.java.net/media/jai/builds/release/1_1_3/jai-1_1_3-lib-
linux-amd64.tar.gz && \  
wget -q http://download.java.net/media/jai-
imageio/builds/release/1.1/jai_imageio-1_1-lib-linux-amd64.tar.gz && \  
# get the GeoServer Active Clustering Extension  
# http://geoserver.geo-
solutions.it/edu/en/clustering/clustering/active/installation.html  
wget -q
http://ares.boundlessgeo.com/geoserver/${GS_VERSION_MAJOR}.x/community-
latest/geoserver-${GS_VERSION_MAJOR}-SNAPSHOT-jms-cluster-plugin.zip  
  
# unpack jai libraries and move to $JAVA_HOME folders  
RUN tar -xvzf jai-1_1_3-lib-linux-amd64.tar.gz && \  
tar -xvzf jai_imageio-1_1-lib-linux-amd64.tar.gz && \  
  
mv /tmp/jai-1_1_3/lib/*.jar $JAVA_HOME/lib/ext/ && \  
mv /tmp/jai-1_1_3/lib/*.so $JAVA_HOME/lib/amd64/ && \  
mv /tmp/jai_imageio-1_1/lib/*.jar $JAVA_HOME/lib/ext/ && \  
mv /tmp/jai_imageio-1_1/lib/*.so $JAVA_HOME/lib/amd64/  
  
WORKDIR $CATALINA_HOME  
  
COPY startup.sh ./startup.sh  
  
# unzip and move geoserver files to tomcat webapps folder  
RUN unzip /tmp/geoserver.zip -d /tmp && \  
unzip /tmp/geoserver.war -d $CATALINA_HOME/webapps/geoserver/ && \  
unzip /tmp/geoserver-${GS_VERSION_MAJOR}-SNAPSHOT-jms-cluster-plugin.zip -d
$CATALINA_HOME/webapps/geoserver/WEB-INF/lib/ && \  
chmod +x ./startup.sh  
  
#some cleanup of files and apk packages  
RUN rm -rf $CATALINA_HOME/webapps/ROOT && \  
rm -rf $CATALINA_HOME/webapps/docs && \  
rm -rf $CATALINA_HOME/webapps/examples && \  
rm -rf $CATALINA_HOME/webapps/host-manager && \  
rm -rf $CATALINA_HOME/webapps/manager && \  
rm -rf /tmp && \  
apk del --no-cache unzip tar  
  
EXPOSE 8080 9545  
  
CMD ["./startup.sh"]

