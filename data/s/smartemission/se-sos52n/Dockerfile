FROM 52north/sos:4.3.7  
# see https://github.com/52North/docker-images  
LABEL maintainer="Gerwin Hulsteijn, Just van den Broecke"  
  
ENV TZ Europe/Amsterdam  
ENV SOS_WEBAPP_DIR $CATALINA_HOME/webapps/sos52n  
ENV SOS_WEBAPP_WAR $CATALINA_HOME/webapps/sos52n.war  
  
# Remove unneccesary standard Tomcat Webapps and install required libs  
# for initializing config and sqlite config DB. Rename webapp  
# and unzip .war for convenience.  
# (SOS .war is originally installed at: $CATALINA_HOME/webapps/52n-sos-
webapp.war).  
RUN \  
rm -rf $CATALINA_HOME/webapps/ROOT \  
&& rm -rf $CATALINA_HOME/webapps/docs \  
&& rm -rf $CATALINA_HOME/webapps/examples \  
&& rm -rf $CATALINA_HOME/webapps/host-manager \  
&& rm -rf $CATALINA_HOME/webapps/manager \  
&& mv $CATALINA_HOME/webapps/52n-sos-webapp.war $SOS_WEBAPP_WAR \  
&& unzip $SOS_WEBAPP_WAR -d $SOS_WEBAPP_DIR \  
&& rm -rf $SOS_WEBAPP_WAR \  
&& apt-get update \  
&& apt-get -y install gettext-base sqlite3 libsqlite3-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /opt/sos52n  
  
COPY data/datasource.properties /opt/sos52n/datasource.properties  
COPY data/configuration.db /opt/sos52n//configuration.db  
COPY data/logback.xml $SOS_WEBAPP_DIR/WEB-INF/classes/logback.xml  
COPY data/timeseries-api_v1_beans.xml $SOS_WEBAPP_DIR/WEB-
INF/spring/timeseries-api_v1_beans.xml  
COPY data/jsclient.json $SOS_WEBAPP_DIR/static/client/jsClient/settings.json  
  
COPY entry.sh /entry.sh  
RUN chmod +x /entry.sh  
  
CMD /entry.sh

