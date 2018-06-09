#  
# Note. cannot use jboss/teiid since it sets standalone directory as a volume
which means  
# although files can be copied to it, their permissions cannot be changed
using chown so  
# this uses the jboss/teiid steps but leaves out the VOLUME command.  
#  
FROM jboss/wildfly:10.0.0.Final  
MAINTAINER Teiid-Komodo Community <http://teiiddesigner.jboss.org>  
  
# Env variables  
ENV VDB_BENCH_RELEASE_DIRECTORY "0.1-SNAPSHOT"  
ENV VDB_BENCH_RELEASE_EAR "vdb-bench-ear-0.1-20170227.193529-6.ear"  
ENV VDB_BENCH_EAR_URL
"https://repository.jboss.org/nexus/service/local/repositories/snapshots/content/org/teiid/vdb-
bench-ear/$VDB_BENCH_RELEASE_DIRECTORY/$VDB_BENCH_RELEASE_EAR"  
ENV VDB_BENCH_EAR_FILE "ds-builder-archive.ear"  
ENV JBOSS_HOME /opt/jboss/wildfly  
ENV TEIID_VERSION 9.1.0.Final  
  
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
  
# Add in the teiid configuration, which includes the ssl parameters  
COPY standalone.xml $JBOSS_HOME/standalone/configuration/standalone-teiid.xml  
  
# Add user credentials for access  
COPY application-users.properties $JBOSS_HOME/standalone/configuration/  
COPY application-roles.properties $JBOSS_HOME/standalone/configuration/  
COPY mgmt-users.properties $JBOSS_HOME/standalone/configuration/  
  
# Download and add the dsbuilder archive ear  
ADD $VDB_BENCH_EAR_URL $JBOSS_HOME/standalone/deployments/$VDB_BENCH_EAR_FILE  
  
#  
# ADD and COPY always create files as root. Need to call  
# chown to have them owned by the jboss user  
#  
USER root  
RUN chown -R jboss:jboss ${JBOSS_HOME}/standalone  
  
# Change to jboss user for running the server  
USER jboss  
  
# Expose the wildfly and teiid ports  
EXPOSE 8080 8443 9990 31000 35432  
CMD ["/bin/sh", "-c", "$JBOSS_HOME/bin/standalone.sh -c standalone-teiid.xml
-b 0.0.0.0 -bmanagement 0.0.0.0"]  

