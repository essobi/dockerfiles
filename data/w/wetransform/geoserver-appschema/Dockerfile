#--------- Generic stuff
--------------------------------------------------------------------  
FROM tomcat:8-jre8  
MAINTAINER Simon Templer <simon@wetransform.to>  
  
RUN apt-get -y update  
  
#-------------Application Specific Stuff
----------------------------------------------------  
RUN apt-get -y install unzip groovy2  
  
ADD resources /tmp/resources  
  
ENV GEOSERVER_VERSION 2.13.0  
ENV GEOSERVER_DIR /opt/webapps/geoserver  
ENV TOMCAT_DIR /usr/local/tomcat  
  
# Fetch the geoserver zip file if it is not available locally in the resources
dir  
RUN if [ ! -f /tmp/resources/geoserver.zip ]; then \  
wget -c
https://sourceforge.net/projects/geoserver/files/GeoServer/${GEOSERVER_VERSION}/geoserver-${GEOSERVER_VERSION}-war.zip/download
-O /tmp/resources/geoserver.zip; \  
fi; \  
mkdir /tmp/resources/geoserver && cd /tmp/resources/geoserver && unzip
../geoserver.zip; \  
mkdir /opt/webapps && mv -v geoserver.war /opt/webapps && mkdir
${GEOSERVER_DIR} && cd ${GEOSERVER_DIR} && unzip ../geoserver.war; \  
rm -rf /tmp/resources/geoserver;  
  
# Fetch the geoserver app-schema plugin zip file if it is not available
locally in the resources dir  
RUN if [ ! -f /tmp/resources/app-schema-plugin.zip ]; then \  
wget -c
https://sourceforge.net/projects/geoserver/files/GeoServer/${GEOSERVER_VERSION}/extensions/geoserver-${GEOSERVER_VERSION}-app-
schema-plugin.zip/download -O /tmp/resources/app-schema-plugin.zip; \  
fi; \  
mkdir /tmp/resources/app-schema && cd /tmp/resources/app-schema && unzip
../app-schema-plugin.zip; \  
mv -v *.jar ${GEOSERVER_DIR}/WEB-INF/lib; \  
rm -rf /tmp/resources/app-schema;  
  
# delete default workspaces  
RUN rm -rf ${GEOSERVER_DIR}/data/workspaces && mkdir
${GEOSERVER_DIR}/data/workspaces; \  
rm -rf ${GEOSERVER_DIR}/data/layergroups/*  
  
COPY ./ROOT.xml ${TOMCAT_DIR}/conf/Catalina/localhost/ROOT.xml  
  
ADD scripts /tmp/scripts  
RUN chmod -R a+x /tmp/scripts  
  
# Run setup script to apply initial settings  
RUN /tmp/scripts/setup.groovy ${GEOSERVER_DIR}  
  
EXPOSE 8080  
CMD ["/tmp/scripts/launch.sh"]  

