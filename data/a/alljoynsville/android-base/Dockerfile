FROM ubuntu:xenial  
  
LABEL maintainer="allyonville"  
  
ENV DEBIAN_FRONTEND=noninteractive  
# Install base utilities  
RUN apt-get update && apt-get install -y software-properties-common \  
python-software-properties git build-essential unzip  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get -yqq update && \  
apt-get -yqq install oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
#define env var for 8.  
ENV JAVA_8_HOME /usr/lib/jvm/java-8-oracle  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME $JAVA_8_HOME  
  
# Install Deps  
RUN dpkg --add-architecture i386 && apt-get update && \  
apt-get install -y expect git wget \  
libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 lib32z1 python curl libswt-
gtk-3-java libswt-gtk-3-jni  
  
#install android base sdk (download and unzip)  
RUN wget -q https://dl.google.com/android/repository/tools_r25.2.5-linux.zip
-O android_tools.zip && \  
unzip -qq -d /usr/local/android-sdk-linux android_tools.zip && rm
android_tools.zip  
# setup ENV for android SDK  
ENV ANDROID_HOME /usr/local/android-sdk-linux  
ENV PATH
${JAVA_HOME}/bin:${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:${ANDROID_HOME}/tools/bin  
  
#install ndk , cmake, built-tools, android image and maven repo  
RUN mkdir "$ANDROID_HOME/licenses" && \  
echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" >
"$ANDROID_HOME/licenses/android-sdk-license" && \  
echo -e "\nd56f5187479451eabf01fb78af6dfcb131a6481e" >>
"$ANDROID_HOME/licenses/android-sdk-license" && \  
echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" >
"$ANDROID_HOME/licenses/android-sdk-preview-license"  
RUN sdkmanager --list 2>/dev/null|grep "build-tools"|tail -n -1|awk
'{printf("export buildtools=#%s#\n",$1)}' >> /tmp/packages.android  
RUN sdkmanager --list 2>/dev/null|grep "cmake"|tail -n -1|awk '{printf("export
cmake=#%s#\n",$1)}' >> /tmp/packages.android  
RUN sdkmanager --list 2>/dev/null|grep "lldb"|tail -n -1|awk '{printf("export
lldb=#%s#\n",$1)}' >> /tmp/packages.android  
RUN cat /tmp/packages.android|tr '#' \' > /tmp/packages.android_ && mv
/tmp/packages.android_ /tmp/packages.android  
RUN . /tmp/packages.android && sdkmanager "$buildtools" "$cmake"
"extras;android;m2repository" \  
"extras;google;m2repository" "$lldb" "ndk-bundle" "platforms;android-23" \  
"platforms;android-24" "platforms;android-25"  
RUN rm /tmp/packages.android  
  
# Cleaning  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
  
WORKDIR /  

