FROM alpine:3.6  
MAINTAINER Rom Luengwattanapong <s1567783@ed.ac.uk>  
  
USER root  
  
# Installs bash and php for run script  
RUN apk --no-cache upgrade \  
&& apk --no-cache add \  
bash \  
coreutils \  
php7 \  
php7-posix \  
php7-json  
  
# Installs Dependencies  
RUN apk --no-cache add --virtual .build-dependencies \  
ca-certificates \  
curl \  
git \  
openssl \  
tar \  
unzip \  
wget  
  
# Installs OpenJDK-8  
RUN apk --no-cache add openjdk8-jre  
RUN apk --no-cache add openjdk8  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk  
  
# Installs Android SDKs  
# Modified from https://hub.docker.com/r/bwits/android-sdk-alpine/  
ENV ANDROID_SDK_FILENAME tools_r25.2.3-linux.zip  
ENV ANDROID_SDK_URL
https://dl.google.com/android/repository/${ANDROID_SDK_FILENAME}  
ENV ANDROID_API_LEVELS
android-1,android-2,android-3,android-4,android-5,android-6,android-7,android-8,android-9,android-10,android-11,android-12,android-13,android-14,android-15,android-16,android-17,android-18,android-19,android-20,android-21,android-22,android-23,android-24,android-25  
ENV ANDROID_BUILD_TOOLS_VERSION 26.0.0  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
RUN mkdir -p /opt \  
&& cd /opt \  
&& wget ${ANDROID_SDK_URL} \  
&& unzip ${ANDROID_SDK_FILENAME} -d "${ANDROID_HOME}" \  
&& rm ${ANDROID_SDK_FILENAME} \  
&& echo y | android update sdk --no-ui --all --filter tools,platform-
tools,${ANDROID_API_LEVELS},build-tools-${ANDROID_BUILD_TOOLS_VERSION} \  
&& chown -R 1000:1000 $ANDROID_HOME  
  
# Downloads FlowDroid and required software  
ENV FLOWDROIDPATH /opt/flowdroid  
ENV PATH ${FLOWDROIDPATH}:$PATH  
  
RUN mkdir -p ${FLOWDROIDPATH}/ \  
&& curl -L http://soot-build.cs.uni-paderborn.de/nightly/soot/soot-trunk.jar
--output ${FLOWDROIDPATH}/soot-trunk.jar \  
&& curl -L https://github.com/secure-software-engineering/soot-
infoflow/releases/download/FlowDroid_1.5/soot-infoflow.jar --output
${FLOWDROIDPATH}/soot-infoflow.jar \  
&& curl -L https://github.com/secure-software-engineering/soot-infoflow-
android/releases/download/FlowDroid_1.5/soot-infoflow-android.jar --output
${FLOWDROIDPATH}/soot-infoflow-android.jar \  
&& curl -L https://github.com/secure-software-engineering/soot-infoflow-
android/raw/develop/lib/slf4j-api-1.7.5.jar --output
${FLOWDROIDPATH}/slf4j-api-1.7.5.jar \  
&& curl -L https://github.com/secure-software-engineering/soot-infoflow-
android/raw/develop/lib/slf4j-simple-1.7.5.jar --output
${FLOWDROIDPATH}/slf4j-simple-1.7.5.jar \  
&& curl -L https://github.com/secure-software-engineering/soot-infoflow-
android/raw/develop/lib/axml-2.0.jar --output ${FLOWDROIDPATH}/axml-2.0.jar \  
  
&& curl -L https://github.com/secure-software-engineering/soot-infoflow-
android/raw/develop/SourcesAndSinks.txt --output
${FLOWDROIDPATH}/SourcesAndSinks.txt \  
&& curl -L https://github.com/secure-software-engineering/soot-
infoflow/raw/develop/EasyTaintWrapperSource.txt --output
${FLOWDROIDPATH}/EasyTaintWrapperSource.txt \  
&& curl -L https://github.com/secure-software-engineering/soot-infoflow-
android/raw/develop/AndroidCallbacks.txt --output
${FLOWDROIDPATH}/AndroidCallbacks.txt \  
  
&& cd ${FLOWDROIDPATH} \  
&& chmod +x *  
  
# Cleans up  
RUN apk del .build-dependencies\  
&& rm -rf /tmp/* /var/tmp/*  
  
# Create application folder  
RUN mkdir -p /app  
  
VOLUME ["/app"]  
  
COPY run.php /tmp/  
RUN chmod +x /tmp/run.php  
  
WORKDIR /tmp  
  
ENTRYPOINT ["/usr/bin/php", "/tmp/run.php"]  

