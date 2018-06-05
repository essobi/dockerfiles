FROM java:8  
MAINTAINER Takao Chiba <chibatching.apps@gmail.com>  
  
RUN dpkg --add-architecture i386 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get update && \  
apt-get install -yq libc6:i386 libstdc++6:i386 zlib1g:i386 libncurses5:i386
build-essential libssl-dev ruby ruby-dev --no-install-recommends && \  
apt-get clean  
  
RUN gem install bundler  
  
# Download and untar Android SDK tools  
RUN mkdir -p /usr/local/android-sdk-linux  
RUN wget https://dl.google.com/android/repository/tools_r25.2.3-linux.zip -O
tools.zip  
RUN unzip tools.zip -d /usr/local/android-sdk-linux  
RUN rm tools.zip  
  
# Set environment variable  
ENV ANDROID_HOME /usr/local/android-sdk-linux  
ENV PATH ${ANDROID_HOME}/tools:$ANDROID_HOME/platform-tools:$PATH  
  
RUN mkdir $ANDROID_HOME/licenses  
RUN echo 8933bad161af4178b1185d1a37fbf41ea5269c55 >
$ANDROID_HOME/licenses/android-sdk-license  
RUN echo d56f5187479451eabf01fb78af6dfcb131a6481e >>
$ANDROID_HOME/licenses/android-sdk-license  
RUN echo 84831b9409646a918e30573bab4c9c91346d8abd >
$ANDROID_HOME/licenses/android-sdk-preview-license  
  
# Update and install using sdkmanager  
RUN $ANDROID_HOME/tools/bin/sdkmanager "tools" "platform-tools"  
RUN $ANDROID_HOME/tools/bin/sdkmanager "build-tools;26.0.2" "build-
tools;25.0.3"  
RUN $ANDROID_HOME/tools/bin/sdkmanager "platforms;android-26"
"platforms;android-25" "platforms;android-24" "platforms;android-23"  
RUN $ANDROID_HOME/tools/bin/sdkmanager "extras;android;m2repository"
"extras;google;m2repository"  
RUN $ANDROID_HOME/tools/bin/sdkmanager
"extras;m2repository;com;android;support;constraint;constraint-layout;1.0.2"  
RUN $ANDROID_HOME/tools/bin/sdkmanager
"extras;m2repository;com;android;support;constraint;constraint-layout-
solver;1.0.2"  

