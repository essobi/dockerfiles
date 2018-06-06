  
FROM ubuntu:16.04  
# == Install required tools  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq && apt-get install -qq -y \  
bc \  
binutils-arm-linux-gnueabi \  
binutils-aarch64-linux-gnu \  
binutils-multiarch \  
curl \  
expect \  
git \  
maven \  
nano \  
python \  
python-dev \  
python-pip \  
python3-pip \  
scons \  
unzip \  
wget \  
zip \  
libcapstone3 \  
openjdk-8-jdk-headless \  
tzdata \  
software-properties-common  
  
# == Add python 3.6 repository  
RUN add-apt-repository -y ppa:deadsnakes/ppa  
RUN apt-get update -qq && apt-get install -qq -y \  
python3.6 \  
python3.6-dev  
  
RUN ln -fs /usr/share/zoneinfo/Europe/London /etc/localtime  
  
# Set JAVA_HOME  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
# FIXME: Python stuff should be in a venv handled by .jenkins.sh  
ENV PYTHON_REQS "requests PyJWT validators durations pyaxmlparser javalang
capstone virtualenv"  
RUN pip install --upgrade pip && pip install -q $PYTHON_REQS  
RUN pip3 install -q $PYTHON_REQS  
  
#Android stuff  
RUN apt-get install -qq -y gradle  
  
# 32-bit libraries  
RUN dpkg --add-architecture i386 \  
&& apt-get update -qq \  
&& apt-get install -qq -y libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1
libbz2-1.0:i386  
  
# == Set up Android NDK-related environment  
ENV ANDROID_NDK_HOME /opt/android-ndk-r12  
ENV PATH ${PATH}:${ANDROID_NDK_HOME}  
  
# == Download Android NDK and install in /opt/android-ndk-r12  
ENV ANDROID_NDK_PACKAGE=android-ndk-r12-linux-x86_64.zip  
RUN cd /opt \  
&& wget -q http://dl.google.com/android/repository/${ANDROID_NDK_PACKAGE} \  
&& unzip -q ${ANDROID_NDK_PACKAGE} \  
&& rm ${ANDROID_NDK_PACKAGE} \  
&& test -d "${ANDROID_NDK_HOME}"  
  
# === Install Android SDKs  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV ANDROID_SDK_FILENAME android-sdk_r24.3.3-linux.tgz  
ENV ANDROID_SDK_URL http://dl.google.com/android/${ANDROID_SDK_FILENAME}  
ENV ANDROID_API_LEVELS android-25  
ENV ANDROID_BUILD_TOOLS_VERSION 25.0.3  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
RUN cd /opt && \  
wget -q ${ANDROID_SDK_URL} && \  
tar -xzf ${ANDROID_SDK_FILENAME} && \  
rm ${ANDROID_SDK_FILENAME} && \  
echo y | android update sdk --no-ui -a --filter tools,platform-
tools,${ANDROID_API_LEVELS},build-tools-${ANDROID_BUILD_TOOLS_VERSION}  
  
# Create home directory and make it writable so jenkins can invoke gradle
safely  
RUN mkdir $ANDROID_HOME/.android && \  
chmod 777 $ANDROID_HOME/.android  
  
# === Install Android Support Repository  
# If missing, causes: Could not find any matches for
com.android.support:support-v4:23.0.+ as no  
# versions of com.android.support:support-v4 are available.  
# extra-android-m2repository  
# Type: Extra  
# Desc: Android Support Repository, revision 41  
# By Android  
# Local Maven repository for Support Libraries  
RUN mkdir "$ANDROID_HOME/licenses" && \  
echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" >
"$ANDROID_HOME/licenses/android-sdk-license" && \  
echo -e "\nd56f5187479451eabf01fb78af6dfcb131a6481e" >>
"$ANDROID_HOME/licenses/android-sdk-license" && \  
echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" >
"$ANDROID_HOME/licenses/android-sdk-preview-license"  
  
RUN cd /opt/android-sdk-linux/tools/ && \  
echo y | ./android update sdk --no-ui --all --filter extra-
android-m2repository | grep 'package installed' && \  
echo y | ./android update sdk --no-ui --all --filter extra-google-m2repository
| grep 'package installed'  

