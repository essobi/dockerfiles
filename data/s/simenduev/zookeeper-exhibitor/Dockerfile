FROM java:alpine  
MAINTAINER Alex Simenduev <shamil.si@gmail.com>  
  
# Args for built time overrides  
ARG EXHIBITOR_VERSION="1.5.6"  
ARG MVN_VERSION="3.3.9"  
ARG ZK_VERSION="3.4.8"  
  
ENV \  
BUILD_DEPS="go git" \  
EXHIBITOR_POM="https://raw.githubusercontent.com/Netflix/exhibitor/v$EXHIBITOR_VERSION/exhibitor-
standalone/src/main/resources/buildscripts/standalone/maven/pom.xml" \  
MVN_RELEASE="http://www.apache.org/dist/maven/maven-3/$MVN_VERSION/binaries/apache-
maven-$MVN_VERSION-bin.tar.gz" \  
ZK_RELEASE="http://www.apache.org/dist/zookeeper/zookeeper-$ZK_VERSION/zookeeper-$ZK_VERSION.tar.gz"  
# Use one step so we can remove intermediate dependencies and minimize size  
RUN \  
# Install required packages  
apk add --no-cache bash fuse $BUILD_DEPS \  
# Default DNS cache TTL is -1. DNS records, like, change, man.  
&& sed -i 's/^#*\\(networkaddress.cache.ttl\\).*/\1=60/' /usr/lib/jvm/default-
jvm/jre/lib/security/java.security \  
# Alpine doesn't have /opt dir  
&& mkdir -p /opt \  
# Install ZK  
&& wget -O /tmp/zookeeper.tgz $ZK_RELEASE \  
&& tar -xvzf /tmp/zookeeper.tgz -C /opt/ \  
&& ln -s /opt/zookeeper-* /opt/zookeeper \  
&& rm /tmp/zookeeper.tgz \  
# Install maven  
&& wget -O /tmp/apache-maven.tgz $MVN_RELEASE \  
&& tar -xvzf /tmp/apache-maven.tgz -C /opt/ \  
&& ln -s /opt/apache-maven-* /opt/apache-maven \  
&& rm /tmp/apache-maven.tgz \  
# Install Exhibitor  
&& mkdir -p /opt/exhibitor \  
&& wget -O /opt/exhibitor/pom.xml $EXHIBITOR_POM \  
&& /opt/apache-maven/bin/mvn -f /opt/exhibitor/pom.xml package \  
&& ln -s /opt/exhibitor/target/exhibitor*jar /opt/exhibitor/exhibitor.jar \  
# Install gcsfuse  
&& GOPATH=/tmp/go GO15VENDOREXPERIMENT=1 go get -u
github.com/googlecloudplatform/gcsfuse \  
&& mv /tmp/go/bin/gcsfuse /usr/local/bin/ \  
&& rm -Rf /tmp/go \  
# Remove build-time dependencies  
&& apk del --no-cache $BUILD_DEPS \  
&& rm -Rf /opt/apache-maven* ~/.m2  
  
# Add the optional web.xml for authentication  
ADD include/web.xml /opt/exhibitor/web.xml  
  
# Add the wrapper script to setup configs and exec exhibitor  
ADD include/wrapper.sh /opt/exhibitor/wrapper.sh  
  
WORKDIR /opt/exhibitor  
EXPOSE 2181 2888 3888 8181  
  
ENTRYPOINT ["bash", "-ex", "/opt/exhibitor/wrapper.sh"]  

