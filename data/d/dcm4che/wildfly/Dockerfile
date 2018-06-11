FROM openjdk:8-jre  
  
# explicitly set user/group IDs  
RUN groupadd -r wildfly --gid=1023 && useradd -r -g wildfly --uid=1023 -d
/opt/wildfly wildfly  
  
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
  
ENV WILDFLY_VERSION=12.0.0.Final \  
KEYCLOAK_VERSION=3.4.3.Final \  
LOGSTASH_GELF_VERSION=1.11.2 \  
JBOSS_HOME=/opt/wildfly  
  
ENV JBOSS_LOGMANAGER_JAR=jboss-logmanager-
ext-${JBOSS_LOGMANAGER_EXT_VERSION}.jar  
RUN cd $HOME \  
&& curl
https://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
| tar xz \  
&& mv wildfly-$WILDFLY_VERSION $JBOSS_HOME \  
&& curl
http://downloads.jboss.org/keycloak/$KEYCLOAK_VERSION/adapters/keycloak-
oidc/keycloak-wildfly-adapter-dist-$KEYCLOAK_VERSION.tar.gz | tar xz -C
$JBOSS_HOME \  
&& curl http://central.maven.org/maven2/biz/paluch/logging/logstash-
gelf/$LOGSTASH_GELF_VERSION/logstash-gelf-$LOGSTASH_GELF_VERSION-logging-
module.zip -O \  
&& unzip logstash-gelf-$LOGSTASH_GELF_VERSION-logging-module.zip \  
&& mv logstash-gelf-$LOGSTASH_GELF_VERSION/biz $JBOSS_HOME/modules/biz \  
&& rmdir logstash-gelf-$LOGSTASH_GELF_VERSION \  
&& rm logstash-gelf-$LOGSTASH_GELF_VERSION-logging-module.zip \  
&& mkdir /docker-entrypoint.d && mv $JBOSS_HOME/standalone/* /docker-
entrypoint.d \  
&& chown wildfly $JBOSS_HOME  
  
# Default configuration: can be overridden at the docker command line  
ENV WILDFLY_ADMIN_USER= \  
WILDFLY_ADMIN_PASSWORD= \  
JAVA_OPTS="-Xms64m -Xmx512m -XX:MetaspaceSize=96M -XX:MaxMetaspaceSize=256m
-Djava.net.preferIPv4Stack=true -Djboss.modules.system.pkgs=org.jboss.byteman
-Djava.awt.headless=true"  
ENV WILDFLY_STANDALONE configuration deployments  
ENV WILDFLY_INIT=  
ENV WILDFLY_CHOWN $JBOSS_HOME/standalone  
  
# Ensure signals are forwarded to the JVM process correctly for graceful
shutdown  
ENV LAUNCH_JBOSS_IN_BACKGROUND true  
  
ENV PATH $JBOSS_HOME/bin:$PATH  
  
VOLUME /opt/wildfly/standalone  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]  

