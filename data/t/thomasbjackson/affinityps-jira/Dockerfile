FROM thomasbjackson/java:oracle-java7  
# FROM nordstromsets/atlassian-app  
MAINTAINER Tom Jackson thomas.jackson@cprime.com  
  
# Version of Jira to run  
# The only change need to run a different version is a change to this variable  
ENV JIRA_VERSION 6.3.15  
# Atlassian's download site for Jira  
ENV DOWNLOAD_URL
https://downloads.atlassian.com/software/jira/downloads/atlassian-jira-  
  
# Confluence install and home paths  
ENV JIRA_HOME /var/local/atlassian/jira  
ENV JIRA_INSTALL /usr/local/jira  
  
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
# Download and expand JIRA binaries into the install dir  
RUN mkdir -p "${JIRA_HOME}" \  
&& chmod -R 770 "${JIRA_HOME}" \  
&& chown daemon:daemon "${JIRA_HOME}" \  
&& mkdir -p "${JIRA_INSTALL}/conf" \  
&& mkdir -p "${JIRA_INSTALL}/security" \  
&& curl -L --silent ${DOWNLOAD_URL}${JIRA_VERSION}.tar.gz | tar -xz --strip=1
-C "${JIRA_INSTALL}" \--no-same-owner \  
&& chmod -R 770 "${JIRA_INSTALL}/conf" \  
&& chmod -R 770 "${JIRA_INSTALL}/temp" \  
&& chmod -R 770 "${JIRA_INSTALL}/logs" \  
&& chmod -R 770 "${JIRA_INSTALL}/work" \  
&& chown -R daemon:daemon "${JIRA_INSTALL}/conf" \  
&& chown -R daemon:daemon "${JIRA_INSTALL}/temp" \  
&& chown -R daemon:daemon "${JIRA_INSTALL}/logs" \  
&& chown -R daemon:daemon "${JIRA_INSTALL}/work" \  
&& chown -R daemon:daemon "${JIRA_INSTALL}/security"  
  
# Add the pkey and ssl certs to the /tmp dir  
ADD configs/certs/confluence.p7b /tmp/confluence.p7b  
ADD configs/certs/jira.p7b /tmp/jira.p7b  
ADD configs/certs/jira.affinityps.com.key /tmp/jira.affinityps.com.key  
  
# Build the keystore from the cert  
# First convert from p7b format to pem format  
RUN openssl pkcs7 -print_certs -in /tmp/jira.p7b -out /tmp/jira.pem  
  
# Next combine the private key and cert pem file into a single "keyed cert"
file  
RUN cat /tmp/jira.affinityps.com.key /tmp/jira.pem > /tmp/jira-keyed-cert.pem  
  
# Create keystore and import confluence cert into keystore  
# Note that if you change the name of the keystore, you also need to update
configs/server.xml with  
# new filename.  
ENV KEYSTORE_FILE jira_keystore.pkcs12  
RUN openssl pkcs12 -export -in /tmp/jira-keyed-cert.pem -out
$JIRA_INSTALL/security/$KEYSTORE_FILE -name jira -noiter -nomaciter -password
pass:affinityps  
  
# Make kesytore readonly  
RUN chmod 444 $JIRA_INSTALL/security/$KEYSTORE_FILE  
RUN chown -R daemon:daemon ${JIRA_INSTALL}/security/$KEYSTORE_FILE  
  
# point Jira to its home directory.  
RUN echo "jira.home=${JIRA_HOME}" > ${JIRA_INSTALL}/atlassian-jira/WEB-
INF/classes/jira-application.properties  
  
# Add custom versions of web.xml, server.xml, and urlrewrite to support ssl,
and http-to-https rewrites  
# Before overwriting each, save a copy off to a temp dir. server.xml and
urlrewrite.xml rarely change from  
# Jira one release to the next, but web.xml does. The temp copies can be
referenced after an upgrade, and the  
# versions in the configs directory of this repo can be updted as needed.  
# web.xml has mods to support http to https rewrites  
RUN cp ${JIRA_INSTALL}/atlassian-jira/WEB-INF/web.xml
${JIRA_INSTALL}/temp/web.xml.$JIRA_VERSION  
RUN chmod 0666 ${JIRA_INSTALL}/temp/web.xml.$JIRA_VERSION  
ADD configs/web.xml ${JIRA_INSTALL}/atlassian-jira/WEB-INF/web.xml  
RUN chown -R daemon:daemon ${JIRA_INSTALL}/atlassian-jira/WEB-INF/web.xml  
  
# server.xml has mods to support ssl (the 8443 Connector)  
RUN cp ${JIRA_INSTALL}/conf/server.xml
${JIRA_INSTALL}/temp/server.xml.$JIRA_VERSION  
RUN chmod 0666 ${JIRA_INSTALL}/temp/server.xml.$JIRA_VERSION  
ADD configs/server.xml ${JIRA_INSTALL}/conf/server.xml  
RUN chown -R daemon:daemon ${JIRA_INSTALL}/conf/server.xml  
  
# urlrewrite.xml has mods to support http to https rewrites  
RUN cp ${JIRA_INSTALL}/atlassian-jira/WEB-INF/urlrewrite.xml
${JIRA_INSTALL}/temp/urlrewrite.xml.$JIRA_VERSION  
RUN chmod 0666 ${JIRA_INSTALL}/temp/urlrewrite.xml.$JIRA_VERSION  
ADD configs/urlrewrite.xml ${JIRA_INSTALL}/atlassian-jira/WEB-
INF/urlrewrite.xml  
RUN chown -R daemon:daemon ${JIRA_INSTALL}/atlassian-jira/WEB-
INF/urlrewrite.xml  
  
# Build the truststore and add the confluence cert  
# Need to add certs for apps that jira is app-linked to  
# First convert from p7b format to pem format  
RUN openssl pkcs7 -print_certs -in /tmp/confluence.p7b -out
/tmp/confluence.pem  
  
# Convert cert from pem format to der format:  
RUN openssl x509 -outform der -in /tmp/confluence.pem -out /tmp/confluence.der  
  
# Load def-formatted confluence cert into a new truststore  
# keytool prompts with "Trust this certificate?". Printf 'yes' in response.  
# ENV TRUSTSTORE_FILE jira-truststore.jks  
# RUN printf 'yes' | keytool -import -file /tmp/confluence.der -alias
confluence -keystore $JIRA_INSTALL/security/$TRUSTSTORE_FILE -storepass
affinityps  
# Make truststore readonly  
# RUN chmod 444 $JIRA_INSTALL/security/$TRUSTSTORE_FILE  
# RUN chown -R daemon:daemon ${JIRA_INSTALL}/security/$TRUSTSTORE_FILE  
# Load def-formatted Confluence cert into Java truststore. Password is per
oracle defaults  
RUN printf 'changeit\nyes' | keytool -import -file /tmp/confluence.der -alias
confluence -keystore /usr/lib/jvm/java-7-oracle/jre/lib/security/cacerts  
  
# Install JavaMelody plugin for monitoring app  
RUN curl -L
https://github.com/javamelody/javamelody/releases/download/1.56.0/jira-
javamelody-1.56.0.jar > ${JIRA_INSTALL}/atlassian-jira/WEB-INF/lib/jira-
javamelody-1.56.0.jar  
  
# Run jira under the default unprivileged account. This could be considered
bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
# Note: this must be done before the volumes below are created  
USER daemon:daemon  
  
# Set volume mount points for installation and home directory. Changes to the  
# home directory needs to be persisted as well as parts of the installation  
# directory due to eg. logs  
# Also, logs need to be accessible to agents running in separate containers
(see README)  
VOLUME [ ${JIRA_INSTALL} , ${JIRA_HOME} ]  
  
# expose HTTP and HTTPS port per Connectors in server.xml  
EXPOSE 8080 8443  
# Set the working directory to the directory where jira will be launched  
WORKDIR /usr/local/jira  
  
# Run JIRA in foreground  
CMD ["./bin/start-jira.sh", "-fg"]  

