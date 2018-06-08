FROM openjdk:8-jdk-slim  
  
# https://developer.android.com/studio/index.html  
ARG ANDROID_SDK_TOOLS_VERSION=3859397  
ARG
ANDROID_SDK_TOOLS_SHA256=444e22ce8ca0f67353bda4b85175ed3731cae3ffa695ca18119cbacef1c1bea0  
ARG ANDROID_BUILD_TOOLS_VERSION=27.0.3  
# https://services.gradle.org/distributions/gradle-4.6-bin.zip.sha256  
ARG GRADLE_VERSION=4.6  
ARG
GRADLE_SHA256=98bd5fd2b30e070517e03c51cbb32beee3e2ee1a84003a5a5d748996d4b1b915  
  
ENV ANDROID_HOME=/opt/android-sdk-linux  
ENV ANDROID_SDK_TOOLS_VERSION=$ANDROID_SDK_TOOLS_VERSION  
ENV ANDROID_SDK_TOOLS_SHA256=$ANDROID_SDK_TOOLS_SHA256  
ENV ANDROID_BUILD_TOOLS_VERSION=$ANDROID_BUILD_TOOLS_VERSION  
ENV GRADLE_VERSION=$GRADLE_VERSION  
ENV GRADLE_SHA256=$GRADLE_SHA256  
ENV GRADLE_HOME=/opt/gradle-$GRADLE_VERSION  
ENV
PATH=${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools:${ANDROID_HOME}/build-
tools/${ANDROID_BUILD_TOOLS_VERSION}:${GRADLE_HOME}/bin  
  
RUN set -ex; \  
apt-get update ; \  
apt-get install -y --no-install-recommends curl ; \  
apt-get autoremove --purge -y ; \  
apt-get clean -y; \  
rm -rf /var/lib/apt/lists/* ;  
  
RUN set -ex; \  
WORKDIR="$PWD" ; \  
mkdir -p "$ANDROID_HOME" ; \  
curl -q -sSLO "https://dl.google.com/android/repository/sdk-tools-
linux-${ANDROID_SDK_TOOLS_VERSION}.zip" ; \  
echo "$ANDROID_SDK_TOOLS_SHA256 sdk-tools-
linux-${ANDROID_SDK_TOOLS_VERSION}.zip" | sha256sum -c; \  
unzip -d "$ANDROID_HOME" "sdk-tools-linux-${ANDROID_SDK_TOOLS_VERSION}.zip" ;
\  
rm "sdk-tools-linux-${ANDROID_SDK_TOOLS_VERSION}.zip" ; \  
curl -q -sSLO
"https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" ;
\  
echo "$GRADLE_SHA256 gradle-${GRADLE_VERSION}-bin.zip" | sha256sum -c; \  
unzip -d "/opt" "gradle-${GRADLE_VERSION}-bin.zip" ; \  
rm "gradle-${GRADLE_VERSION}-bin.zip" ; \  
mkdir -p /root/.android ; \  
touch /root/.android/repositories.cfg ; \  
yes | sdkmanager --licenses ;  
  
# Prefetch common android sdk packages  
RUN set -ex; \  
sdkmanager --update --verbose; \  
sdkmanager --verbose 'platform-tools' ; \  
sdkmanager --verbose
'extras;m2repository;com;android;support;constraint;constraint-layout-
solver;1.0.2' ; \  
sdkmanager --verbose
'extras;m2repository;com;android;support;constraint;constraint-layout;1.0.2' ;
\  
sdkmanager --verbose 'extras;google;m2repository' ; \  
sdkmanager --verbose 'extras;android;m2repository' ; \  
sdkmanager --verbose 'extras;google;google_play_services' ; \  
# Presently KitKat(19) - Current represents about 95% of platform
distribution:
https://cordova.apache.org/docs/en/latest/guide/platforms/android/  
sdkmanager --verbose 'platforms;android-19' 'platforms;android-26'
'platforms;android-27' ; \  
sdkmanager --verbose "build-tools;${ANDROID_BUILD_TOOLS_VERSION}"; \  
yes | sdkmanager --licenses ;  
  
RUN set -ex; \  
gradle -v  

