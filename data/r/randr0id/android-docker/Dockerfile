#  
# Android Docker v1.0  
#  
# https://hub.docker.com/r/randr0id/android-docker  
# https://github.com/randr0id/android-docker  
#  
FROM ubuntu:17.10  
LABEL maintainer="randy@randr0id.com"  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.schema-version="1.0"  
LABEL org.label-schema.name="randr0id/android-docker"  
LABEL org.label-schema.description="A Docker image for building and testing
Android apps."  
LABEL org.label-schema.version="1.0"  
LABEL org.label-schema.build-date=${BUILD_DATE}  
LABEL org.label-schema.url="https://hub.docker.com/r/randr0id/android-docker"  
LABEL org.label-schema.vcs-url="https://github.com/randr0id/android-docker"  
LABEL org.label-schema.vcs-ref=${VCS_REF}  
  
ENV VERSION_SDK_TOOLS "3859397"  
ENV ANDROID_HOME "/sdk"  
ENV PATH "${PATH}:${ANDROID_HOME}/tools"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update && \  
apt-get install -qqy --no-install-recommends \  
build-essential \  
bzip2 \  
curl \  
git-core \  
html2text \  
libc6-i386 \  
lib32stdc++6 \  
lib32gcc1 \  
lib32ncurses5 \  
lib32z1 \  
openjdk-8-jdk \  
qemu-kvm \  
unzip \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN rm -f /etc/ssl/certs/java/cacerts; \  
/var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
RUN curl -s "https://dl.google.com/android/repository/sdk-tools-
linux-${VERSION_SDK_TOOLS}.zip" > /sdk.zip && \  
unzip /sdk.zip -d /sdk && \  
rm -v /sdk.zip  
  
RUN mkdir -p "${ANDROID_HOME}/licenses/" && \  
printf
"8933bad161af4178b1185d1a37fbf41ea5269c55\\\nd56f5187479451eabf01fb78af6dfcb131a6481e"
> "${ANDROID_HOME}/licenses/android-sdk-license" && \  
printf
"84831b9409646a918e30573bab4c9c91346d8abd\\\n504667f4c0de7af1a06de9f4b1727b84351f2910"
> "${ANDROID_HOME}/licenses/android-sdk-preview-license"  
  
RUN mkdir -p /root/.android && \  
touch /root/.android/repositories.cfg && \  
"${ANDROID_HOME}/tools/bin/sdkmanager" \--update  
  
COPY packages.txt /sdk  
RUN while read -r package; do PACKAGES="${PACKAGES}${package} "; done <
/sdk/packages.txt && \  
"${ANDROID_HOME}/tools/bin/sdkmanager" ${PACKAGES}  
  
RUN yes | "${ANDROID_HOME}/tools/bin/sdkmanager" \--licenses  
  
RUN mkdir /utils  
COPY install-google-cloud-sdk.sh /utils  
COPY start-test-emulator.sh /utils  
COPY wait-for-emulator.sh /utils  
  
CMD ${ANDROID_HOME}/tools/bin/sdkmanager --update  

