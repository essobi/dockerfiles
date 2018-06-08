FROM nearpod/alpine-jvm:3.7-jdk8  
  
ARG CONFLUENT_VERSION="3.3.1"  
ARG MAVEN_VERSION=3.5.2  
ARG KAFKA_USER=kafka  
  
ENV KAFKA_USER=$KAFKA_USER  
ENV PATH=$PATH:$KAFKA_HOME/bin  
  
RUN set -ex; \  
WORKDIR="$PWD"; \  
apk --no-cache add gnupg; \  
PATH=$PATH:/opt/maven/bin; \  
mkdir -p /opt/maven; \  
curl -q -sSLO
"http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz"; \  
curl -q -sSLO
"http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz.asc"; \  
curl -q -sSLO "http://archive.apache.org/dist/maven/KEYS"; \  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --import KEYS; \  
gpg --batch --verify "apache-maven-$MAVEN_VERSION-bin.tar.gz.asc" "apache-
maven-$MAVEN_VERSION-bin.tar.gz"; \  
mkdir -p /opt/maven; \  
tar -xzf "apache-maven-$MAVEN_VERSION-bin.tar.gz" \--strip-components=1 -C
/opt/maven; \  
mvn --version; \  
\  
mkdir -p /opt/src/common; cd /opt/src/common; \  
curl -q -sSL
"https://github.com/confluentinc/common/archive/v$CONFLUENT_VERSION.tar.gz" |
tar -xzf - --strip-components=1 -C ./; \  
mvn install -Dmaven.test.skip=true; \  
mkdir -p /opt/src/rest-utils; cd /opt/src/rest-utils; \  
curl -q -sSL "https://github.com/confluentinc/rest-
utils/archive/v$CONFLUENT_VERSION.tar.gz" | tar -xzf - --strip-components=1 -C
./; \  
mvn install -Dmaven.test.skip=true; \  
mkdir -p /opt/src/kafka-rest; cd /opt/src/kafka-rest; \  
curl -q -sSL "https://github.com/confluentinc/kafka-
rest/archive/v$CONFLUENT_VERSION.tar.gz" | tar -xzf - --strip-components=1 -C
./; \  
mvn install -Dmaven.test.skip=true; \  
\  
cd $WORKDIR; \  
mkdir -p $WORKDIR/share/java; \  
mv /opt/src/common/package/target/common-package-$CONFLUENT_VERSION-
package/share/java/confluent-common ./share/java/; \  
mv /opt/src/rest-utils/package/target/rest-utils-package-$CONFLUENT_VERSION-
package/share/java/rest-utils ./share/java/; \  
mv /opt/src/kafka-rest/target/kafka-rest-$CONFLUENT_VERSION-package/bin/*
./bin/; \  
mv /opt/src/kafka-rest/target/kafka-rest-$CONFLUENT_VERSION-
package/share/java/* ./share/java/; \  
mv /opt/src/kafka-rest/target/kafka-rest-$CONFLUENT_VERSION-package/etc/*
/etc; \  
rm -rf "$GNUPGHOME" "apache-maven-$MAVEN_VERSION-bin.tar.gz" "apache-
maven-$MAVEN_VERSION-bin.tar.gz.asc" KEYS /root/.m2 /opt/maven /opt/src; \  
apk del gnupg;  
  
RUN set -ex; \  
WORKDIR="$PWD"; \  
addgroup -g 1000 "$KAFKA_USER"; \  
adduser -D -h "$WORKDIR" -u 1000 -G "$KAFKA_USER" "$KAFKA_USER"; \  
[ `id -u "$KAFKA_USER"` -eq 1000 ]; \  
[ `id -g "$KAFKA_USER"` -eq 1000 ]  
  
USER kafka:kafka  

