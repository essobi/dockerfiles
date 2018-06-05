FROM gradle  
  
MAINTAINER Nikolay Glushchenko <nick@nickalie.com>  
  
USER root  
  
# Install AIR SDK  
RUN wget
https://airdownload.adobe.com/air/win/download/latest/AIRSDK_Compiler.zip && \  
unzip AIRSDK_Compiler.zip -d /AIRSDK && \  
rm AIRSDK_Compiler.zip  
  
ENV FLEX_HOME=/AIRSDK  
  
# Install Android SDK  
ENV ANDROID_HOME /opt/android-sdk  
  
RUN mkdir -p $ANDROID_HOME && \  
cd $ANDROID_HOME && \  
wget https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip -O
tools.zip && \  
unzip tools.zip && \  
rm -f tools.zip && \  
mkdir $ANDROID_HOME/licenses && \  
echo 8933bad161af4178b1185d1a37fbf41ea5269c55 >
$ANDROID_HOME/licenses/android-sdk-license && \  
echo 84831b9409646a918e30573bab4c9c91346d8abd >
$ANDROID_HOME/licenses/android-sdk-preview-license  
  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  
  
RUN sdkmanager --verbose "platforms;android-25" "build-tools;25.0.3"
"extras;android;m2repository" "extras;google;m2repository"  
  
# Initialize template project to preload commonly used libraries  
COPY template /tmp/template  
RUN cd /tmp/template && \  
chmod +x gradlew && \  
./gradlew build && \  
cd / rm -rf /tmp/template

