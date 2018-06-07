FROM tomcat:7  
MAINTAINER Oliver Nautsch <oliver.nautsch@nautsch.com>  
  
ENV DROOLS_VERSION 6.1.0.Final  
ENV DROOLS_WB_WAR_URL
https://repository.jboss.org/nexus/content/repositories/public/org/kie/kie-
drools-wb-distribution-wars/$DROOLS_VERSION/kie-drools-wb-distribution-
wars-$DROOLS_VERSION-tomcat7.0.war  
  
RUN curl -SL "$DROOLS_WB_WAR_URL" -o droolswb.war \  
&& mv droolswb.war $CATALINA_HOME/webapps/  
  
# see https://github.com/droolsjbpm/kie-wb-distributions/tree/6.1.x/kie-
drools-wb/kie-drools-wb-distribution-wars/src/main/tomcat7  
ADD ./tomcat/setenv.sh $CATALINA_HOME/bin/  
RUN chmod +x $CATALINA_HOME/bin/setenv.sh  
  
ENV DROOLS_TOMCAT_INTEGRATION_URL
https://repository.jboss.org/nexus/content/groups/public/org/kie/kie-tomcat-
integration/$DROOLS_VERSION/kie-tomcat-integration-$DROOLS_VERSION.jar  
  
RUN curl -SL "$DROOLS_TOMCAT_INTEGRATION_URL" -o kie-tomcat-
integration-$DROOLS_VERSION.jar \  
&& mv kie-tomcat-integration-$DROOLS_VERSION.jar $CATALINA_HOME/lib/  
  
ADD ./tomcat/server.xml $CATALINA_HOME/conf/  
  
ENV JACC_VERSION 1.5  
ENV JACC_URL
https://bintray.com/artifact/download/bintray/jcenter/javax/security/jacc/javax.security.jacc-
api/$JACC_VERSION/javax.security.jacc-api-$JACC_VERSION.jar  
  
RUN curl -SL "$JACC_URL" -o javax.security.jacc-api-$JACC_VERSION.jar \  
&& mv javax.security.jacc-api-$JACC_VERSION.jar $CATALINA_HOME/lib/  
  
ENV SLF4J_VERSION 1.7.9  
ENV SLF4J_URL
https://bintray.com/artifact/download/bintray/jcenter/org/slf4j/slf4j-api/$SLF4J_VERSION/slf4j-api-$SLF4J_VERSION.jar  
  
RUN curl -SL "$SLF4J_URL" -o slf4j-api-$SLF4J_VERSION.jar \  
&& mv slf4j-api-$SLF4J_VERSION.jar $CATALINA_HOME/lib/  
  

