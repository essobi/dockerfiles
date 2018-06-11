# Use latest jboss/base-jdk:7 image as the base  
FROM jboss/base-jdk:7  
# Set the JBOSS_VERSION env variable  
ENV JBOSS_VERSION 7.1.1.Final  
ENV JBOSS_SHA1 fcec1002dce22d3281cc08d18d0ce72006868b6f  
ENV JBOSS_HOME /opt/jboss/wildfly  
ENV JBOSS_URL http://download.jboss.org/jbossas/7.1/jboss-
as-7.1.1.Final/jboss-as-7.1.1.Final.tar.gz  
  
# Add the JBoss distribution to /opt, and make jboss the owner of the
extracted tar content  
# Make sure the distribution is available from a well-known place  
RUN cd $HOME \  
&& curl -o ${JBOSS_VERSION}.tar.gz ${JBOSS_URL} \  
&& sha1sum ${JBOSS_VERSION}.tar.gz | grep ${JBOSS_SHA1} \  
&& mkdir -p ${JBOSS_HOME} \  
&& tar --strip-components 1 -xaf ${JBOSS_VERSION}.tar.gz -C ${JBOSS_HOME} \  
&& rm $JBOSS_VERSION.tar.gz  
  
# Ensure signals are forwarded to the JVM process correctly for graceful
shutdown  
ENV LAUNCH_JBOSS_IN_BACKGROUND true  
  
# Expose the ports we're interested in  
EXPOSE 8080  
# Set the default command to run on boot  
# This will boot JBoss AS in the standalone mode and bind to all interface  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]  

