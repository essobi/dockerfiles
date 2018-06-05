FROM maven:3.5.2-jdk-8-alpine as builder  
  
WORKDIR /build  
RUN apk update \  
&& apk upgrade \  
&& apk add --no-cache git \  
&& git clone https://github.com/sonatype/nexus-blobstore-s3.git \  
&& cd nexus-blobstore-s3 \  
&& git checkout 7df0429580c910292df112ba22a16294467924a3 \  
&& mvn install  
  
FROM sonatype/nexus3:3.8.0  
LABEL maintainer "Hiroyuki Wada <wadahiro@gmail.com>"  
  
ENV S3_BLOBSTORE_VERSION 1.2.1-SNAPSHOT  
ENV NEXUS_HOME /opt/sonatype/nexus  
  
COPY \--from=builder /build/nexus-blobstore-s3/target/nexus-
blobstore-s3-${S3_BLOBSTORE_VERSION}.jar
${NEXUS_HOME}/system/org/sonatype/nexus/nexus-
blobstore-s3/${S3_BLOBSTORE_VERSION}/  
  
USER root  
  
RUN sed -i.bak \  
-e "/nexus-blobstore-file/a\\\"$'\n'"<bundle>mvn:org.sonatype.nexus/nexus-blobstore-s3/${S3_BLOBSTORE_VERSION}</bundle>" \  
${NEXUS_HOME}/system/org/sonatype/nexus/assemblies/nexus-base-feature/*/nexus-
base-feature-*-features.xml \  
${NEXUS_HOME}/system/org/sonatype/nexus/assemblies/nexus-core-feature/*/nexus-
core-feature-*-features.xml  
  
# RUN yum -y update && yum install -y python-setuptools && easy_install pip &&
pip install awscli  
USER nexus  
  

