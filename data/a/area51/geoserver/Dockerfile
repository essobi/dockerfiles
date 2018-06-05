ARG GEOSERVER_VERSION  
  
FROM area51/java:serverjre-8  
ARG GEOSERVER_VERSION  
MAINTAINER Peter Mount <peter@retep.org>  
  
#ENV GEOSERVER_VERSION 2.12.0  
ENV GEOSERVER_HOME /opt/geoserver  
ENV GEOSERVER_DATA_DIR /opt/data  
  
COPY index.html /tmp  
COPY docker-entrypoint.sh /  
  
WORKDIR /opt  
RUN echo Retrieving geoserver $GEOSERVER_VERSION &&\  
curl -s -o /tmp/geoserver.zip \  
https://cdn.area51.onl/tools/geoserver/geoserver-${GEOSERVER_VERSION}-bin.zip
&&\  
\  
echo Installing &&\  
unzip -q /tmp/geoserver.zip &&\  
rm -f /tmp/geoserver.zip &&\  
mv geoserver-$GEOSERVER_VERSION $GEOSERVER_HOME &&\  
\  
echo Configuring root &&\  
mkdir -p $GEOSERVER_HOME/webapps/ROOT &&\  
mv /tmp/index.html $GEOSERVER_HOME/webapps/ROOT &&\  
\  
mkdir -p $GEOSERVER_DATA_DIR &&\  
chmod +x /docker-entrypoint.sh  
  
WORKDIR $GEOSERVER_HOME/bin  
VOLUME $GEOSERVER_DATA_DIR  
  
CMD ["/docker-entrypoint.sh"]  

