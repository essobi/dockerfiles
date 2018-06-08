###########################################################################  
# Dockerfile that provides the image for JBoss jBPM Workbench 7.0.0.CR2  
###########################################################################  
  
####### BASE ############  
FROM jboss/wildfly:10.1.0.Final  
  
####### MAINTAINER ############  
MAINTAINER "Martijn Burger" "martijnburger@paston.nl"  
  
####### ENVIRONMENT ############  
ENV JBOSS_BIND_ADDRESS 0.0.0.0  
ENV KIE_REPOSITORY https://repository.jboss.org/nexus/content/groups/public-
jboss  
ENV KIE_VERSION 7.0.0.CR3  
ENV KIE_CLASSIFIER wildfly10  
ENV KIE_SERVER_CLASSIFIER ee7  
ENV KIE_CONTEXT_PATH kie-wb  
ENV KIE_SERVER_CONTEXT_PATH kie-server  
ENV KIE_SERVER_ID kie-server  
ENV KIE_SERVER_LOCATION http://localhost:8080/kie-server/services/rest/server  
ENV KIE_SERVER_USER kieserver  
ENV KIE_SERVER_PWD kieserver1!  
ENV KIE_SERVER_CONTROLLER http://localhost:8080/kie-wb/rest/controller  
ENV KIE_SERVER_CONTROLLER_USER admin  
ENV KIE_SERVER_CONTROLLER_PWD admin  
ENV KIE_MAVEN_REPO http://localhost:8080/kie-wb/maven2  
ENV KIE_MAVEN_REPO_USER admin  
ENV KIE_MAVEN_REPO_PASSWORD admin  
ENV JAVA_OPTS -Xms256m -Xmx1024m -Djava.net.preferIPv4Stack=true  
# Do NOT use demo neither examples by default in this image (no internet
connection required).  
ENV KIE_DEMO false  
ENV KIE_SERVER_PROFILE standalone-full-kie  
  
###### SWITCH USER root ######  
USER root  
  
###### INSTALL PACKAGES ######  
RUN yum install -y net-tools  
  
##### SWITCH BACK TO jboss ####  
USER jboss  
  
####### KIE-WB ############  
RUN curl -o $HOME/$KIE_CONTEXT_PATH.war $KIE_REPOSITORY/org/kie/kie-
wb/$KIE_VERSION/kie-wb-$KIE_VERSION-$KIE_CLASSIFIER.war && \  
unzip -q $HOME/$KIE_CONTEXT_PATH.war -d
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war && \  
touch $JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war.dodeploy && \  
rm -rf $HOME/$KIE_CONTEXT_PATH.war  
  
####### KIE-SERVER ########  
RUN curl -o $HOME/$KIE_SERVER_CONTEXT_PATH.war
$KIE_REPOSITORY/org/kie/server/kie-server/$KIE_VERSION/kie-
server-$KIE_VERSION-$KIE_SERVER_CLASSIFIER.war && \  
unzip -q $HOME/$KIE_SERVER_CONTEXT_PATH.war -d
$JBOSS_HOME/standalone/deployments/$KIE_SERVER_CONTEXT_PATH.war && \  
touch $JBOSS_HOME/standalone/deployments/$KIE_SERVER_CONTEXT_PATH.war.dodeploy
&& \  
rm -rf $HOME/$KIE_SERVER_CONTEXT_PATH.war  
  
###### SWITCH USER root ######  
USER root  
  
####### CONFIGURATION ############  
ADD etc/start_kie-wb.sh $JBOSS_HOME/bin/start_kie-wb.sh  
ADD etc/standalone-full-kie.xml
$JBOSS_HOME/standalone/configuration/standalone-full-kie.xml  
ADD etc/kie-users.properties $JBOSS_HOME/standalone/configuration/kie-
users.properties  
ADD etc/kie-roles.properties $JBOSS_HOME/standalone/configuration/kie-
roles.properties  
ADD etc/settings.xml $JBOSS_HOME/../.m2/settings.xml  
ADD etc/fix-kie-git.sh $JBOSS_HOME/bin/fix-kie-git.sh  
  
  
RUN chown jboss:jboss $JBOSS_HOME/standalone/deployments/*
$JBOSS_HOME/bin/start_kie-wb.sh $JBOSS_HOME/bin/fix-kie-git.sh
$JBOSS_HOME/standalone/configuration/standalone-full-kie.xml
$JBOSS_HOME/standalone/configuration/kie-users.properties
$JBOSS_HOME/standalone/configuration/kie-roles.properties $JBOSS_HOME/../.m2  
RUN chmod 755 $JBOSS_HOME/bin/start_kie-wb.sh $JBOSS_HOME/bin/fix-kie-git.sh  
  
####### MYSQL ###########  
RUN mkdir -p /opt/jboss/wildfly/modules/system/layers/base/com/mysql/main; cd
/opt/jboss/wildfly/modules/system/layers/base/com/mysql/main && curl -O
http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.18/mysql-
connector-java-5.1.18.jar  
ADD etc/module-mysql.xml
/opt/jboss/wildfly/modules/system/layers/base/com/mysql/main/module.xml  
  
####### KEYCLOAK #########  
RUN cd /opt/jboss/wildfly; curl -O
https://downloads.jboss.org/keycloak/3.1.0.Final/adapters/keycloak-
oidc/keycloak-wildfly-adapter-dist-3.1.0.Final.tar.gz; tar xzf keycloak-
wildfly-adapter-dist-3.1.0.Final.tar.gz; rm keycloak-wildfly-adapter-
dist-3.1.0.Final.tar.gz  
ADD etc/kie-git.json /opt/jboss/wildfly/standalone/configuration/kie-git.json  
RUN chown jboss:jboss /opt/jboss/wildfly/standalone/configuration/kie-git.json  
  
####### Standalone.xml transformations #######  
ADD etc/changeStandalone.xsl /opt/jboss/wildfly/changeStandalone.xsl  
RUN java -jar /usr/share/java/saxon.jar
-s:/opt/jboss/wildfly/standalone/configuration/standalone-full-kie.xml
-xsl:/opt/jboss/wildfly/changeStandalone.xsl
-o:/opt/jboss/wildfly/standalone/configuration/standalone-full-kie.xml; rm
/opt/jboss/wildfly/changeStandalone.xsl  
  
####### web.xml transformations #####  
ADD etc/changeWeb.xsl /opt/jboss/wildfly/changeWeb.xsl  
RUN java -jar /usr/share/java/saxon.jar
-s:/opt/jboss/wildfly/standalone/deployments/kie-wb.war/WEB-INF/web.xml
-xsl:/opt/jboss/wildfly/changeWeb.xsl
-o:/opt/jboss/wildfly/standalone/deployments/kie-wb.war/WEB-INF/web.xml; rm
/opt/jboss/wildfly/changeWeb.xsl  
  
####### CUSTOM JBOSS USER ############  
# Switchback to jboss user  
USER jboss  
  
####### EXPOSE INTERNAL JBPM GIT PORT ############  
EXPOSE 8001  
  
####### RUNNING JBPM-WB ############  
WORKDIR $JBOSS_HOME/bin/  
CMD ["./start_kie-wb.sh"]  

