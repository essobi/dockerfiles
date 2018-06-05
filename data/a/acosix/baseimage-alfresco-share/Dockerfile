FROM acosix/baseimage-tomcat7:latest  
  
LABEL vendor="Acosix GmbH" \  
de.acosix.version="0.0.1-SNAPSHOT" \  
de.acosix.is-beta="" \  
de.acosix.is-production="" \  
de.acosix.release-date="2017-08-13" \  
de.acosix.maintainer="axel.faust@acosix.de"  
  
ENV MAVEN_REQUIRED_ARTIFACTS= \  
ALFRESCO_PLATFORM_VERSION=5.2.g \  
ALFRESCO_SHARE_VERSION=5.2.g \  
MAVEN_ACTIVE_REPOSITORIES=acosix,alfresco,alfresco_ee,central,ossrh \  
MAVEN_REPOSITORIES_central_URL=https://repo1.maven.org/maven2 \  
MAVEN_REPOSITORIES_alfresco_URL=https://artifacts.alfresco.com/nexus/content/groups/public
\  
MAVEN_REPOSITORIES_alfresco_ee_URL=https://artifacts.alfresco.com/nexus/content/groups/private
\  
MAVEN_REPOSITORIES_acosix_URL=https://acosix.de/nexus/content/groups/public \  
MAVEN_REPOSITORIES_ossrh_URL=https://oss.sonatype.org/content/repositories/snapshots
\  
JMX_RMI_PORT=5002  
  
EXPOSE 8080 8081 5002  
  
VOLUME ["/srv/alfresco/keystore", "/srv/alfresco/defaultArtifacts"]  
  
# add prepared files that would be too awkward to handle via RUN / sed  
COPY share-global.properties share-config-custom.xml dev-log4j.properties
share-logrotate.d initShare.sh prepareWarFiles.js /tmp/  
  
# apply our Alfresco Repository default configurations  
RUN mv /tmp/share-logrotate.d /etc/logrotate.d/share \  
&& mkdir -p /var/lib/tomcat7/shared/classes/alfresco/web-extension \  
&& mv /tmp/dev-log4j.properties /var/lib/tomcat7/shared/classes/alfresco/web-
extension/ \  
&& mv /tmp/share-config-custom.xml
/var/lib/tomcat7/shared/classes/alfresco/web-extension/ \  
&& touch /var/lib/tomcat7/logs/.share-logrotate-dummy \  
&& mv /tmp/share-global.properties /var/lib/tomcat7/shared/classes/ \  
&& mv /tmp/prepareWarFiles.js /var/lib/tomcat7/ \  
&& mv /tmp/initShare.sh /etc/my_init.d/50_initShare.sh \  
&& chmod +x /etc/my_init.d/50_initShare.sh

