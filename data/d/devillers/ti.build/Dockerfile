#  
# Appcelerator Titanium Mobile Build Dockerfile  
#  
# https://github.com/MartinDevillers/ti.build  
#  
FROM ubuntu:14.04  
MAINTAINER Martin Devillers <martin@devillers.nl>  
  
# Install Oracle Java JDK 6  
RUN \  
apt-get update && \  
apt-get install -y software-properties-common && \  
echo oracle-java6-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java6-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk6-installer  
  
# Set Java Home to JDK6  
ENV JAVA_HOME /usr/lib/jvm/java-6-oracle  
  
# Install necesary packages (i386 stuff is required for Android 32-bit build;
gperf is used by ndk-build)  
RUN \  
dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get -y install \  
libc6:i386 libncurses5:i386 libstdc++6:i386 zlib1g:i386 \  
gperf \  
unzip \  
nodejs \  
npm  
  
# Alias nodejs command under node  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# Install Titanium SDK and Alloy  
RUN npm install -g titanium alloy  
  
# Grab Android SDK  
RUN cd /opt && \  
wget -nv -O android-sdk.tgz http://dl.google.com/android/android-
sdk_r24.4.1-linux.tgz && \  
tar -xvzf android-sdk.tgz && \  
rm -f android-sdk.tgz  
  
# Install Android SDK 23 and additional tools  
RUN echo y | /opt/android-sdk-linux/tools/android update sdk --all --filter
android-23,platform-tools,build-tools-21.0.0 --no-ui --force  
  
# Grab Android NDK (r10 instead of r11 due to bug; see TIMOB-20613 for more
details)  
RUN cd /opt && \  
wget -nv -O android-ndk.zip https://dl.google.com/android/repository/android-
ndk-r10e-linux-x86_64.zip && \  
unzip android-ndk.zip && \  
rm -f android-ndk.zip  
  
# Set full permissions on /opt/ (ensures build user has appropriate
permissions)  
RUN chmod -R 777 /opt/  
  
# Create build user (required by Titanium)  
RUN useradd -ms /bin/bash build  
USER build  
  
# Grab Titanium SDK  
RUN mkdir /home/build/.titanium && \  
cd /home/build/.titanium && \  
wget -nv -O titanium.zip http://builds.appcelerator.com/mobile-
releases/5.2.2/mobilesdk-5.2.2.GA-linux.zip && \  
unzip titanium.zip && \  
rm -f titanium.zip  
#RUN titanium sdk install 5.2.2.GA --default #doesn't work due to bug in
titanium  
#RUN appc ti sdk install 5.2.2.GA #appc requires login  
# Set Android SDK/NDK Environment Variable  
ENV ANDROID_SDK /opt/android-sdk-linux  
ENV ANDROID_NDK /opt/android-ndk-r10e  
  
# Configure Android SDK/NDK path in Titanium CLI  
RUN titanium config android.sdk /opt/android-sdk-linux  
RUN titanium config android.ndk /opt/android-ndk-r10e  
  
# Set the defauilt build command  
CMD titanium build -b -p android --log-level trace

