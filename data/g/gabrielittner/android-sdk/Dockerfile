FROM openjdk:8-jdk-alpine  
  
LABEL maintainer="gabriel.ittner@gmail.com"  
  
# Install dependencies  
# git and openssh-client for CircleCI  
# glibc from https://github.com/sgerrand/alpine-pkg-
glibc/issues/1#issuecomment-251170697  
RUN apk --no-cache add ca-certificates git openssh-client && \  
wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
apk --no-cache -X https://apkproxy.herokuapp.com/sgerrand/alpine-pkg-glibc add
glibc glibc-bin && \  
rm -f /etc/apk/keys/sgerrand.rsa.pub  
  
# Create new user  
ARG username=worker  
RUN addgroup ${username} && \  
adduser -D -G ${username} ${username}  
USER ${username}  
  
# Android SDK location  
ARG android_home=/home/${username}/android-sdk  
  
# Accept Android SDK licenses  
ARG sdk_license="d56f5187479451eabf01fb78af6dfcb131a6481e"  
ARG sdk_license_preview="84831b9409646a918e30573bab4c9c91346d8abd"  
RUN mkdir -p "${android_home}/licenses" && \  
echo ${sdk_license} > "${android_home}/licenses/android-sdk-license" && \  
echo ${sdk_license_preview} > "${android_home}/licenses/android-sdk-preview-
license"  
  
# Download and install Android SDK  
ARG sdk_version=sdk-tools-linux-4333796.zip  
RUN mkdir -p ${android_home} && \  
wget -q -O /tmp/${sdk_version}
https://dl.google.com/android/repository/${sdk_version} && \  
unzip -q /tmp/${sdk_version} -d ${android_home} && \  
rm /tmp/${sdk_version}  
  
# Set environmental variables  
ENV ANDROID_HOME ${android_home}  
ENV ADB_INSTALL_TIMEOUT 120  
ENV
PATH=${ANDROID_HOME}/emulator:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools:${PATH}  
ENV TERM dumb  

