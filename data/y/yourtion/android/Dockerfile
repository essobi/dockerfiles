FROM java:8  
MAINTAINER Yourtion <yourtion@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
# Everything will be installed in the directory but jdk.  
ENV SDK_HOME /usr/local  
  
# Install dependencies  
RUN dpkg --add-architecture i386 && \  
apt-get -qq update && \  
apt-get -qqy install libc6:i386 libstdc++6:i386 zlib1g:i386 libncurses5:i386
tar git --no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
# Download and untar Android SDK  
ENV ANDROID_SDK_VERSION 25.2.4  
ENV ANDROID_SDK_URL
http://dl.google.com/android/repository/tools_r${ANDROID_SDK_VERSION}-linux.zip  
RUN curl -L "${ANDROID_SDK_URL}" > android-sdk.zip && \  
unzip android-sdk.zip -d ${SDK_HOME}/android-sdk-linux && \  
rm android-sdk.zip  
ENV ANDROID_HOME ${SDK_HOME}/android-sdk-linux  
ENV ANDROID_SDK ${SDK_HOME}/android-sdk-linux  
ENV PATH ${ANDROID_HOME}/tools:$ANDROID_HOME/platform-tools:$PATH  
  
RUN mkdir -p "$ANDROID_SDK/licenses" && \  
echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" >
"$ANDROID_SDK/licenses/android-sdk-license" && \  
echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" >
"$ANDROID_SDK/licenses/android-sdk-preview-license"  
  
# Install Android SDK components  
ENV ANDROID_VERSION 25  
ENV ANDROID_TOOLS_VERSION 25.0.2  
ENV ANDROID_COMPONENTS platform-tools,build-
tools-${ANDROID_TOOLS_VERSION},android-${ANDROID_VERSION}  
ENV GOOGLE_COMPONENTS extra-android-m2repository,extra-android-support  
  
RUN echo y | android update sdk --no-ui --all --filter
"${ANDROID_COMPONENTS}"; \  
echo y | android update sdk --no-ui --all --filter "${GOOGLE_COMPONENTS}"  

