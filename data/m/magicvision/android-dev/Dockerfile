FROM ubuntu:14.04  
MAINTAINER MagicVision Team  
  
WORKDIR /opt  
  
# Add i386 as Android SDK contains 32b binaries  
RUN dpkg --add-architecture i386  
  
# Use tsinghua ubuntu mirror  
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted
universe multiverse" > /etc/apt/sources.list && \  
echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted
universe multiverse" >> /etc/apt/sources.list && \  
echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted
universe multiverse" >> /etc/apt/sources.list && \  
echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted
universe multiverse" >> /etc/apt/sources.list && \  
echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted
universe multiverse" >> /etc/apt/sources.list && \  
apt-get update -y  
  
# Install common tools  
RUN apt-get install -y wget git unzip  
  
# Install Android SDK dependencies  
RUN apt-get install -y lib32stdc++6 lib32z1  
RUN apt-get install -y openjdk-7-jdk  
  
# Install Android SDK Tools, see
http://developer.android.com/sdk/index.html#Other  
RUN wget -q http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz && \  
tar xf android-sdk_r24.4.1-linux.tgz && \  
rm -f android-sdk_r24.4.1-linux.tgz  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH $PATH:$ANDROID_HOME/tools  
  
# Install latest android (15 / 4.0.3) tools and system image.  
RUN echo "y" | android update sdk --no-ui --force --all --filter platform-
tools,build-tools-22.0.1,android-15 --no-https --proxy-host
mirrors.dormforce.net  
ENV PATH $PATH:$ANDROID_HOME/platform-tools  
ENV PATH $PATH:$ANDROID_HOME/build-tools/22.0.1  
# Install Android NDK dependencies  
RUN apt-get install -y make  
  
# Install Android NDK, see
http://developer.android.com/ndk/downloads/index.html  
RUN wget -q http://dl.google.com/android/ndk/android-ndk-r10e-linux-x86_64.bin
&& \  
chmod a+x android-ndk-r10e-linux-x86_64.bin && \  
./android-ndk-r10e-linux-x86_64.bin >/dev/null && \  
rm -f android-ndk-r10e-linux-x86_64.bin  
ENV ANDROID_NDK_HOME /opt/android-ndk-r10e  
ENV PATH $PATH:$ANDROID_NDK_HOME  
  
# Install gradle  
RUN wget -q https://services.gradle.org/distributions/gradle-2.8-bin.zip && \  
unzip gradle-2.8-bin.zip && \  
rm -f gradle-2.8-bin.zip  
ENV GRADLE_HOME /opt/gradle-2.8  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
# Provisioning GitLab CA  
ADD CA.crt /usr/local/share/ca-certificates/  
RUN update-ca-certificates  

