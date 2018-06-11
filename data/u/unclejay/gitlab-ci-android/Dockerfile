#  
# GitLab CI: Android v0.2  
#  
# https://hub.docker.com/r/jangrewe/gitlab-ci-android/  
# https://git.faked.org/jan/gitlab-ci-android  
#  
FROM ubuntu:17.10  
MAINTAINER Jan Grewe <jan@faked.org>  
  
  
ENV ANDROID_NDK_HOME /opt/android-ndk  
ENV ANDROID_NDK_VERSION r16b  
  
ENV VERSION_SDK_TOOLS "3859397"  
ENV ANDROID_HOME "/sdk"  
ENV PATH "$PATH:${ANDROID_HOME}/tools"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update && \  
apt-get install -qqy --no-install-recommends \  
bzip2 \  
curl \  
git-core \  
html2text \  
openjdk-8-jdk \  
libc6-i386 \  
lib32stdc++6 \  
lib32gcc1 \  
lib32ncurses5 \  
lib32z1 \  
unzip \  
wget \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN rm -f /etc/ssl/certs/java/cacerts; \  
/var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
# GitLab injects the username as ENV-variable which will crash a gradle-build.  
# Workaround by adding unicode-support.  
# See  
# https://github.com/gradle/gradle/issues/3117#issuecomment-336192694  
# https://github.com/tianon/docker-brew-debian/issues/45  
RUN apt-get update && apt-get install -y locales && rm -rf
/var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.UTF-8  
RUN curl -s https://dl.google.com/android/repository/sdk-tools-
linux-${VERSION_SDK_TOOLS}.zip > /sdk.zip && \  
unzip /sdk.zip -d /sdk && \  
rm -v /sdk.zip  
  
RUN mkdir -p $ANDROID_HOME/licenses/ \  
&& echo
"8933bad161af4178b1185d1a37fbf41ea5269c55\nd56f5187479451eabf01fb78af6dfcb131a6481e"
> $ANDROID_HOME/licenses/android-sdk-license \  
&& echo
"84831b9409646a918e30573bab4c9c91346d8abd\n504667f4c0de7af1a06de9f4b1727b84351f2910"
> $ANDROID_HOME/licenses/android-sdk-preview-license  
  
ADD packages.txt /sdk  
RUN mkdir -p /root/.android && \  
touch /root/.android/repositories.cfg && \  
${ANDROID_HOME}/tools/bin/sdkmanager --update  
  
RUN while read -r package; do PACKAGES="${PACKAGES}${package} "; done <
/sdk/packages.txt && \  
${ANDROID_HOME}/tools/bin/sdkmanager ${PACKAGES}  
  
RUN yes | ${ANDROID_HOME}/tools/bin/sdkmanager --licenses  
  
# ------------------------------------------------------  
# --- Android NDK  
# download  
#RUN mkdir /opt/android-ndk-tmp  
#RUN cd /opt/android-ndk-tmp  
#RUN wget -q https://dl.google.com/android/repository/android-
ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip  
# uncompress  
#RUN unzip -q android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip  
# move to its final location  
#RUN mv ./android-ndk-${ANDROID_NDK_VERSION} ${ANDROID_NDK_HOME}  
# remove temp dir  
#RUN cd ${ANDROID_NDK_HOME}  
#RUN rm -rf /opt/android-ndk-tmp  
# add to PATH  
#ENV PATH ${PATH}:${ANDROID_NDK_HOME}  

