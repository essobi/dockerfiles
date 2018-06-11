# Use Wildfly 10 image as the base  
FROM jboss/wildfly:10.0.0.Final  
  
MAINTAINER Eric Wittmann <eric.wittmann@redhat.com>  
  
ENV APIMAN_VERSION 1.2.9.Final  
  
RUN $JBOSS_HOME/bin/add-user.sh admin admin123! --silent  
  
RUN cd $JBOSS_HOME \  
&& curl http://downloads.jboss.org/overlord/apiman/$APIMAN_VERSION/apiman-
distro-wildfly10-$APIMAN_VERSION-overlay.zip -o apiman-distro-
wildfly10-$APIMAN_VERSION-overlay.zip \  
&& bsdtar -xf apiman-distro-wildfly10-$APIMAN_VERSION-overlay.zip \  
&& rm apiman-distro-wildfly10-$APIMAN_VERSION-overlay.zip  
  
RUN rm -f $JBOSS_HOME/standalone/deployments/apiman-ds.xml  
RUN rm -f $JBOSS_HOME/standalone/deployments/apiman-es.war  
RUN rm -f $JBOSS_HOME/standalone/deployments/apiman.war  
RUN rm -f $JBOSS_HOME/standalone/deployments/apimanui.war  
  
# Add standalone-apiman.xml  
ADD standalone-apiman.xml $JBOSS_HOME/standalone/configuration/  
  
# Apiman properties  
ADD apiman.properties $JBOSS_HOME/standalone/configuration/  
  
COPY m2 $JBOSS_HOME/m2  
  
# Postgres  
ADD postgresql-9.3-1102-jdbc41.jar $JBOSS_HOME/standalone/deployments  
  
# Add apiman-ds.xml.xml  
ADD apiman-ds.xml $JBOSS_HOME/standalone/deployments  
  
# Add modules.xml.xml  
ADD modules.xml $JBOSS_HOME/standalone/deployments  
  
# Set the default command to run on boot  
ENTRYPOINT ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0",
"-bmanagement", "0.0.0.0", "-c", "standalone-apiman.xml"]  

