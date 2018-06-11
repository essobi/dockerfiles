FROM ubuntu:trusty  
MAINTAINER winsent<pipetc@gmail.com>  
# ECW support https://github.com/daiko/docker-mapserver-ecw  
MAINTAINER Florestan Bredow <florestan.bredow@daiko.fr>  
MAINTAINER Amandine Sahl <amandine.sahl@gmail.com>  
  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV GDAL_PATH /usr/share/gdal  
ENV GEOSERVER_HOME /opt/geoserver  
ENV JAVA_HOME /usr  
ENV GDAL_DATA $GDAL_PATH/1.10  
ENV PATH $GDAL_PATH:$PATH  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/lib/jni:/usr/share/java  
  
RUN export DEBIAN_FRONTEND=noninteractive  
RUN dpkg-divert --local --rename --add /sbin/initctl  
  
# Install packages  
RUN \  
apt-get -y update --fix-missing && \  
apt-get -y install unzip build-essential software-properties-common && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get -y update && \  
apt-get install -y oracle-java8-installer gdal-bin libgdal-dev libgdal-java &&
\  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
rm -rf /tmp/* /var/tmp/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Get native JAI and ImageIO  
RUN \  
cd $JAVA_HOME && \  
wget http://data.boundlessgeo.com/suite/jai/jai-1_1_3-lib-linux-amd64-jdk.bin
&& \  
echo "yes" | sh jai-1_1_3-lib-linux-amd64-jdk.bin && \  
rm jai-1_1_3-lib-linux-amd64-jdk.bin  
  
RUN \  
cd $JAVA_HOME && \  
export _POSIX2_VERSION=199209 &&\  
wget http://data.opengeo.org/suite/jai/jai_imageio-1_1-lib-linux-amd64-jdk.bin
&& \  
echo "yes" | sh jai_imageio-1_1-lib-linux-amd64-jdk.bin && \  
rm jai_imageio-1_1-lib-linux-amd64-jdk.bin  
# ECW support from here https://github.com/daiko/docker-mapserver-ecw  
  
COPY libs/erdas /usr/local/erdas  
RUN ln -s "/usr/local/erdas/lib/x64/release/libNCSEcw.so"
"/usr/local/lib/libNCSEcw.so" \  
&& ldconfig  
  
COPY libs/gdal-ecw/libgdal-ecw-1.10.0.tar.gz /usr/src/  
COPY libs/gdal-ecw/gdal-ecw-build /usr/bin/  
RUN gdal-ecw-build "/usr/local/erdas"  
#  
# GEOSERVER INSTALLATION  
#  
ENV GEOSERVER_VERSION 2.11.0  
# Get GeoServer  
RUN wget -c
http://downloads.sourceforge.net/project/geoserver/GeoServer/$GEOSERVER_VERSION/geoserver-$GEOSERVER_VERSION-
bin.zip -O ~/geoserver.zip &&\  
unzip ~/geoserver.zip -d /opt && mv -v /opt/geoserver* /opt/geoserver && \  
rm ~/geoserver.zip  
  
# Get OGR plugin  
RUN wget -c
http://downloads.sourceforge.net/project/geoserver/GeoServer/$GEOSERVER_VERSION/extensions/geoserver-$GEOSERVER_VERSION-
ogr-wfs-plugin.zip -O ~/geoserver-ogr-plugin.zip &&\  
unzip -o ~/geoserver-ogr-plugin.zip -d /opt/geoserver/webapps/geoserver/WEB-
INF/lib/ && \  
rm ~/geoserver-ogr-plugin.zip  
  
# Get GDAL plugin  
RUN wget -c
http://downloads.sourceforge.net/project/geoserver/GeoServer/$GEOSERVER_VERSION/extensions/geoserver-$GEOSERVER_VERSION-
gdal-plugin.zip -O ~/geoserver-gdal-plugin.zip &&\  
unzip -o ~/geoserver-gdal-plugin.zip -d /opt/geoserver/webapps/geoserver/WEB-
INF/lib/ && \  
rm ~/geoserver-gdal-plugin.zip  
  
# Get printing plugin  
RUN wget -c
http://downloads.sourceforge.net/project/geoserver/GeoServer/$GEOSERVER_VERSION/extensions/geoserver-$GEOSERVER_VERSION-
printing-plugin.zip -O ~/geoserver-printing-plugin.zip &&\  
unzip ~/geoserver-printing-plugin.zip -d /opt/geoserver/webapps/geoserver/WEB-
INF/lib/ && \  
rm ~/geoserver-printing-plugin.zip  
  
# Get import plugin  
RUN wget -c
http://downloads.sourceforge.net/project/geoserver/GeoServer/$GEOSERVER_VERSION/extensions/geoserver-$GEOSERVER_VERSION-
importer-plugin.zip -O ~/geoserver-importer-plugin.zip &&\  
unzip -o ~/geoserver-importer-plugin.zip -d
/opt/geoserver/webapps/geoserver/WEB-INF/lib/ && \  
rm ~/geoserver-importer-plugin.zip  
  
# Replace GDAL Java bindings  
RUN rm -rf $GEOSERVER_HOME/webapps/geoserver/WEB-INF/lib/imageio-ext-gdal-
bindings-1.9.2.jar  
RUN cp /usr/share/java/gdal.jar $GEOSERVER_HOME/webapps/geoserver/WEB-
INF/lib/gdal.jar  
# Remove old JAI from geoserver  
RUN rm -rf $GEOSERVER_HOME/webapps/geoserver/WEB-INF/lib/jai_codec-1.1.3.jar
&& \  
rm -rf $GEOSERVER_HOME/webapps/geoserver/WEB-INF/lib/jai_core-1.1.3.jar && \  
rm -rf $GEOSERVER_HOME/webapps/geoserver/WEB-INF/lib/jai_imageio-1.1.jar  
# Expose GeoServer's default port  
EXPOSE 8080  
CMD ["/opt/geoserver/bin/startup.sh"]  

