# Molgenis Installation  
#  
# VERSION 0.0.2  
#  
FROM tomcat:7.0-jre8-alpine  
  
RUN apk --no-cache add openssl \  
&& wget -O molgenis-app-3.0.1.war
http://search.maven.org/remotecontent?filepath=org/molgenis/molgenis-
app/3.0.1/molgenis-app-3.0.1.war  
  
RUN rm -r $CATALINA_HOME/webapps/ROOT \  
&& rm -r $CATALINA_HOME/webapps/docs \  
&& rm -r $CATALINA_HOME/webapps/examples \  
&& mv molgenis-app-3.0.1.war $CATALINA_HOME/webapps/ROOT.war \  
&& echo 'CATALINA_OPTS="-Xmx2g -XX:+UseConcMarkSweepGC
-XX:+CMSClassUnloadingEnabled -Dmolgenis.home=/opt/molgenis/"' >
$CATALINA_HOME/bin/setenv.sh  
  
RUN mkdir -p /opt/molgenis \  
&& if ! test -f /opt/molgenis/molgenis-server.properties; then echo -e
"db_user=molgenis\ndb_password=molgenis\ndb_uri=jdbc\:postgresql\://molgenis-
db/molgenis?reWriteBatchedInserts\=true&autosave\=CONSERVATIVE\nadmin.password=admin"
> /opt/molgenis/molgenis-server.properties; fi  
  
VOLUME /opt/molgenis  
  
CMD ["catalina.sh", "run"]

