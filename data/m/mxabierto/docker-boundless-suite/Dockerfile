FROM tomcat:8.0-jre8  
  
# GET FILES  
RUN wget -q https://github.com/mxabierto/boundless-
suite/releases/download/4.9.1/BoundlessSuite-4.9.1-war.zip -O boundless.zip \  
&& wget -q https://github.com/mxabierto/boundless-
suite/releases/download/4.9.1/BoundlessSuite-4.9.1-ext.zip -O boundless-
ext.zip  
  
# UPDATE AND INSTALL DEPENDENCIES  
RUN apt-get -y update \  
&& apt-get -y install git  
  
# CLONE REPO  
RUN git clone https://github.com/mxabierto/docker-boundless-suite suite  
  
# UNZIP FILES  
RUN unzip boundless.zip && unzip boundless-ext.zip  
  
# SETUP  
ENV GEOSERVER_DEFAULT_DATA_DIR
/var/opt/boundless/server/geoserver/default_data  
ENV GEOSERVER_DATA_DIR $GEOSERVER_DEFAULT_DATA_DIR  
ENV GEOWEBCACHE_CACHE_DIR /var/opt/boundless/server/geowebcache/tilecache  
ENV GEOWEBCACHE_CONFIG_DIR /var/opt/boundless/server/geowebcache/config  
  
# CREATE DATA DIRECTORIES  
RUN mkdir -p $GEOWEBCACHE_CACHE_DIR \  
&& mkdir -p $GEOWEBCACHE_CONFIG_DIR \  
&& mkdir -p $GEOSERVER_DEFAULT_DATA_DIR  
  
# ---------------------------------------------- DEPLOY GEOSERVER  
## SETUP DEFAULT DATA DIR  
RUN unzip BoundlessSuite-latest-war/suite-data-dir.zip -d
$GEOSERVER_DEFAULT_DATA_DIR  
  
## DEPLOY  
RUN unzip BoundlessSuite-latest-war/geoserver.war -d
$CATALINA_HOME/webapps/geoserver  
  
## EXTENSIONS  
### maril render  
RUN cp BoundlessSuite-latest-ext/marlin/* $CATALINA_HOME/lib  
### libjpeg-turbo  
RUN wget -q https://svwh.dl.sourceforge.net/project/libjpeg-
turbo/1.5.3/libjpeg-turbo-official_1.5.3_amd64.deb -O libjpeg-turbo.deb \  
&& dpkg -i libjpeg-turbo.deb  
  
### gdal  
RUN apt-get install -y gdal-bin libgdal-java \  
&& cp /usr/share/java/gdal.jar $CATALINA_HOME/webapps/geoserver/WEB-INF/lib \  
&& cp BoundlessSuite-latest-ext/gdal/* $CATALINA_HOME/webapps/geoserver/WEB-
INF/lib \  
&& echo "GDAL_DATA=/usr/share/gdal" >> $CATALINA_HOME/conf/catalina.properties  
  
### netcdf  
RUN cp BoundlessSuite-latest-ext/netcdf-out/*
$CATALINA_HOME/webapps/geoserver/WEB-INF/lib \  
&& apt-get install -y netcdf-bin  
  
### csw  
RUN cp BoundlessSuite-latest-ext/csw/* $CATALINA_HOME/webapps/geoserver/WEB-
INF/lib/  
### css  
RUN wget -q
https://cytranet.dl.sourceforge.net/project/geoserver/GeoServer/2.12.0/extensions/geoserver-2.12.0-css-
plugin.zip -O geoserver-css.zip \  
&& unzip geoserver-css.zip -d $CATALINA_HOME/webapps/geoserver/WEB-INF/lib/  
# ---------------------------------------------- DEPLOY GEOWEBCACHE  
RUN cp BoundlessSuite-latest-war/geowebcache.war $CATALINA_HOME/webapps  
  
# ---------------------------------------------- DEPLOY COMPOSER  
RUN cp BoundlessSuite-latest-war/composer.war $CATALINA_HOME/webapps  
  
# ---------------------------------------------- DEPLOY DOCUMENTATION  
RUN cp BoundlessSuite-latest-war/suite-docs.war $CATALINA_HOME/webapps  
  
# ---------------------------------------------- DEPLOY QUICKVIEW  
RUN cp BoundlessSuite-latest-war/quickview.war $CATALINA_HOME/webapps  
  
# REMOVE APACHE ADMIN  
RUN rm -rf webapps/ROOT/* \  
&& cp suite/index.jsp webapps/ROOT/  
  
EXPOSE 8080  

