FROM ubuntu:latest  
  
LABEL maintainers "dev@oyez.fr"  
  
ARG ARG_ANDROID_SDK  
ARG ARG_ANDROID_SDK_TOOLS  
ARG ARG_ANDROID_BUILD_TOOLS  
ARG ARG_GOOGLE_APIS  
  
ENV ANDROID_SDK ${ARG_ANDROID_SDK:-23}  
ENV ANDROID_TOOLS ${ARG_ANDROID_SDK_TOOLS:-25.2.5}  
ENV ANDROID_BUILD_TOOLS ${ARG_ANDROID_BUILD_TOOLS:-25.0.1}  
ENV GOOGLE_APIS ${ARG_GOOGLE_APIS:-23}  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
  
RUN \  
apt-get update -qq && \  
apt-get install -qq -y sudo software-properties-common zip && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update -qq && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get install -qq -y oracle-java8-installer gradle maven && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# sudo apt install oracle-java8-set-default  
RUN \  
cd /opt && \  
wget -q
https://dl.google.com/android/repository/tools_r${ANDROID_TOOLS}-linux.zip -O
android-sdk-tools.zip && \  
unzip -q android-sdk-tools.zip && \  
mkdir -p ${ANDROID_HOME} && \  
mv tools/ android-sdk-linux/tools/ && \  
rm android-sdk-tools.zip  
  
# Install android requirements  
RUN \  
echo y | android update sdk -u -a -t platform-tools | grep 'package installed'
&& \  
echo y | android update sdk -u -a -t android-${ANDROID_SDK} | grep 'package
installed' && \  
echo y | android update sdk -u -a -t build-tools-${ANDROID_BUILD_TOOLS} | grep
'package installed' && \  
echo y | android update sdk -u -a -t extra-android-m2repository | grep
'package installed' && \  
echo y | android update sdk -u -a -t addon-google_apis-google-${GOOGLE_APIS} |
grep 'package installed'

