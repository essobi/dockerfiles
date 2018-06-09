FROM jetty:9-jre8  
  
ENV JETTY_WEBAPPS $JETTY_BASE/webapps  
ENV DIGILIB_VERSION_MAJOR 2.3  
ENV DIGILIB_VERSION_MINOR 2.3.6  
ENV DIGILIB_VERSION_URL
http://sourceforge.net/projects/digilib/files/releases/$DIGILIB_VERSION_MAJOR/digilib-
webapp-$DIGILIB_VERSION_MINOR-srv3.war  
#this would get latest version from  
#RUN wget --no-verbose -O tmp.war $DIGILIB_VERSION_URL && unzip -q tmp.war -d
"$JETTY_WEBAPPS"/ROOT/ && rm tmp.war  
  
ADD digilib-webapp-2.3-SNAPSHOT-srv3.war tmp.war  
RUN unzip -q tmp.war -d "$JETTY_WEBAPPS"/ROOT/ && rm tmp.war  
  
ADD jetty.xml $JETTY_BASE/etc/jetty.xml  
  
VOLUME ["/var/lib/jetty/webapps/ROOT/sample-images"]  
  
EXPOSE 8080  

