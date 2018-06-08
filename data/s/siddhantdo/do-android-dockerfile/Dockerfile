FROM openjdk:8  
  
# Install Git and dependencies  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -y file git curl zip libncurses5:i386 libstdc++6:i386
zlib1g:i386 libqt5widgets5  
  
# Set up environment variables  
ENV ANDROID_HOME="/home/user/android-sdk-linux" \  
SDK_URL="https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip"  
# Create a non-root user  
RUN useradd -m user  
USER user  
WORKDIR /home/user  
  
# Download Android SDK  
RUN mkdir "$ANDROID_HOME" .android \  
&& cd "$ANDROID_HOME" \  
&& curl -o sdk.zip $SDK_URL \  
&& unzip sdk.zip \  
&& rm sdk.zip \  
&& yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses  
  
ENV PATH="${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${PATH}"  
ENV TARGET="android-27"  
RUN mkdir -p ~/.android \  
&& touch ~/.android/repositories.cfg \  
&& $ANDROID_HOME/tools/bin/sdkmanager \  
"tools" \  
"platforms;${TARGET}"  

