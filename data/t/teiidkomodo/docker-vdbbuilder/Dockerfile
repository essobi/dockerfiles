#  
# Note. cannot use jboss/teiid since it sets standalone directory as a volume
which means  
# although files can be copied to it, their permissions cannot be changed
using chown so  
# this uses the jboss/teiid steps but leaves out the VOLUME command.  
#  
FROM jboss/wildfly:10.1.0.Final  
MAINTAINER Teiid-Komodo Community <http://teiiddesigner.jboss.org>  
  
# Env variables  
ENV VDB_BUILDER_RELEASE_DIRECTORY "0.0.4-SNAPSHOT"  
ENV VDB_BUILDER_RELEASE_WAR "komodo-rest-0.0.4-20170406.085836-1.war"  
ENV VDB_BUILDER_WAR_URL
"https://repository.jboss.org/nexus/service/local/repositories/snapshots/content/org/komodo/komodo-
rest/$VDB_BUILDER_RELEASE_DIRECTORY/$VDB_BUILDER_RELEASE_WAR"  
ENV VDB_BUILDER_WAR_FILE "vdb-builder.war"  
ENV BIN_DIR "/usr/local/bin"  
ENV JBOSS_HOME /opt/jboss/wildfly  
ENV TEIID_VERSION 9.1.0.Final  
  
user root  
  
# Download and unzip wildfly-teiid distribution  
RUN cd $JBOSS_HOME \  
&& curl -O
https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/teiid/teiid/$TEIID_VERSION/teiid-$TEIID_VERSION-
wildfly-dist.zip \  
&& bsdtar -xf teiid-$TEIID_VERSION-wildfly-dist.zip \  
&& chmod +x $JBOSS_HOME/bin/*.sh \  
&& rm teiid-$TEIID_VERSION-wildfly-dist.zip  
  
# Add ssl store for https  
ADD ssl $JBOSS_HOME/standalone/configuration/ssl  
  
# Add binary running configuration  
COPY bin/* $JBOSS_HOME/bin/  
  
# Add in the teiid configuration, which includes the ssl parameters  
COPY standalone.xml $JBOSS_HOME/standalone/configuration/standalone-teiid.xml  
  
# Add user credentials for access  
COPY application-users.properties $JBOSS_HOME/standalone/configuration/  
COPY application-roles.properties $JBOSS_HOME/standalone/configuration/  
COPY mgmt-users.properties $JBOSS_HOME/standalone/configuration/  
  
# Download and add the vdb-builder war  
ADD $VDB_BUILDER_WAR_URL
$JBOSS_HOME/standalone/deployments/$VDB_BUILDER_WAR_FILE  
  
#  
# ADD and COPY always create files as root. Need to call  
# chown to have them owned by the jboss user  
#  
#  
# Copy wildfly exec script and set permissions  
#  
COPY wildfly-exec.sh ${BIN_DIR}/  
  
USER root  
RUN chown -R jboss:0 ${JBOSS_HOME} \  
&& chmod -R g+rw ${JBOSS_HOME} \  
&& chmod +x ${BIN_DIR}/wildfly-exec.sh \  
&& yum -y install --setopt=tsflags=nodocs bc  
  
# Change to jboss user for running the server  
USER jboss  
  
# Expose the wildfly and teiid ports  
EXPOSE 8080 8443 9990 31000 35432  
#  
# The default cmd for this container  
#  
CMD ["/bin/sh", "-c", "${BIN_DIR}/wildfly-exec.sh"]  
  

