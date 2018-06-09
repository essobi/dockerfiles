FROM java:8  
MAINTAINER Ian Buchanan <ibuchanan@atlassian.com>  
  
# Install dependencies  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -yq libc6:i386 libstdc++6:i386 zlib1g:i386 libncurses5:i386
--no-install-recommends && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Ant  
ENV ANT_VERSION=1.9.6  
RUN cd && \  
mkdir -p /opt/ant && \  
curl http://archive.apache.org/dist/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz | tar --no-same-owner -xz --strip 1 --directory
/opt/ant  
ENV ANT_HOME=/opt/ant \  
PATH=${PATH}:/opt/ant/bin  
  
# Intall TestFairy Uploader CLI  
ENV TFU_VERSION=1.1.6  
RUN cd && \  
mkdir -p /opt/testfairy-uploader && \  
curl -LO https://github.com/testfairy/testfairy-uploader-
cli/releases/download/${TFU_VERSION}/testfairy-uploader-${TFU_VERSION}.zip &&
\  
unzip testfairy-uploader-${TFU_VERSION}.zip -d /opt/testfairy-uploader && \  
rm testfairy-uploader-${TFU_VERSION}.zip  
ENV PATH=${PATH}:/opt/testfairy-uploader  
  
# Download and untar Android SDK  
ENV ANDROID_SDK_VERSION=24.4.1  
RUN cd && \  
mkdir -p /opt/android-sdk && \  
curl http://dl.google.com/android/android-
sdk_r${ANDROID_SDK_VERSION}-linux.tgz | tar --no-same-owner -xz --strip 1
--directory /opt/android-sdk  
ENV ANDROID_HOME=/opt/android-sdk \  
ANDROID_SDK=/opt/android-sdk \  
PATH=${PATH}:/opt/android-sdk/tools:/opt/android-sdk/platform-tools  
  
# Support Gradle  
ENV TERM=dumb  
  
RUN mkdir -p /opt/atlassian/bitbucketci/agent/build  
WORKDIR /opt/atlassian/bitbucketci/agent/build  
ENTRYPOINT /bin/bash  

