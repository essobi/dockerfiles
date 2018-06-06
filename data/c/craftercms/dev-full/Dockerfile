#Base  
FROM craftercms/tomcatbase:snapshot  
MAINTAINER Carlos Ortiz<carlos.ortiz@craftercms.org>  
#Set Container Envs  
ENV DATA_DB_PATH=$CRAFTER_HOME/data/db  
ENV DATA_REPO_PATH=$CRAFTER_HOME/data/repo  
  
ENV CRAFTER_VERSION=LATEST  
ENV SOLR_VERSION=4.10.4  
ENV MAVEN_REPO_URL=https://oss.sonatype.org  
ENV MAVEN_REPO=snapshots  
ENV DEPLOYER_HOME=$CRAFTER_HOME/deployer  
#Change dir to CRAFTER_HOME  
WORKDIR ${CRAFTER_HOME}  
RUN mkdir -p data  
RUN mkdir -p ${DATA_REPO_PATH}  
ADD ./config/studio/server-config.properties
$CATALINA_HOME/shared/classes/crafter/cstudio/extension/  
ADD ./config/studio/services-context.xml
$CATALINA_HOME/shared/classes/crafter/cstudio/extension/  
  
ADD ./config/engine/server-config.properties
$CATALINA_HOME/shared/classes/crafter/engine/extension/  
ADD ./config/engine/rendering-context.xml
$CATALINA_HOME/shared/classes/crafter/engine/extension/  
ADD ./config/engine/services-context.xml
$CATALINA_HOME/shared/classes/crafter/engine/extension/  
  
ADD ./config/solr-crafter.xml $CATALINA_HOME/conf/Catalina/localhost/  
  
#TODO Make this the proper ZIP file on next RELEASE  
ADD
"$MAVEN_REPO_URL/service/local/artifact/maven/redirect?r=$MAVEN_REPO&g=org.craftercms&a=crafter-
studio-publishing-receiver-zip&v=$CRAFTER_VERSION&p=zip" deployer.zip  
ADD
"http://repository.sonatype.org/service/local/artifact/maven/redirect?r=central-
proxy&g=commons-daemon&a=commons-daemon&v=1.0.15" $DEPLOYER_HOME/commons-
daemon.jar  
RUN unzip deployer.zip -d $DEPLOYER_HOME  
RUN rm deployer.zip  
RUN chmod +x $DEPLOYER_HOME/*.sh  
  
WORKDIR ${CATALINA_HOME}  
#Download all Crafter Wars  
ADD
"$MAVEN_REPO_URL/service/local/artifact/maven/redirect?r=$MAVEN_REPO&g=org.craftercms&a=crafter-
studio-2&v=$CRAFTER_VERSION&p=war" $CATALINA_HOME/webapps/studio.war  
ADD
"$MAVEN_REPO_URL/service/local/artifact/maven/redirect?r=$MAVEN_REPO&g=org.craftercms&a=crafter-
search-server&v=$CRAFTER_VERSION&p=war" $CATALINA_HOME/webapps/crafter-
search.war  
ADD
"$MAVEN_REPO_URL/service/local/artifact/maven/redirect?r=$MAVEN_REPO&g=org.craftercms&a=crafter-
engine&v=$CRAFTER_VERSION&p=war" $CATALINA_HOME/webapps/ROOT.war  
ADD
"http://repository.sonatype.org/service/local/artifact/maven/redirect?r=central-
proxy&g=org.apache.solr&a=solr&v=$SOLR_VERSION&p=war"
$CATALINA_HOME/webapps/solr-crafter.war  
  
RUN git clone https://github.com/craftercms/search.git  
RUN mkdir solr-crafter  
RUN cp -rf search/crafter-search-provider/solr/* solr-crafter/  
RUN rm -rf search  
  
#Make Sure we can override this later !  
RUN rm /opt/craftercms/deployer/conf/*  
RUN mkdir -pv /opt/craftercms/deployer/target/site/content/  
ADD ./config/deployer/sample-target-context.xml /opt/craftercms/deployer/conf  
ADD ./config/deployer/preview-target-context.xml /opt/craftercms/deployer/conf  
  
VOLUME ${CRAFTER_HOME}/data  
VOLUME ${CRAFTER_HOME}/deployer/conf  
VOLUME ${CRAFTER_HOME}/deployer/target  
  
WORKDIR ${CRAFTER_HOME}  
ADD ./config/runStudio.sh /opt/craftercms/  
#StartTomcat!!:  
CMD ["./runStudio.sh"]  

