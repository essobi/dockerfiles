# Glibc is required so we use alpine image that has glibc baked in.  
# https://github.com/frol/docker-alpine-glibc  
FROM frolvlad/alpine-glibc:alpine-3.7  
  
ENV ANDROID_APIS="android-27" \  
ANDROID_BUILD_TOOLS_VERSION=27.0.3 \  
ANDROID_HOME="/opt/android" \  
ANDROID_SDK_URL="https://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip"  
  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:${ANDROID_HOME}/build-tools/${ANDROID_BUILD_TOOLS_VERSION}  
  
COPY requirements.txt .  
  
RUN apk add --no-cache --update \  
bash \  
ca-certificates \  
curl \  
gcc \  
git \  
expect \  
libstdc++ \  
libffi \  
libffi-dev \  
openssl-dev \  
openjdk8 \  
python2 \  
python2-dev \  
py-pip \  
# Install mailcap for mimetypes. Without this packet gplay deployments will
fail  
# because of missing apk mimetype.  
mailcap \  
musl-dev \  
unzip && \  
# Update to latest pip & Install Python pip packets from requirements.txt  
pip install --upgrade pip && \  
pip install --upgrade --requirement requirements.txt && \  
rm -rf /tmp/* /var/tmp/*  
  
# Install sdk tools  
RUN mkdir -p ${ANDROID_HOME} && \  
curl -o sdk-tools.zip ${ANDROID_SDK_URL} && \  
unzip sdk-tools.zip -d ${ANDROID_HOME} && \  
rm sdk-tools.zip && \  
yes | ${ANDROID_HOME}/tools/bin/sdkmanager --licenses  
  
# Install sdk with sdk manager  
RUN ${ANDROID_HOME}/tools/bin/sdkmanager \  
"platform-tools" \  
"platforms;${ANDROID_APIS}" \  
"build-tools;${ANDROID_BUILD_TOOLS_VERSION}" \  
"extras;android;m2repository"  
# Setup environment.  
ENV JAVA_HOME="/usr/lib/jvm/java-1.8-openjdk"  
# Go to workspace.  
WORKDIR /opt/workspace  

