FROM tomcat:7-jre7  
  
ADD
http://downloads.sourceforge.net/project/geoserver/GeoServer/2.1.1/geoserver-2.1.1-war.zip
/tmp  
ADD http://download.java.net/media/jai/builds/release/1_1_3/jai-1_1_3-lib-
linux-amd64.tar.gz /tmp  
ADD http://download.java.net/media/jai-
imageio/builds/release/1.1/jai_imageio-1_1-lib-linux-amd64.tar.gz /tmp  
#ADD geoserver-*-war.zip jai-*-lib-linux-amd64.tar.gz jai_imageio-*-lib-linux-
amd64.tar.gz /tmp/  
  
RUN tar xf /tmp/jai-*.tar.gz -C /tmp && \  
tar xf /tmp/jai_imageio-*.tar.gz -C /tmp && \  
mv /tmp/jai-*/lib/*.so /tmp/jai_imageio-*/lib/*.so $JAVA_HOME/lib/amd64/ && \  
mv /tmp/jai-*/lib/*.jar /tmp/jai_imageio-*/lib/*.jar $JAVA_HOME/lib/ext/ && \  
rm -r /tmp/jai_imageio-* /tmp/jai-* && \  
unzip /tmp/geoserver-*-war.zip geoserver.war -d /tmp && \  
rm /tmp/geoserver-*-war.zip && \  
mv /tmp/geoserver.war /tmp/geoserver.zip && \  
unzip /tmp/geoserver.zip -d $CATALINA_HOME/webapps/geoserver && \  
rm $CATALINA_HOME/webapps/geoserver/WEB-INF/lib/jai_codec-*.jar \  
$CATALINA_HOME/webapps/geoserver/WEB-INF/lib/jai_core-*.jar \  
$CATALINA_HOME/webapps/geoserver/WEB-INF/lib/jai_imageio-*.jar && \  
mkdir -p /data && \  
mv $CATALINA_HOME/webapps/geoserver/data /data/geoserver && \  
ln -s /data/geoserver $CATALINA_HOME/webapps/geoserver/data && \  
rm /tmp/geoserver.zip  
  
VOLUME /data/geoserver

