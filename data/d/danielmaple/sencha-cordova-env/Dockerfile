FROM danielmaple/sencha-env:latest  
MAINTAINER Daniel Maple <danielm@ibcos.co.uk>  
  
# Install Cordova module using NPM  
RUN npm install -g cordova  
  
# Set environment variables for Cordova CLI  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH $PATH:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
# Install Android SDK  
ENV ANDROID_BUILD_TOOLS_VERSION 24.0.2  
ENV ANDROID_API_LEVELS android-22,android-23,android-24  
ENV ANDROID_PACKAGES tools,platform-tools,build-
tools-${ANDROID_BUILD_TOOLS_VERSION},extra-android-
support,${ANDROID_API_LEVELS}  
# Download the compressed Android command line tools archive  
RUN curl -o /tmp/android-sdk.tgz https://dl.google.com/android/android-
sdk_r24.4.1-linux.tgz && \  
# Extract the archive to /opt  
tar -xzf /tmp/android-sdk.tgz -C /opt && \  
# Update Android SDK  
echo y | android update sdk --filter ${ANDROID_PACKAGES} -a --no-ui && \  
# Remove temporary file  
rm /tmp/android-sdk.tgz  

