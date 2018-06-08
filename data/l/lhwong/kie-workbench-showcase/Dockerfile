#####################################################################################  
# Dockerfile that provides the image for JBoss KIE Workbench 7.0.0.Final
Showcase  
#####################################################################################  
  
####### BASE ############  
FROM lhwong/kie-workbench:latest  
  
####### MAINTAINER ############  
MAINTAINER "Michael Biarnes Kiefer" "mbiarnes@redhat.com"  
  
####### ENVIRONMENT ############  
# Use demo and examples by default in this showcase image (internet connection
required).  
ENV KIE_DEMO true  
ENV KIE_SERVER_PROFILE standalone-kie  
ENV DB_DRIVER_DOWNLOAD_URL http://central.maven.org/maven2/mysql/mysql-
connector-java/5.1.18/mysql-connector-java-5.1.18.jar  
  
#https://repository.jboss.org/nexus/service/local/repositories/central/content/mysql/mysql-
connector-java/5.1.18/mysql-connector-java-5.1.18.jar  
  
  
####### KIE Workbench CUSTOM CONFIGURATION ############  
ADD etc/standalone-kie.xml $JBOSS_HOME/standalone/configuration/standalone-
kie.xml  
ADD etc/users.properties $JBOSS_HOME/standalone/configuration/users.properties  
ADD etc/roles.properties $JBOSS_HOME/standalone/configuration/roles.properties  
  
####### DATABASE ############  
RUN mkdir -p $JBOSS_HOME/modules/com && \  
mkdir -p $JBOSS_HOME/modules/com/mysql && \  
mkdir -p $JBOSS_HOME/modules/com/mysql/main  
ADD etc/mysql_module.xml $JBOSS_HOME/modules/com/mysql/main/module.xml  
RUN curl -o $JBOSS_HOME/modules/com/mysql/main/mysql-connector-java.jar
$DB_DRIVER_DOWNLOAD_URL  
  
####### HTTPS #######  
ADD etc/applicationKeyStore.jks
$JBOSS_HOME/standalone/configuration/application.keystore  
  
EXPOSE 8443  
  
  
####### KEYCLOAK ######  
ENV KEYCLOAK_VERSION 3.1.0.Final  
  
WORKDIR $JBOSS_HOME  
  
RUN curl -L
https://downloads.jboss.org/keycloak/$KEYCLOAK_VERSION/adapters/keycloak-
oidc/keycloak-wildfly-adapter-dist-$KEYCLOAK_VERSION.tar.gz | tar zx  
  
#ADD etc/keycloak.json
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/keycloak.json  
#ADD etc/demo-keycloak.json
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/demo-
keycloak.json  
  
ADD etc/web.xml $JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-
INF/web.xml  
ADD etc/kie-git.json $JBOSS_HOME/kie-git.json  
  
#ADD etc/optabot-servlet-security-0.0.1-SNAPSHOT.jar
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/lib/optabot-
servlet-security-0.0.1-SNAPSHOT.jar  
  
# multi-tenancy support  
#ADD etc/keycloak-config-resolver-0.0.1-SNAPSHOT.jar
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/lib/keycloak-
config-resolver-0.0.1-SNAPSHOT.jar  
#ADD etc/keycloak-adapter-core-3.1.0.Final.jar
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/lib/keycloak-
adapter-core-3.1.0.Final.jar  
#ADD etc/keycloak-adapter-spi-3.1.0.Final.jar
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/lib/keycloak-
adapter-spi-3.1.0.Final.jar  
  
  
#https://github.com/AppFormer/uberfire/tree/master/uberfire-
extensions/uberfire-security/uberfire-security-management/uberfire-security-
management-keycloak  
  
#ADD etc/security-management.properties
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-
INF/classes/security-management.properties  
#ADD etc/uberfire-security-management-keycloak-2.0.0-SNAPSHOT.jar
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/lib/uberfire-
security-management-keycloak-2.0.0-SNAPSHOT.jar  
  
#ADD etc/keycloak-core-$KEYCLOAK_VERSION.jar
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/lib/keycloak-
core-$KEYCLOAK_VERSION.jar  
#ADD etc/keycloak-common-$KEYCLOAK_VERSION.jar
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/lib/keycloak-
common-$KEYCLOAK_VERSION.jar  
  
#ADD etc/jboss-deployment-structure.xml
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/jboss-
deployment-structure.xml  
  
#ADD etc/log4j.xml
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-
INF/classes/log4j.xml  
  
# Added files are chowned to root user, change it to the jboss one.  
USER root  
RUN chown jboss:jboss $JBOSS_HOME/standalone/configuration/standalone-kie.xml
&& \  
chown jboss:jboss $JBOSS_HOME/standalone/configuration/users.properties && \  
chown jboss:jboss $JBOSS_HOME/standalone/configuration/roles.properties && \  
chown jboss:jboss $JBOSS_HOME/modules/com/mysql/main/module.xml  
  
RUN chown jboss:jboss
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/web.xml && \  
chown jboss:jboss $JBOSS_HOME/kie-git.json  
#&& \  
#chown jboss:jboss
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/lib/optabot-
servlet-security-0.0.1-SNAPSHOT.jar  
  
#&& \  
#chown jboss:jboss
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-
INF/classes/security-management.properties && \  
#chown jboss:jboss
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/lib/keycloak-
core-$KEYCLOAK_VERSION.jar && \  
#chown jboss:jboss
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/lib/keycloak-
common-$KEYCLOAK_VERSION.jar && \  
#chown jboss:jboss
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/lib/uberfire-
security-management-keycloak-2.0.0-SNAPSHOT.jar && \  
#chown jboss:jboss
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/jboss-
deployment-structure.xml  
#&& \  
#chown jboss:jboss
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-
INF/classes/log4j.xml  
  
#RUN rm $JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-
INF/lib/uberfire-security-management-wildfly-1.3.0.Final.jar  
  
  
  
#chown jboss:jboss
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/lib/keycloak-
config-resolver-0.0.1-SNAPSHOT.jar && \  
#chown jboss:jboss
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/lib/keycloak-
adapter-core-3.1.0.Final.jar && \  
#chown jboss:jboss
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/lib/keycloak-
adapter-spi-3.1.0.Final.jar && \  
#chown jboss:jboss
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/keycloak.json
&& \  
#chown jboss:jboss
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war/WEB-INF/demo-
keycloak.json  
  
  
  
  
  
  
RUN mkdir -p $JBOSS_HOME/wb_git  
RUN chown jboss:jboss $JBOSS_HOME/wb_git  
  
  
# Switchback to jboss user  
USER jboss  
  
####### RUNNING DROOLS-WB ############  
WORKDIR $JBOSS_HOME/bin/  
CMD ["./start_kie-wb.sh"]

