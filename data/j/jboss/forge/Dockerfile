# Use latest jboss/base-jdk:8 image as the base  
FROM jboss/base-jdk:8  
# The maintainer of this Docker image  
MAINTAINER JBoss Forge Team <forge@redhat.com>  
  
# Set the FORGE_VERSION env variable  
ENV FORGE_VERSION 3.3.2.Final  
  
# Add the JBoss Forge distribution to /opt, and make forge the owner of the
extracted tar content  
# Make sure the distribution is available from a well-known place  
RUN cd $HOME && curl
http://downloads.jboss.org/forge/releases/$FORGE_VERSION/forge-
distribution-$FORGE_VERSION-offline.zip>forge-distribution-$FORGE_VERSION-
offline.zip && unzip forge-distribution-$FORGE_VERSION-offline.zip && mv
$HOME/forge-distribution-$FORGE_VERSION $HOME/forge && rm forge-
distribution-$FORGE_VERSION-offline.zip  
  
# Set the FORGE_HOME env variable  
ENV FORGE_HOME /opt/jboss/forge  
  
# Set the default command to run on boot  
# This will boot the Forge CLI  
CMD ["/opt/jboss/forge/bin/forge"]  

