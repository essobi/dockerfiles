FROM sonatype/nexus3:3.10.0  
ENV S3_BLOBSTORE_VERSION 1.2.1-SNAPSHOT  
ENV NEXUS_HOME /opt/sonatype/nexus  
  
USER root  
  
RUN yum update -y && yum install epel-release -y && yum install python-pip
unzip -y && pip install --upgrade pip awscli  
  
ADD https://bin.equinox.io/c/ekMN3bCZFUn/forego-stable-linux-amd64.rpm /tmp/  
RUN rpm -i /tmp/forego-stable-linux-amd64.rpm && rm -fr /tmp/forego-stable-
linux-amd64.rpm  
  
RUN \  
curl -O -L https://github.com/joshdvir/nexus-
blobstore-s3/releases/download/v0.2/nexus-blobstore-s3.zip && \  
unzip nexus-blobstore-s3.zip && \  
mkdir -p ${NEXUS_HOME}/system/org/sonatype/nexus/nexus-
blobstore-s3/${S3_BLOBSTORE_VERSION}/ && \  
mv target/* ${NEXUS_HOME}/system/org/sonatype/nexus/nexus-
blobstore-s3/${S3_BLOBSTORE_VERSION}/ && \  
rm -fr nexus-blobstore-s3.zip  
  
RUN sed -i.bak \  
-e "/nexus-blobstore-file/a\\\"$'\n'"<bundle>mvn:org.sonatype.nexus/nexus-blobstore-s3/${S3_BLOBSTORE_VERSION}</bundle>" \  
${NEXUS_HOME}/system/org/sonatype/nexus/assemblies/nexus-base-feature/*/nexus-
base-feature-*-features.xml \  
${NEXUS_HOME}/system/org/sonatype/nexus/assemblies/nexus-core-feature/*/nexus-
core-feature-*-features.xml  
  
RUN echo $'#!/bin/bash\n\  
\n\  
while true; do\n\  
aws s3 sync $DATA_FOLDER/ s3://$S3_BUCKET/ \n\  
sleep $(( 60*60*INTERVAL_IN_HOURS ))\n\  
done' > s3.sh && chmod +x s3.sh  
  
RUN echo 'nexus: /opt/sonatype/start-nexus-repository-manager.sh' > Procfile  
RUN echo 's3: ./s3.sh' >> Procfile  
  
USER nexus  
  
ENV INTERVAL_IN_HOURS=12  
CMD [ "forego", "start" ]  
  

