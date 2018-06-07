#  
# CircleCi Android Runner  
#  
#  
FROM ubuntu:16.04  
ENV VERSION_SDK_TOOLS "26.0.2"  
ENV VERSION_NDK "r14b"  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV ANDROID_HOME "/sdk"  
ENV PATH "$PATH:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools"  
ENV ANDROID_NDK_HOME "/ndk"  
ENV PATH "$PATH:${ANDROID_NDK_HOME}/"  
RUN apt-get -qq update && \  
apt-get install -qqy --no-install-recommends \  
curl \  
html2text \  
openjdk-8-jdk \  
libc6-i386 \  
lib32stdc++6 \  
lib32gcc1 \  
lib32ncurses5 \  
lib32z1 \  
unzip \  
wget \  
build-essential \  
expect \  
file \  
libmagic1 \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Fix the java certs  
RUN rm -f /etc/ssl/certs/java/cacerts; \  
/var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
# Install the SDK tools  
RUN wget https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip
-O /tools.zip \  
&& unzip /tools.zip -d /$ANDROID_HOME && \  
rm -v /tools.zip  
  
# Add travis tools  
RUN wget
https://raw.githubusercontent.com/appunite/docker/eacea57245e95f112c55c41b41d2c0cf218fd334/android-
java8/tools/android-accept-licenses.sh -O /usr/local/bin/android-accept-
licenses \  
&& chmod +x /usr/local/bin/android-accept-licenses  
  
RUN wget https://raw.githubusercontent.com/travis-ci/travis-
cookbooks/ca800a93071a603745a724531c425a41493e70ff/community-
cookbooks/android-sdk/files/default/android-wait-for-emulator -O
/usr/local/bin/android-wait-for-emulator \  
&& chmod +x /usr/local/bin/android-wait-for-emulator  
  
# ADD  
# ADD echo -e "84831b9409646a918e30573bab4c9c91346d8abd" >
$ANDROID_HOME/licenses/android-sdk-preview-license  
# Install the SDK stuff  
RUN mkdir $ANDROID_HOME/licenses && echo -n -e
"\n8933bad161af4178b1185d1a37fbf41ea5269c55" > $ANDROID_HOME/licenses/android-
sdk-license && \  
echo -e "84831b9409646a918e30573bab4c9c91346d8abd" >
$ANDROID_HOME/licenses/android-sdk-preview-license && \  
$ANDROID_HOME/tools/bin/sdkmanager "platform-tools" \  
"tools" \  
"platforms;android-22" \  
"platforms;android-23" \  
"platforms;android-24" \  
"platforms;android-25" && \  
$ANDROID_HOME/tools/bin/sdkmanager "extras;android;m2repository" \  
"extras;google;m2repository" \  
"extras;google;webdriver" \  
"extras;google;google_play_services"  
  
CMD ["/bin/bash"]  

