FROM acosix/baseimage-tomcat7:latest  
  
LABEL vendor="Acosix GmbH" \  
de.acosix.version="0.0.1-SNAPSHOT" \  
de.acosix.is-beta="" \  
de.acosix.is-production="" \  
de.acosix.release-date="2017-06-29" \  
de.acosix.maintainer="axel.faust@acosix.de"  
  
ENV MAVEN_REQUIRED_ARTIFACTS= \  
ALFRESCO_SOLR4_VERSION=5.2.f \  
ALFRESCO_SOLR4_WAR_ARTIFACT= \  
ALFRESCO_SOLR4_CONFIG_ZIP_ARTIFACT= \  
MAVEN_ACTIVE_REPOSITORIES=acosix,alfresco,alfresco_ee,central,ossrh \  
MAVEN_REPOSITORIES_central_URL=https://repo1.maven.org/maven2 \  
MAVEN_REPOSITORIES_alfresco_URL=https://artifacts.alfresco.com/nexus/content/groups/public
\  
MAVEN_REPOSITORIES_alfresco_ee_URL=https://artifacts.alfresco.com/nexus/content/groups/private
\  
MAVEN_REPOSITORIES_acosix_URL=https://acosix.de/nexus/content/groups/public \  
MAVEN_REPOSITORIES_ossrh_URL=https://oss.sonatype.org/content/repositories/snapshots
\  
JMX_RMI_PORT=5003  
  
EXPOSE 8080 8081 8082 8083 5003  
# having SOLR core configurations in an externalised volume is optional -
index is expected to be always externalised  
VOLUME ["/srv/alfresco-solr4/index", "/srv/alfresco-solr4/coreConfigs",
"/srv/alfresco-solr4/keystore", "/srv/alfresco-solr4/defaultArtifacts"]  
  
# add prepared files that would be too awkward to handle via RUN / sed  
COPY initSolr4.sh solr4-logrotate.d prepareSolr4Files.js /tmp/  
COPY defaultKeystore /tmp/defaultKeystore/  
  
# apply our SOLR 4 default configurations  
RUN mv /tmp/solr4-logrotate.d /etc/logrotate.d/alfresco-solr4 \  
&& touch /var/lib/tomcat7/logs/.solr4-logrotate-dummy \  
&& mv /tmp/prepareSolr4Files.js /var/lib/tomcat7/ \  
&& mv /tmp/initSolr4.sh /etc/my_init.d/50_initSolr4.sh \  
&& chmod +x /etc/my_init.d/50_initSolr4.sh \  
&& mkdir -p /srv/alfresco-solr4 \  
&& mv /tmp/defaultKeystore /srv/alfresco-solr4/ \  
&& chmod 600 /srv/alfresco-solr4/defaultKeystore/* \  
&& chown -R tomcat7:tomcat7 /srv/alfresco-solr4/defaultKeystore

