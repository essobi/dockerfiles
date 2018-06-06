# This image provides a base for building and running WildFly applications  
# with the option of running a Thermostat agent as a secondary process.  
#  
# It builds using maven and runs the resulting artifacts on WildFly 10.1.0
Final  
# This test image is based on:  
# https://github.com/openshift-s2i/s2i-wildfly folder 10.1  
FROM icedtea/thermostat-agent-builder  
  
EXPOSE 8080  
ENV WILDFLY_VERSION=10.1.0.Final  
  
LABEL io.k8s.description="Platform for building and running JEE applications
on WildFly 10.1.0.Final" \  
io.k8s.display-name="WildFly 10.1.0.Final" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,wildfly,wildfly10" \  
io.openshift.s2i.destination="/opt/s2i/destination"  
  
# Tell base image about our S2I destination  
ENV THERMOSTAT_SOURCE_DIR="/opt/s2i/destination"  
USER root  
  
RUN INSTALL_PKGS="tar unzip bc which lsof java-1.8.0-openjdk
java-1.8.0-openjdk-devel" && \  
yum install -y yum-utils && \  
yum-config-manager --enable rhel-7-server-rpms && \  
yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS && \  
rpm -V $INSTALL_PKGS && \  
yum clean all -y && \  
mkdir -p /wildfly && \  
(curl -v
https://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
| tar -zx --strip-components=1 -C /wildfly) && \  
mkdir -p /opt/s2i/destination  
  
# Add s2i wildfly customizations  
ADD ./contrib/wfmodules/ /wildfly/modules/  
ADD ./contrib/wfbin/standalone.conf /wildfly/bin/standalone.conf  
ADD ./contrib/wfcfg/standalone.xml
/wildfly/standalone/configuration/standalone.xml  
ADD ./contrib/settings.xml $HOME/.m2/  
  
# Copy the S2I scripts from the specific language image to $STI_SCRIPTS_PATH  
COPY ./s2i/bin/ ${STI_SCRIPTS_PATH}  
  
RUN chown -R 1001:0 /wildfly && chown -R 1001:0 $HOME && \  
chmod -R ug+rw /wildfly && \  
chmod -R g+rw /opt/s2i/destination  
  
# Cleanup the hsperdata_<user> directories in /tmp  
# These might otherwise conflict with directories created  
# at image runtime. In which case jvmstat-based tools  
# won't be funtional. The JVM won't expose the memory-mapped  
# file if the users' directory already exists and permissions  
# don't match  
RUN rm -rf /tmp/hsperfdata_*  
  
USER 1001  
CMD ${STI_SCRIPTS_PATH}/usage  

