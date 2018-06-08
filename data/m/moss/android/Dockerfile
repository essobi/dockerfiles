#: title : moss/android  
#: author : "Thiago Almeida" <thiagoalmeidasa@gmail.com>  
#: version: "1.1.0"  
FROM moss/java_oracle  
MAINTAINER Thiago Almeida <thiagoalmeidasa@gmail.com>  
  
LABEL version="1.1.0"  
  
# Build variables  
ENV ANDROID_SDK_FILE android-sdk_r24.4.1-linux.tgz  
ENV ANDROID_SDK_URL https://dl.google.com/android/${ANDROID_SDK_FILE}  
ENV ANDROID_BUILD_TOOLS_VERSION 24.0.2  
ENV ANDROID_APIS android-21,android-24  
ENV ANDROID_ABI sys-img-armeabi-v7a-android-21,sys-img-armeabi-v7a-android-21  
ENV ANDROID_EXTRA extra-android-m2repository  
  
# Set environment variables  
ENV GRADLE_HOME /usr/share/gradle  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-
tools:$ANDROID_HOME/build-tools/$ANDROID_BUILD_TOOLS_VERSION  
ENV PATH $PATH:$ANT_HOME/bin  
ENV PATH $PATH:$MAVEN_HOME/bin  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
WORKDIR "/opt"  
  
RUN apt-get update -y && \  
# install 32-bit dependencies require by the android sdk  
dpkg --add-architecture i386 && \  
apt-get update -y && \  
apt-get install -y libncurses5:i386 libstdc++6:i386 zlib1g:i386 --no-install-
recommends  
  
# Install Android SDK  
RUN curl -sL ${ANDROID_SDK_URL} | tar xz -C . && \  
echo y | android update sdk -a -u -t platform-tools,${ANDROID_APIS},build-
tools-${ANDROID_BUILD_TOOLS_VERSION},${ANDROID_ABI},${ANDROID_EXTRA} && \  
  
# Clean up  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get autoremove -y && \  
apt-get clean  
  
# Create AVD  
RUN echo "no" | android create avd \  
\--force \  
\--device "Nexus 6" \  
\--name MOSS_NEXUS6 \  
\--target android-21 \  
\--abi armeabi-v7a \  
\--skin WVGA800  
  
# Go to workspace  
RUN mkdir -p /opt/workspace  
WORKDIR /opt/workspace  
  

