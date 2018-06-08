FROM jetty:9-jre8  
  
MAINTAINER mark.cooper@lyrasis.org  
  
ENV FCREPO_HOME=/opt/data \  
FCREPO_NAME=fcrepo \  
FCREPO_VERSION=4.7.3 \  
JETTY_WEBAPPS=/var/lib/jetty/webapps  
  
ENV JAVA_OPTIONS="-Dfile.encoding=UTF-8 -Dfcrepo.home=${FCREPO_HOME}
-Dfcrepo.modeshape.configuration=classpath:/config/file-
simple/repository.json" \  
FCREPO_URL=https://github.com/fcrepo4/fcrepo4/releases/download/fcrepo-${FCREPO_VERSION}/fcrepo-
webapp-${FCREPO_VERSION}.war  
  
RUN wget -O ${JETTY_WEBAPPS}/${FCREPO_NAME}.war $FCREPO_URL  
RUN mkdir $FCREPO_HOME && chown -R jetty:jetty $FCREPO_HOME  
  
VOLUME ["$FCREPO_HOME"]  
  
CMD ["java","-jar","/usr/local/jetty/start.jar"]  

