FROM acosix/baseimage-tomcat7:latest  
  
LABEL vendor="Acosix GmbH" \  
de.acosix.version="0.0.1-SNAPSHOT" \  
de.acosix.is-beta="" \  
de.acosix.is-production="" \  
de.acosix.release-date="2017-09-01" \  
de.acosix.maintainer="axel.faust@acosix.de"  
  
ENV MAVEN_REQUIRED_ARTIFACTS= \  
ALFRESCO_PLATFORM_VERSION=5.2.g \  
ALFRESCO_AOS_VERSION=1.1.6 \  
ALFRESCO_VTI_BIN_VERSION=1.1.5 \  
ALFRESCO_SHARE_SERVICES_VERSION=5.2.f \  
ALFRESCO_PLATFORM_WAR_ARTIFACT= \  
ALFRESCO_PLATFORM_ROOT_WAR_ARTIFACT= \  
MAVEN_ACTIVE_REPOSITORIES=acosix,alfresco,alfresco_ee,central,ossrh \  
MAVEN_REPOSITORIES_central_URL=https://repo1.maven.org/maven2 \  
MAVEN_REPOSITORIES_alfresco_URL=https://artifacts.alfresco.com/nexus/content/groups/public
\  
MAVEN_REPOSITORIES_alfresco_ee_URL=https://artifacts.alfresco.com/nexus/content/groups/private
\  
MAVEN_REPOSITORIES_acosix_URL=https://acosix.de/nexus/content/groups/public \  
MAVEN_REPOSITORIES_ossrh_URL=https://oss.sonatype.org/content/repositories/snapshots
\  
JMX_RMI_PORT=5001  
# Public HTTP ports for reverse-proxy: 8080 / 8081 (assumed secured via SSL)  
# Private HTTP ports for SOLR: 8082 / 8083 (active SSL)  
# JMX / RMI port: 5001 (aligned with SOLR + Share images so that each havea a
distinct port - it's hard to forward JMX / RMI otherwise due JVM having to
know the public port you're exposing via Docker)  
# Various protocol ports: 10025 (inboundSMTP) / 10445,10137-10139 (CIFS/SMB) /
10021 FTP (active) / 11000-11099 FTP (passive)  
EXPOSE 8080 8081 8082 8083 5001 10445 10137-10139 10025 10021 11000-11099  
  
VOLUME ["/srv/alfresco/data", "/srv/alfresco/keystore",
"/srv/alfresco/defaultArtifacts"]  
  
# Add common JDBC drivers  
# We need (temporary) wget support to download  
# (We could just as easily have used ADD, but since we need to unzip the MySQL
download and want to avoid two additional layers, we do this via a single RUN)  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update -q \  
&& apt-get upgrade -q -y -o Dpkg::Options::="--force-confdef" -o
Dpkg::Options::="--force-confold" \  
&& apt-get install -q -y -o Dpkg::Options::="--force-confdef" -o
Dpkg::Options::="--force-confold" \  
wget \  
&& wget -P /var/lib/tomcat7/shared
https://jdbc.postgresql.org/download/postgresql-42.1.1.jar \  
&& wget -P /var/lib/tomcat7/shared
https://downloads.mariadb.com/Connectors/java/connector-java-2.0.1/mariadb-
java-client-2.0.1.jar \  
&& wget -P /var/lib/tomcat7/shared
https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.42.zip \  
&& unzip /var/lib/tomcat7/shared/mysql-connector-java-5.1.42.zip mysql-
connector-java-5.1.42/mysql-connector-java-5.1.42-bin.jar -d
/var/lib/tomcat7/shared \  
&& rm /var/lib/tomcat7/shared/mysql-connector-java-5.1.42.zip \  
&& apt-get autoremove -q -y \  
wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# add prepared files that would be too awkward to handle via RUN / sed  
COPY alfresco-logrotate.d initAlfresco.sh prepareWarFiles.js shared-classes
/tmp/  
  
# apply our Alfresco Repository default configurations  
RUN mv /tmp/alfresco-logrotate.d /etc/logrotate.d/alfresco \  
&& touch /var/lib/tomcat7/logs/.alfresco-logrotate-dummy \  
&& mv /tmp/alfresco /var/lib/tomcat7/shared/classes/ \  
&& mv /tmp/alfresco-global.properties /var/lib/tomcat7/shared/classes/ \  
&& mv /tmp/prepareWarFiles.js /var/lib/tomcat7/ \  
&& mv /tmp/initAlfresco.sh /etc/my_init.d/50_initAlfresco.sh \  
&& chmod +x /etc/my_init.d/50_initAlfresco.sh

