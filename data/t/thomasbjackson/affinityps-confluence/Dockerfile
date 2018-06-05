FROM thomasbjackson/java:oracle-java7  
  
MAINTAINER Tom Jackson thomas.jackson@cprime.com  
  
# Version of Confluence to run  
# The only change need to run a different version is a change to this variable  
ENV CONFLUENCE_VERSION 5.7  
# Atlassian's download site for Confluence  
ENV DOWNLOAD_URL
https://downloads.atlassian.com/software/confluence/downloads/atlassian-
confluence-  
  
# Confluence install and home paths  
ENV CONFLUENCE_HOME /var/local/atlassian/confluence  
ENV CONFLUENCE_INSTALL /usr/local/confluence  
  
  
# Default JVM options  
# These are typically overriden/augmented via the --env-file run arg  
ENV CATALINA_OPTS \  
-Dfile.encoding=UTF-8 \  
-Xms6G \  
-Xmx6G   
  
# Install xmlstarlet for use in manipulating xml files in situ  
# Ability is useful for Atlassian apps that use an xml file to configure the
DB  
# connection but do not support variables in the files.  
RUN set -x \  
&& apt-get update --quiet \  
&& apt-get install --quiet --yes --no-install-recommends libtcnative-1
xmlstarlet  
  
# Create the install and home directories and setup ownership to daemon:daemon  
# Download and expand Confluence binaries into the install dir  
RUN mkdir -p "${CONFLUENCE_HOME}" \  
&& chmod -R 770 "${CONFLUENCE_HOME}" \  
&& chown daemon:daemon "${CONFLUENCE_HOME}" \  
&& mkdir -p "${CONFLUENCE_INSTALL}/conf" \  
&& mkdir -p "${CONFLUENCE_INSTALL}/security" \  
&& curl -L --silent ${DOWNLOAD_URL}${CONFLUENCE_VERSION}.tar.gz | tar -xz
--strip=1 -C "${CONFLUENCE_INSTALL}" \--no-same-owner \  
&& chmod -R 770 "${CONFLUENCE_INSTALL}/conf" \  
&& chmod -R 770 "${CONFLUENCE_INSTALL}/temp" \  
&& chmod -R 770 "${CONFLUENCE_INSTALL}/logs" \  
&& chmod -R 770 "${CONFLUENCE_INSTALL}/work" \  
&& chmod -R 770 "${CONFLUENCE_INSTALL}/security" \  
&& chown -R daemon:daemon "${CONFLUENCE_INSTALL}/conf" \  
&& chown -R daemon:daemon "${CONFLUENCE_INSTALL}/temp" \  
&& chown -R daemon:daemon "${CONFLUENCE_INSTALL}/logs" \  
&& chown -R daemon:daemon "${CONFLUENCE_INSTALL}/work" \  
&& chown -R daemon:daemon "${CONFLUENCE_INSTALL}/security"  
  
# Add the pkey and ssl certs to the /tmp dir  
ADD configs/certs/confluence.p7b /tmp/confluence.p7b  
ADD configs/certs/jira.p7b /tmp/jira.p7b  
ADD configs/certs/confluence.affinityps.com.key
/tmp/confluence.affinityps.com.key  
  
# Build the keystore from the cert  
# First convert from p7b format to pem format  
RUN openssl pkcs7 -print_certs -in /tmp/confluence.p7b -out
/tmp/confluence.pem  
  
# Next combine the private key and cert pem file into a single "keyed cert"
file  
RUN cat /tmp/confluence.affinityps.com.key /tmp/confluence.pem >
/tmp/confluence-keyed-cert.pem  
  
# Create keystore and import confluence cert into keystore  
# Note that if you change the name of the keystore, you also need to update
configs/server.xml with  
# new filename.  
ENV KEYSTORE_FILE confluence_keystore.pkcs12  
RUN openssl pkcs12 -export -in /tmp/confluence-keyed-cert.pem -out
$CONFLUENCE_INSTALL/security/$KEYSTORE_FILE -name jira-noiter -nomaciter
-password pass:affinityps  
  
# Make kesytore readonly  
RUN chmod 444 $CONFLUENCE_INSTALL/security/$KEYSTORE_FILE  
RUN chown -R daemon:daemon ${CONFLUENCE_INSTALL}/security/$KEYSTORE_FILE  
  
# point Confluence to its home directory.  
RUN echo "confluence.home=${CONFLUENCE_HOME}" >
${CONFLUENCE_INSTALL}/confluence/WEB-INF/classes/confluence-init.properties  
  
# Add custom versions of web.xml, server.xml, and urlrewrite to support ssl,
and http-to-https rewrites  
# Before overwriting each, save a copy off to a temp dir. server.xml and
urlrewrite.xml rarely change from  
# Confluence one release to the next, but web.xml does. The temp copies can be
referenced after an upgrade, and the  
# versions in the configs directory of this repo can be updted as needed.  
# web.xml has mods to support http to https rewrites  
RUN cp ${CONFLUENCE_INSTALL}/confluence/WEB-INF/web.xml
${CONFLUENCE_INSTALL}/temp/web.xml.$CONFLUENCE_VERSION  
ADD configs/web.xml ${CONFLUENCE_INSTALL}/confluence/WEB-INF/web.xml  
RUN chown -R daemon:daemon ${CONFLUENCE_INSTALL}/confluence/WEB-INF/web.xml  
  
# server.xml has mods to support ssl (the 8443 Connector)  
RUN cp ${CONFLUENCE_INSTALL}/conf/server.xml
${CONFLUENCE_INSTALL}/temp/server.xml.$CONFLUENCE_VERSION  
ADD configs/server.xml ${CONFLUENCE_INSTALL}/conf/server.xml  
RUN chown -R daemon:daemon ${CONFLUENCE_INSTALL}/conf/server.xml  
  
# urlrewrite.xml has mods to support http to https rewrites  
RUN cp ${CONFLUENCE_INSTALL}/confluence/WEB-INF/urlrewrite.xml
${CONFLUENCE_INSTALL}/temp/urlrewrite.xml.$CONFLUENCE_VERSION  
ADD configs/urlrewrite.xml ${CONFLUENCE_INSTALL}/confluence/WEB-
INF/urlrewrite.xml  
RUN chown -R daemon:daemon ${CONFLUENCE_INSTALL}/confluence/WEB-
INF/urlrewrite.xml  
  
# Create a directory where we can store customizable files for this  
# installation that have environment dependencies (e.g. cnames). We will move
default files  
# to this location and build symlinks back to each s.t. each can be overlayed
via a volume  
# bind in docker create container  
RUN install -d -m 0755 -o daemon -g daemon "${CONFLUENCE_HOME}/affinityps-
configs"  
  
# Add a re-usable script that will build the symlinks  
ADD configs/configs_linker.sh /tmp/configs_linker.sh  
RUN chmod 0744 /tmp/configs_linker.sh  
  
# Build the truststore and add the jira cert  
# Need to add certs for apps that confluence is app-linked to  
# First convert from p7b format to pem format  
RUN openssl pkcs7 -print_certs -in /tmp/jira.p7b -out /tmp/jira.pem  
  
# Convert cert from pem format to der format:  
RUN openssl x509 -outform der -in /tmp/jira.pem -out /tmp/jira.der  
  
# Load def-formatted jira cert into a new truststore  
# keytool prompts with "Trust this certificate?". Printf 'yes' in response.  
# ENV TRUSTSTORE_FILE confluence-truststore.jks  
# RUN printf 'yes' | keytool -import -file /tmp/jira.der -alias jira -keystore
$CONFLUENCE_INSTALL/security/$TRUSTSTORE_FILE -storepass affinityps  
# Make truststore readonly  
# RUN chmod 444 $CONFLUENCE_INSTALL/security/$TRUSTSTORE_FILE  
# RUN chown -R daemon:daemon ${CONFLUENCE_INSTALL}/security/$TRUSTSTORE_FILE  
# Load def-formatted jira cert into Java truststore. Password is per oracle
defaults  
RUN printf 'changeit\nyes' | keytool -import -file /tmp/jira.der -alias jira
-keystore /usr/lib/jvm/java-7-oracle/jre/lib/security/cacerts  
  
# add utility that can be used to fix a known keystore bug (CONF-11074)  
ADD configs/initKeyStore_4_2.jsp
${CONFLUENCE_INSTALL}/confluence/admin/initKeyStore_4_2.jsp  
  
# add startup script that adds env-specfic vesion of urlrewrite and starts
confluence  
ADD configs/start-container.sh ${CONFLUENCE_INSTALL}/bin/start-container.sh  
RUN chmod 555 ${CONFLUENCE_INSTALL}/bin/start-container.sh  
ADD configs/urlrewrite.xml ${CONFLUENCE_HOME}/affinityps-
configs/urlrewrite.xml  
RUN chown -R daemon:daemon ${CONFLUENCE_HOME}/affinityps-
configs/urlrewrite.xml  
  
# Run Confluence under the default unprivileged account. This could be
considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
# Note: this must be done before the volumes below are created  
USER daemon:daemon  
  
# Set volume mount points for installation and home directory. Changes to the  
# home directory needs to be persisted as well as parts of the installation  
# directory due to eg. logs  
# Also, logs need to be accessible to agents running in separate containers
(see README)  
VOLUME [ ${CONFLUENCE_INSTALL} , ${CONFLUENCE_HOME} ]  
  
# HTTP Port  
# EXPOSE 8090  
EXPOSE 8090 8443  
# Set the working directory to the directory where confluence will be launched  
WORKDIR /usr/local/confluence  
  
# Run Confluence in foreground  
CMD ["./bin/start-container.sh", "-fg"]  

