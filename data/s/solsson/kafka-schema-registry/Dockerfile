FROM solsson/kafka-
jre@sha256:7765513cf5fa455a672a06f584058c1c81cc0b3b56cc56b0cfdf1a917a183f26  
  
ENV CP_VERSION=v3.3.0  
  
RUN set -ex; \  
export DEBIAN_FRONTEND=noninteractive; \  
runDeps=''; \  
buildDeps='curl ca-certificates'; \  
apt-get update && apt-get install -y $runDeps $buildDeps --no-install-
recommends; \  
\  
MAVEN_VERSION=3.5.0 PATH=$PATH:/opt/maven/bin; \  
mkdir -p /opt/maven; \  
curl -SLs
https://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar -xzf - --strip-components=1 -C
/opt/maven; \  
mvn --version; \  
\  
mkdir -p /opt/src/common; cd /opt/src/common; \  
curl -SLs https://github.com/confluentinc/common/archive/$CP_VERSION.tar.gz |
tar -xzf - --strip-components=1 -C ./; \  
mvn install; \  
\  
mkdir -p /opt/src/rest-utils; cd /opt/src/rest-utils; \  
curl -SLs https://github.com/confluentinc/rest-
utils/archive/$CP_VERSION.tar.gz | tar -xzf - --strip-components=1 -C ./; \  
mvn install; \  
\  
mkdir -p /opt/src/schema-registry; cd /opt/src/schema-registry; \  
curl -SLs https://github.com/confluentinc/schema-
registry/archive/$CP_VERSION.tar.gz | tar -xzf - --strip-components=1 -C ./; \  
mvn install; \  
\  
mv /opt/src/schema-registry/package-schema-registry/target/kafka-schema-
registry-package-3.3.0-package /opt/schema-registry; \  
mv /opt/src/common/package/target/common-
package-3.3.0-package/share/java/confluent-common /opt/schema-
registry/share/java/; \  
mv /opt/src/rest-utils/package/target/rest-utils-
package-3.3.0-package/share/java/rest-utils /opt/schema-registry/share/java/;
\  
\  
rm -Rf /opt/src /opt/maven /root/.m2; \  
\  
apt-get purge -y --auto-remove $buildDeps; \  
rm -rf /var/lib/apt/lists/*; \  
rm -rf /var/log/dpkg.log /var/log/alternatives.log /var/log/apt  
  
WORKDIR /opt/schema-registry  
  
ENTRYPOINT ["./bin/schema-registry-start"]  
CMD ["./etc/schema-registry/schema-registry.properties"]  

