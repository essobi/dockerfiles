FROM openjdk:8-jre  
  
# explicitly set user/group IDs  
RUN groupadd -r keycloak --gid=1029 && useradd -r -g keycloak --uid=1029 -d
/opt/keycloak keycloak  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.10  
RUN arch="$(dpkg --print-architecture)" \  
&& set -x \  
&& apt-get update \  
&& apt-get install -y netcat-openbsd \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -o /usr/local/bin/gosu -fSL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$arch" \  
&& curl -o /usr/local/bin/gosu.asc -fSL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$arch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
ENV KEYCLOAK_VERSION=3.4.3.Final \  
LOGSTASH_GELF_VERSION=1.11.2 \  
DCM4CHE_VERSION=5.13.1 \  
JBOSS_HOME=/opt/keycloak  
  
RUN cd $HOME \  
&& curl -L
https://downloads.jboss.org/keycloak/$KEYCLOAK_VERSION/keycloak-$KEYCLOAK_VERSION.tar.gz
| tar xz \  
&& mv keycloak-$KEYCLOAK_VERSION $JBOSS_HOME \  
&& curl http://central.maven.org/maven2/biz/paluch/logging/logstash-
gelf/$LOGSTASH_GELF_VERSION/logstash-gelf-$LOGSTASH_GELF_VERSION-logging-
module.zip -O \  
&& unzip logstash-gelf-$LOGSTASH_GELF_VERSION-logging-module.zip \  
&& mv logstash-gelf-$LOGSTASH_GELF_VERSION/biz $JBOSS_HOME/modules/biz \  
&& rmdir logstash-gelf-$LOGSTASH_GELF_VERSION \  
&& rm logstash-gelf-$LOGSTASH_GELF_VERSION-logging-module.zip \  
&& mkdir /docker-entrypoint.d \  
&& mv $JBOSS_HOME/standalone/* /docker-entrypoint.d \  
&& cd $JBOSS_HOME \  
&& curl http://maven.dcm4che.org/org/dcm4che/dcm4che-jboss-
modules/$DCM4CHE_VERSION/dcm4che-jboss-modules-${DCM4CHE_VERSION}.tar.gz | tar
xz \  
&& chown -R keycloak:keycloak $JBOSS_HOME  
  
COPY configuration /docker-entrypoint.d/configuration  
  
COPY themes $JBOSS_HOME/themes  
  
# Default configuration: can be overridden at the docker command line  
ENV LDAP_HOST=ldap \  
LDAP_PORT=389 \  
LDAP_BASE_DN=dc=dcm4che,dc=org \  
LDAP_ROOTPASS=secret \  
KEYCLOAK_DEVICE_NAME=keycloak \  
HTTP_PORT=8080 \  
HTTPS_PORT=8443 \  
MANAGEMENT_HTTP_PORT=9990 \  
WILDFLY_ADMIN_USER=admin \  
WILDFLY_ADMIN_PASSWORD= \  
KEYCLOAK_ADMIN_USER= \  
KEYCLOAK_ADMIN_PASSWORD= \  
KEYSTORE=keycloak/key.jks \  
KEYSTORE_PASSWORD=secret \  
KEY_PASSWORD=secret \  
KEYSTORE_TYPE=JKS \  
TRUSTSTORE=keycloak/cacerts.jks \  
TRUSTSTORE_PASSWORD=secret \  
SSL_REQUIRED=external \  
REALM_NAME=dcm4che \  
SUPER_USER_ROLE=admin \  
HOSTNAME_VERIFICATION_POLICY=ANY \  
SYSLOG_HOST=logstash \  
GELF_FACILITY=keycloak \  
GELF_LEVEL=WARN \  
JAVA_OPTS="-Xms64m -Xmx512m -XX:MetaspaceSize=96M -XX:MaxMetaspaceSize=256m
-Djava.net.preferIPv4Stack=true -Djboss.modules.system.pkgs=org.jboss.byteman
-Djava.awt.headless=true"  
# Ensure signals are forwarded to the JVM process correctly for graceful
shutdown  
ENV LAUNCH_JBOSS_IN_BACKGROUND true  
  
ENV PATH $JBOSS_HOME/bin:$PATH  
  
VOLUME /opt/keycloak/standalone  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0", "-c",
"keycloak.xml", \  
"-Dkeycloak.migration.action=import",
"-Dkeycloak.migration.provider=singleFile", \  
"-Dkeycloak.migration.file=/opt/keycloak/standalone/configuration/dcm4che-
realm.json", \  
"-Dkeycloak.migration.strategy=IGNORE_EXISTING" ]  

