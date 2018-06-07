FROM alpine:3.4  
MAINTAINER Mike Babineau michael.babineau@gmail.com  
  
ARG ZK_VERSION="3.4.9"  
ARG EXHIBITOR_VERSION="1.5.6"  
ARG MAVEN_VERSION="3.3.9"  
ENV \  
MAVEN_HOME="/usr/share/maven" \  
JAVA_HOME="/usr/lib/jvm/default-jvm" \  
JAVA_PREFS="/.java/.userPrefs" \  
ZK_HOME="/opt/zookeeper" \  
EXBT_HOME="/opt/exhibitor" \  
ZK_RELEASE="https://www.apache.org/dist/zookeeper/zookeeper-$ZK_VERSION/zookeeper-$ZK_VERSION.tar.gz"
\  
EXHIBITOR_POM="https://raw.githubusercontent.com/soabase/exhibitor/v$EXHIBITOR_VERSION/exhibitor-
standalone/src/main/resources/buildscripts/standalone/maven/pom.xml" \  
BUILD_DEPS="curl openjdk8 bash tar"  
ENV PATH=${JAVA_HOME}/bin:${PATH}  
  
RUN \  
# Install Java8  
apk add \--update ${BUILD_DEPS} \  
  
# Default DNS cache TTL is -1. DNS records, like, change, man  
&& grep '^networkaddress.cache.ttl='
${JAVA_HOME}/jre/lib/security/java.security || echo
'networkaddress.cache.ttl=60' >> ${JAVA_HOME}/jre/lib/security/java.security \  
  
# Cleanup  
&& rm -rf -- /var/cache/apk/* \  
  
# Install Maven  
&& cd /usr/share \  
&& wget -q
http://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz -O - | tar xzf - \  
&& mv /usr/share/apache-maven-${MAVEN_VERSION} /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
RUN \  
mkdir -p /opt \  
  
# Install ZK  
&& curl -Lo /tmp/zookeeper.tgz ${ZK_RELEASE} \  
&& mkdir -p ${ZK_HOME}/transactions ${ZK_HOME}/snapshots \  
&& tar -xzf /tmp/zookeeper.tgz -C ${ZK_HOME} --strip-components=1 \  
&& rm /tmp/zookeeper.tgz \  
  
# Install Exhibitor  
&& mkdir -p ${EXBT_HOME} \  
&& curl -Lo ${EXBT_HOME}/pom.xml ${EXHIBITOR_POM} \  
&& mvn -f ${EXBT_HOME}/pom.xml package \  
&& ln -s ${EXBT_HOME}/target/exhibitor*jar ${EXBT_HOME}/exhibitor.jar \  
&& chown -R nobody.nobody ${ZK_HOME} ${EXBT_HOME}  
  
# Add the wrapper script to setup configs and exec exhibitor  
ADD include/wrapper.sh ${EXBT_HOME}/wrapper.sh  
  
# Add the optional web.xml for authentication  
ADD include/web.xml ${EXBT_HOME}/web.xml  
  
# To store Java preferences  
RUN mkdir -p ${JAVA_PREFS}  
RUN chown -R nobody.nobody ${JAVA_PREFS}  
  
USER nobody  
WORKDIR /opt/exhibitor  
EXPOSE 2181 2888 3888 8181  
ENTRYPOINT ["bash", "-ex", "/opt/exhibitor/wrapper.sh"]  

