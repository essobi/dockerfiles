FROM sonatype/nexus3:3.10.0  
  
ARG NEXUS_VERSION=3.10.0-04  
ARG
NEXUS_FEATURES_FILE=/opt/sonatype/nexus/system/org/sonatype/nexus/assemblies/nexus-
core-feature/${NEXUS_VERSION}/nexus-core-feature-${NEXUS_VERSION}-features.xml  
ARG NEXUS_APT_DIR=/opt/sonatype/nexus/system/net/staticsnow/nexus-repository-
apt/1.0.5/  
ARG
NEXUS_KEYCLOAK_DIR=/opt/sonatype/nexus/system/org/github/flytreeleft/nexus3-keycloak-
plugin/0.2.0/  
  
USER root  
RUN \  
mkdir -p ${NEXUS_APT_DIR}; \  
sed -i 's@nexus-repository-maven</feature>@nexus-repository-maven</feature>\n
<feature prerequisite="false" dependency="false" version="1.0.5">nexus-
repository-apt</feature>@g' ${NEXUS_FEATURES_FILE}; \  
sed -i 's@<feature name="nexus-repository-maven"@<feature name="nexus-
repository-apt" description="net.staticsnow:nexus-repository-apt"
version="1.0.5">\n <details>net.staticsnow:nexus-repository-apt</details>\n
<bundle>mvn:net.staticsnow/nexus-repository-apt/1.0.5</bundle>\n
<bundle>mvn:org.apache.commons/commons-compress/1.11</bundle>\n </feature>\n
<feature name="nexus-repository-maven"@g' ${NEXUS_FEATURES_FILE};  
COPY nexus-repository-apt-1.0.5.jar ${NEXUS_APT_DIR}  
RUN \  
mkdir -p ${NEXUS_KEYCLOAK_DIR}; \  
sed '$areference\\\:file\\\:org/github/flytreeleft/nexus3-keycloak-
plugin/0.2.0/nexus3-keycloak-plugin-0.2.0.jar = 200'
/opt/sonatype/nexus/etc/karaf/startup.properties;  
COPY nexus3-keycloak-plugin-0.2.0.jar ${NEXUS_KEYCLOAK_DIR}  
USER nexus  

