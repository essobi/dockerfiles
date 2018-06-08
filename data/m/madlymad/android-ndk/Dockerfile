  
FROM madlymad/android-sdk:27  
# Everything will be installed in the directory but jdk.  
ENV SDK_HOME /usr/local  
  
# Install dependencies  
RUN dpkg --add-architecture i386 && \  
apt-get -qq update && \  
apt-get -qqy install --no-install-recommends \  
file && \  
rm -rf /var/lib/apt/lists/*  
  
ENV ANDROID_NDK_VERSION r14b  
  
ENV ANDROID_NDK_URL http://dl.google.com/android/repository/android-
ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip  
  
# Download and unzip Android NDK  
RUN curl -L "${ANDROID_NDK_URL}" -o android-
ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip \  
&& unzip android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip -d ${SDK_HOME} \  
&& rm -rf android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip  
  
ENV ANDROID_NDK_HOME ${SDK_HOME}/android-ndk-${ANDROID_NDK_VERSION}  
  
ENV PATH ${ANDROID_NDK_HOME}:$PATH  

