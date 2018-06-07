###################################################################  
# Dockerfile that provides the image for UF Dashbuilder 0.3.4.Final  
###################################################################  
  
####### BASE ############  
FROM jboss/wildfly:8.2.0.Final  
  
####### MAINTAINER ############  
MAINTAINER "Roger Martinez" "romartin@redhat.com"  
  
####### ENVIRONMENT ############  
ENV JBOSS_BIND_ADDRESS 0.0.0.0  
ENV KIE_REPOSITORY https://repository.jboss.org/nexus/content/groups/public-
jboss  
ENV KIE_VERSION 0.3.4.Final  
ENV KIE_CLASSIFIER wildfly8  
ENV KIE_CONTEXT_PATH dashbuilder  
ENV JAVA_OPTS -XX:MaxPermSize=256m -Xms256m -Xmx512m  
  
####### CUSTOM JBOSS USER ############  
# Switchback to jboss user  
USER jboss  
  
####### UF Dashbuilder ############  
RUN curl -o $HOME/$KIE_CONTEXT_PATH.war
$KIE_REPOSITORY/org/dashbuilder/dashbuilder-distros/$KIE_VERSION/dashbuilder-
distros-$KIE_VERSION-$KIE_CLASSIFIER.war && \  
unzip -q $HOME/$KIE_CONTEXT_PATH.war -d
$JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war && \  
touch $JBOSS_HOME/standalone/deployments/$KIE_CONTEXT_PATH.war.dodeploy && \  
rm -rf $HOME/$KIE_CONTEXT_PATH.war  
  
####### EXPOSE INTERNAL GIT PORT ############  
EXPOSE 8001  
  
####### RUNNING UF Dashbuilder ############  
WORKDIR $JBOSS_HOME/bin/  
CMD ["./standalone.sh", "-b", "$JBOSS_BIND_ADDRESS", "--server-
config=standalone-full.xml"]

