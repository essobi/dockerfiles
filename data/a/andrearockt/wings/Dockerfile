FROM andrearockt/oodt  
  
MAINTAINER Andrea Fonti <andreafontict@gmail.com>  
  
USER root  
  
#================================Build
prerequisites===========================================#  
RUN apt-get update && apt-get install -y git xmlstarlet maven2 graphviz  
  
RUN adduser --disabled-password --gecos '' wings  
  
#================================Wings=========================================================#  
ENV WINGS_HOME /usr/local/wings  
RUN mkdir -p "$WINGS_HOME" && chown -R wings:wings $WINGS_HOME  
WORKDIR $WINGS_HOME  
  
USER wings  
  
RUN git clone https://github.com/IKCAP/wings  
  
#==================================Enable building of oodt
engine==============================#  
RUN xmlstarlet ed -L --subnode "/_:project/_:modules" \--type elem -n module
-v engines/oodt wings/pom.xml  
  
RUN xmlstarlet ed -L --subnode "/_:project//_:dependencies" -type elem -n
dependency wings/portal/pom.xml  
  
RUN xmlstarlet ed -L --subnode
"/_:project//_:dependencies/_:dependency[last()]" -type elem -n groupId -v
edu.isi.wings \  
\--subnode "/_:project//_:dependencies/_:dependency[last()]" -type elem -n
artifactId -v wings-oodt-adapter \  
\--subnode "/_:project//_:dependencies/_:dependency[last()]" -type elem -n
version -v '${project.parent.version}' wings/portal/pom.xml  
  
RUN xmlstarlet ed -L --subnode "/_:project//_:dependencies" -type elem -n
dependency wings/portal/pom.xml  
  
RUN xmlstarlet ed -L --subnode
"/_:project//_:dependencies/_:dependency[last()]" -type elem -n groupId -v
edu.isi.wings \  
\--subnode "/_:project//_:dependencies/_:dependency[last()]" -type elem -n
artifactId -v wings-oodt-wmservices \  
\--subnode "/_:project//_:dependencies/_:dependency[last()]" -type elem -n
version -v '${project.parent.version}' wings/portal/pom.xml  
  
RUN xmlstarlet ed -L -u "//_:oodt.version" -v "0.8"
wings/engines/oodt/adapter/pom.xml  
  
RUN xmlstarlet ed -L -u "//_:oodt.version" -v "0.8"
wings/engines/oodt/task/pom.xml  
  
RUN xmlstarlet ed -L -u "//_:oodt.version" -v "0.8"
wings/engines/oodt/wmservices/pom.xml  
  
RUN xmlstarlet ed -L -u "//Parameter[@name=\"workflow.url\"]/@value" -v
"http://localhost:9001" wings/engines/oodt/wmservices/src/main/webapp/META-
INF/context.xml  
  
RUN xmlstarlet ed -L -u "//Parameter[@name=\"packagedRepo.dir.path\"]/@value"
-v "/replaceme" wings/engines/oodt/wmservices/src/main/webapp/META-
INF/context.xml  
  
RUN rm $WINGS_HOME/wings/portal/src/main/resources/portal.properties  
  
#===================================Build
WINGS================================================#  
RUN cd wings; MAVEN_OPTS='-Dfile.encoding=UTF-8' mvn install  
  
#===================================Deploy
WINGS===============================================#  
USER root  
  
RUN cp $WINGS_HOME/wings/portal/target/wings-portal-*.war
$CATALINA_HOME/webapps/wings-portal.war && chown tomcat:tomcat
$CATALINA_HOME/webapps/wings-portal.war  
  
RUN cp $WINGS_HOME/wings/engines/oodt/wmservices/target/wings-oodt-
wmservices-*.war $CATALINA_HOME/webapps/wings-oodt-wmservices.war && chown
tomcat:tomcat $CATALINA_HOME/webapps/wings-oodt-wmservices.war  
  
USER tomcat  
  
RUN xmlstarlet ed -L --subnode "/tomcat-users" \--type elem -n user -v "" \  
\--subnode "/tomcat-users/user[last()]" \--type attr -n username -v admin \  
\--subnode "/tomcat-users/user[last()]" \--type attr -n password -v admin \  
\--subnode "/tomcat-users/user[last()]" \--type attr -n roles -v
"WingsUser,WingsAdmin" \  
$CATALINA_HOME/conf/tomcat-users.xml  
  
RUN xmlstarlet ed -L --subnode
"/Server/GlobalNamingResources/Resource[@name=\"UserDatabase\"]" -type attr -n
readonly -v false \  
$CATALINA_HOME/conf/server.xml  
  
USER root  
  
RUN cp $WINGS_HOME/wings/engines/oodt/task/target/wings-oodt-task-*.jar
$OODT_DIR/distribution/workflow/lib/ && chown oodt:oodt
$OODT_DIR/distribution/workflow/lib/wings-oodt-task-*.jar  
RUN cp $OODT_DIR/distribution/filemgr/lib/cas-filemgr-*.jar
$OODT_DIR/distribution/workflow/lib && chown oodt:oodt
$OODT_DIR/distribution/workflow/lib/cas-filemgr-*.jar  
  
RUN mkdir -p /home/tomcat/.wings  
  
COPY portal.properties /home/tomcat/.wings/portal.properties  
  
RUN chown -R tomcat:tomcat /home/tomcat/  
  
RUN cp $WINGS_HOME/wings/engines/oodt/wmservices/src/main/webapp/META-
INF/context.xml $CATALINA_HOME/conf/Catalina/localhost/wings-oodt-
wmservices.xml && chown tomcat:tomcat
$CATALINA_HOME/conf/Catalina/localhost/wings-oodt-wmservices.xml  
  
RUN cd $CATALINA_HOME/ && wget
http://search.maven.org/remotecontent?filepath=org/apache/oodt/cas-
curator/0.8/cas-curator-0.8.war -O cas-curator.war && chown tomcat:tomcat cas-
curator.war && mv cas-curator.war webapps/  
  
RUN xmlstarlet ed -L -u "//Parameter[@name=\"workflow.url\"]/@value" -v
"http://localhost:9001" $CATALINA_HOME/conf/Catalina/localhost/wings-oodt-
wmservices.xml  
RUN xmlstarlet ed -L -u "//Parameter[@name=\"workflow.url\"]/@override" -v
"true" $CATALINA_HOME/conf/Catalina/localhost/wings-oodt-wmservices.xml  
  
RUN xmlstarlet ed -L -u "//Parameter[@name=\"packagedRepo.dir.path\"]/@value"
-v "/usr/local/oodt/distribution/workflow/policy/wengine"
$CATALINA_HOME/conf/Catalina/localhost/wings-oodt-wmservices.xml  
RUN xmlstarlet ed -L -u
"//Parameter[@name=\"packagedRepo.dir.path\"]/@override" -v "true"
$CATALINA_HOME/conf/Catalina/localhost/wings-oodt-wmservices.xml  
  
#====================================RUN
TOMCAT================================================#  
WORKDIR /usr/local/wings/  
  
COPY startup.sh ./  
  
CMD ./startup.sh  
  

