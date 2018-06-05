FROM openjdk:8-slim  
  
ARG PACKAGES="git wget unzip"  
ARG ANDROID_SDK_URL="https://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip"  
ARG ANDROID_PACKAGES="tools platform-tools build-tools;27.0.3
platforms;android-27 extras;google;m2repository extras;android;m2repository"  
# Install required packages  
RUN apt-get update \  
&& apt-get install --yes --no-install-recommends --no-install-suggests
${PACKAGES} \  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/*  
  
# Set environment variable for Android SDK  
ENV ANDROID_HOME "/opt/android-sdk"  
# Create directory for Android SDK  
# Download and install Android SDK and its components  
RUN mkdir -p ${ANDROID_HOME} \  
&& cd ${ANDROID_HOME} \  
&& wget --quiet --output-document=android-tools.zip ${ANDROID_SDK_URL} \  
&& unzip android-tools.zip \  
&& rm -f android-tools.zip \  
&& yes | ${ANDROID_HOME}/tools/bin/sdkmanager --licenses \  
&& ${ANDROID_HOME}/tools/bin/sdkmanager ${ANDROID_PACKAGES} \  
&& chmod -R 777 ${ANDROID_HOME}  
  
# Add Android SDK binaries to PATH  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDORID_HOME}/platform-
tools  
  
# Check that Android SDK is installed  
RUN which android  

