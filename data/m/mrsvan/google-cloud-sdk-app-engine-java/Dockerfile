FROM openjdk:8-jdk-alpine  
  
MAINTAINER Stefaan Vanderheyden <svd@nuuvo.mobi>  
ARG CLOUD_SDK_VERSION=194.0.0  
ARG SHA256SUM=bc8128569b8c1c4f53512f95bce66efedec60ab6f877f39472373b4e610ab09c  
ENV PATH /google-cloud-sdk/bin:$PATH  
ENV MAVEN_VERSION="3.5.3" \  
M2_HOME=/root/.m2/  
RUN sed -i 's/http\:\/\/dl-
cdn.alpinelinux.org/https\:\/\/alpine.global.ssl.fastly.net/g'
/etc/apk/repositories && \  
apk add --update wget && \  
cd /tmp && \  
wget "https://repo.maven.apache.org/maven2/org/apache/maven/apache-
maven/$MAVEN_VERSION/apache-maven-$MAVEN_VERSION-bin.tar.gz" && \  
tar -zxvf "apache-maven-$MAVEN_VERSION-bin.tar.gz" && \  
mv "apache-maven-$MAVEN_VERSION" "$M2_HOME" && \  
ln -s "$M2_HOME/bin/mvn" /usr/bin/mvn && \  
apk del wget && \  
apk add git curl tar python bash procps && \  
echo "Add jq for parsing GitLab API responses" && \  
apk add jq && \  
rm /tmp/* /var/cache/apk/* && \  
curl -L -o crcmod.tar.gz
"https://downloads.sourceforge.net/project/crcmod/crcmod/crcmod-1.7/crcmod-1.7.tar.gz"
&& \  
tar -xzf crcmod.tar.gz && \  
cd crcmod-1.7/ && \  
python setup.py install && \  
cd / && \  
curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-
cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
echo "${SHA256SUM} google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz"
> google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz.sha256 && \  
sha256sum -c google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz.sha256
&& \  
tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \  
rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz google-cloud-
sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz.sha256 && \  
ln -s /lib /lib64 && \  
gcloud config set core/disable_usage_reporting true && \  
gcloud config set component_manager/disable_update_check true && \  
gcloud config set metrics/environment github_docker_image && \  
gcloud components install app-engine-java  

