# this is a copy past from https://github.com/jboss-
dockerfiles/wildfly/blob/5746e28501a06a8c30bba39256e295fa1240cbf3/Dockerfile
but replacing wildfly references  
# Use latest jboss/base-jdk:8 image as the base  
FROM jboss/base-jdk:8  
# Set the JBOSS_EAP_VERSION env variable  
ENV JBOSS_EAP_VERSION 6.4  
ENV JBOSS_EAP_PATCH_VERSION 0  
ENV JBOSS_EAP_SHA1 9ac2979fe92040a039a3a3db8b4ce8d166e2c872  
ENV JBOSS_HOME /opt/jboss/jboss-eap  
  
USER root  
  
# Add the WildFly distribution to /opt, and make jboss-eap the owner of the
extracted tar content  
# Make sure the distribution is available from a well-known place  
RUN cd $HOME \  
&& curl -L -o jboss-eap-$JBOSS_EAP_VERSION.$JBOSS_EAP_PATCH_VERSION.zip
https://www.dropbox.com/s/ac3sie1ho2s8avn/jboss-
eap-$JBOSS_EAP_VERSION.$JBOSS_EAP_PATCH_VERSION.zip?dl=1 \  
&& sha1sum jboss-eap-$JBOSS_EAP_VERSION.$JBOSS_EAP_PATCH_VERSION.zip | grep
$JBOSS_EAP_SHA1 \  
&& unzip jboss-eap-$JBOSS_EAP_VERSION.$JBOSS_EAP_PATCH_VERSION.zip \  
&& mv $HOME/jboss-eap-$JBOSS_EAP_VERSION $JBOSS_HOME \  
&& rm jboss-eap-$JBOSS_EAP_VERSION.$JBOSS_EAP_PATCH_VERSION.zip \  
&& chown -R jboss:0 ${JBOSS_HOME} \  
&& chmod -R g+rw ${JBOSS_HOME}  
  
# Ensure signals are forwarded to the JVM process correctly for graceful
shutdown  
ENV LAUNCH_JBOSS_IN_BACKGROUND true  
  
USER jboss  
  
# Expose the ports we're interested in  
EXPOSE 8080 9990 4447 9999  
# Set the default command to run on boot  
# This will boot JBoss EAP in the standalone mode and bind to all interface  
CMD ["/opt/jboss/jboss-eap/bin/standalone.sh", "-b", "0.0.0.0",
"-bmanagement", "0.0.0.0"]  

