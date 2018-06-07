###########################################################################  
# Dockerfile that provides the image for JBoss KIE Workbench 7.0.0.Final  
###########################################################################  
  
####### BASE ############  
FROM jboss/wildfly:10.1.0.Final  
  
####### MAINTAINER ############  
MAINTAINER "Michael Biarnes Kiefer" "mbiarnes@redhat.com"  
  
####### ENVIRONMENT ############  
ENV JBOSS_BIND_ADDRESS 0.0.0.0  
ENV KIE_REPOSITORY https://repository.jboss.org/nexus/content/groups/public-
jboss  
ENV KIE_VERSION 7.5.0.Final  
ENV KIE_CLASSIFIER wildfly10  
ENV KIE_CONTEXT_PATH kie-wb  
ENV KIE_SERVER_PROFILE standalone  
# Do NOT use demo neither examples by default in this image (no internet
connection required).  
ENV KIE_DEMO false  
ENV JAVA_OPTS -Xms512m -Xmx1024m -Djava.net.preferIPv4Stack=true  
  
####### KIE-WB ############  
RUN curl -o $HOME/$KIE_CONTEXT_PATH.war $KIE_REPOSITORY/org/kie/kie-
wb/$KIE_VERSION/kie-wb-$KIE_VERSION-$KIE_CLASSIFIER.war && \  
unzip -q $HOME/$KIE_CONTEXT_PATH.war -d
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war && \  
touch $JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war.dodeploy && \  
rm -rf $HOME/$KIE_CONTEXT_PATH.war  
  
####### MVN REPO ############  
# https://bugzilla.redhat.com/show_bug.cgi?id=1263738  
#RUN mkdir -p $HOME/.m2/repository/org/guvnor/guvnor-asset-mgmt-
project/$KIE_VERSION && \  
#curl -o $HOME/.m2/repository/org/guvnor/guvnor-asset-mgmt-
project/$KIE_VERSION/guvnor-asset-mgmt-project-$KIE_VERSION.jar
$KIE_REPOSITORY/org/guvnor/guvnor-asset-mgmt-project/7.0.0.Beta1/guvnor-asset-
mgmt-project-7.0.0.Beta1.jar  
  
####### SCRIPTS ############  
USER root  
ADD etc/start_kie-wb.sh $JBOSS_HOME/bin/start_kie-wb.sh  
RUN chown jboss:jboss $JBOSS_HOME/standalone/deployments/*  
RUN chown jboss:jboss $JBOSS_HOME/bin/start_kie-wb.sh  
  
#RUN mkdir -p $JBOSS_HOME/repositories  
#RUN chown jboss:jboss $JBOSS_HOME/repositories  
  
####### CUSTOM JBOSS USER ############  
# Switchback to jboss user  
USER jboss  
  
####### EXPOSE INTERNAL JBPM GIT PORT ############  
EXPOSE 8001  
  
####### RUNNING DROOLS-WB ############  
WORKDIR $JBOSS_HOME/bin/  
CMD ["./start_kie-wb.sh"]  

