FROM openjdk:8-jdk  
  
ENV ANDROID_COMPILE_SDK "25"  
ENV ANDROID_BUILD_TOOLS "25.0.2"  
ENV ANDROID_SDK_TOOLS_REV "3859397"  
ENV ANDROID_CMAKE_REV "3.6.4111459"  
  
  
RUN mkdir $HOME/.android && \  
echo 'count=0' > $HOME/.android/repositories.cfg && \  
wget --quiet --output-document=android-sdk.zip
https://dl.google.com/android/repository/sdk-tools-
linux-${ANDROID_SDK_TOOLS_REV}.zip && \  
mkdir $PWD/android-sdk-linux && \  
unzip -qq android-sdk.zip -d $PWD/android-sdk-linux && \  
export ANDROID_HOME=$PWD/android-sdk-linux && \  
# - export ANDROID_NDK_HOME=$ANDROID_HOME/ndk-bundle NDK  
export PATH=$PATH:$ANDROID_HOME/platform-tools/:$ANDROID_NDK_HOME && \  
echo y | $ANDROID_HOME/tools/bin/sdkmanager --update && \  
echo y | $ANDROID_HOME/tools/bin/sdkmanager 'tools' && \  
echo y | $ANDROID_HOME/tools/bin/sdkmanager 'platform-tools' && \  
echo y | $ANDROID_HOME/tools/bin/sdkmanager 'build-tools;'$ANDROID_BUILD_TOOLS
&& \  
echo y | $ANDROID_HOME/tools/bin/sdkmanager
'platforms;android-'$ANDROID_COMPILE_SDK && \  
echo y | $ANDROID_HOME/tools/bin/sdkmanager 'extras;android;m2repository' && \  
echo y | $ANDROID_HOME/tools/bin/sdkmanager
'extras;google;google_play_services' && \  
echo y | $ANDROID_HOME/tools/bin/sdkmanager 'extras;google;m2repository' && \  
echo y | $ANDROID_HOME/tools/bin/sdkmanager 'cmake;'$ANDROID_CMAKE_REV

