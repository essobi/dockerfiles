##################################################################################  
# Dockerfile that provides the image for JBoss UF Dashbuilder 0.3.4.Final
Showcase  
##################################################################################  
  
####### BASE ############  
FROM jboss/uf-dashbuilder:0.3.4.Final  
  
####### MAINTAINER ############  
MAINTAINER "Roger Martinez" "romartin@redhat.com"  
  
####### UF Dashbuilder CUSTOM CONFIGURATION ############  
ADD etc/standalone-full-dashbuilder.xml
$JBOSS_HOME/standalone/configuration/standalone-full-dashbuilder.xml  
ADD etc/dashbuilder-users.properties
$JBOSS_HOME/standalone/configuration/dashbuilder-users.properties  
ADD etc/dashbuilder-roles.properties
$JBOSS_HOME/standalone/configuration/dashbuilder-roles.properties  
  
# Added files are chowned to root user, change it to the jboss one.  
USER root  
RUN chown jboss:jboss $JBOSS_HOME/standalone/configuration/standalone-full-
dashbuilder.xml && \  
chown jboss:jboss $JBOSS_HOME/standalone/configuration/dashbuilder-
users.properties && \  
chown jboss:jboss $JBOSS_HOME/standalone/configuration/dashbuilder-
roles.properties  
  
# Switchback to jboss user  
USER jboss  
  
####### RUNNING UF Dashbuilder ############  
WORKDIR $JBOSS_HOME/bin/  
CMD ["./standalone.sh", "-b", "$JBOSS_BIND_ADDRESS", "--server-
config=standalone-full-dashbuilder.xml"]  

