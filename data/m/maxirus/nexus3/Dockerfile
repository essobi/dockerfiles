FROM maven:3.5.2-jdk-8-alpine as s3-blobstore  
  
RUN apk --update add --no-cache --virtual .build-deps \  
unzip \  
wget && \  
wget --quiet https://github.com/sonatype/nexus-
blobstore-s3/archive/a5ccb438babb35572e9d2042afc71931c2f19078.zip -O
/tmp/nexus-blobstore-s3.zip && \  
unzip /tmp/nexus-blobstore-s3.zip -d /tmp && \  
mv /tmp/nexus-blobstore-s3-* /tmp/nexus-blobstore-s3 && \  
cd /tmp/nexus-blobstore-s3 && \  
mvn clean install && \  
PROJ_VERSION=$(mvn -q \  
-Dexec.executable="echo" \  
-Dexec.args='${project.version}' \  
\--non-recursive \  
org.codehaus.mojo:exec-maven-plugin:1.3.1:exec) && \  
echo "$PROJ_VERSION" > version  
  
FROM maxirus/nexus3:3.8.0-alpine  
  
## Install Blobstore plugin ##  
USER root  
COPY \--from=s3-blobstore /tmp/nexus-blobstore-s3/version /tmp/  
COPY \--from=s3-blobstore /tmp/nexus-blobstore-s3/target/nexus-
blobstore-s3-*.jar /tmp/nexus-blobstore-s3/  
RUN S3_BLOBSTORE_VERSION=$(cat /tmp/version) && \  
mkdir -p ${NEXUS_HOME}/system/org/sonatype/nexus/nexus-
blobstore-s3/${S3_BLOBSTORE_VERSION}/ && \  
mv /tmp/nexus-blobstore-s3/nexus-blobstore-s3-*.jar
${NEXUS_HOME}/system/org/sonatype/nexus/nexus-
blobstore-s3/${S3_BLOBSTORE_VERSION}/ && \  
sed -i.bak -e "/nexus-blobstore-
file/a\\\"$'\n'"<bundle>mvn:org.sonatype.nexus/nexus-
blobstore-s3/${S3_BLOBSTORE_VERSION}</bundle>"
${NEXUS_HOME}/system/org/sonatype/nexus/assemblies/nexus-base-feature/*/nexus-
base-feature-*-features.xml && \  
sed -i.bak -e "/nexus-blobstore-
file/a\\\"$'\n'"<bundle>mvn:org.sonatype.nexus/nexus-
blobstore-s3/${S3_BLOBSTORE_VERSION}</bundle>"
${NEXUS_HOME}/system/org/sonatype/nexus/assemblies/nexus-core-feature/*/nexus-
core-feature-*-features.xml  
  
USER nexus

