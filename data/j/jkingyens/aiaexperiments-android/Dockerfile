FROM openjdk:8  
ENV ANDROID_SDK_HOME /opt/sdk  
ENV ANDROID_HOME /opt/sdk  
ENV SDK_TOOLS "3859397"  
ENV BUILD_TOOLS "27.0.1"  
ENV TARGET_SDK "27"  
# Download and extract Android Tools  
RUN wget http://dl.google.com/android/repository/sdk-tools-
linux-${SDK_TOOLS}.zip -O /tmp/tools.zip && \  
mkdir -p ${ANDROID_HOME} && \  
unzip /tmp/tools.zip -d ${ANDROID_HOME} && \  
rm -v /tmp/tools.zip  
  
# Install SDK Packages  
RUN mkdir -p ${ANDROID_HOME}/licenses/ && \  
echo "8933bad161af4178b1185d1a37fbf41ea5269c55" >
${ANDROID_HOME}/licenses/android-sdk-license && \  
mkdir -p /root/.android/ && touch /root/.android/repositories.cfg && \  
${ANDROID_HOME}/tools/bin/sdkmanager "build-tools;${BUILD_TOOLS}" "platform-
tools" "platforms;android-${TARGET_SDK}" "extras;android;m2repository"
"extras;google;google_play_services" "extras;google;m2repository"  
  
# accept all licenses?  
RUN yes | ${ANDROID_HOME}/tools/bin/sdkmanager --licenses  
  
# Make SDK binaries available to shell  
ENV PATH="${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools:${ANDROID_HOME}/build-tools/27.0.1:${PATH}"  
# install node so we can run the publish script  
RUN cd /root && wget
https://nodejs.org/dist/v6.11.3/node-v6.11.3-linux-x64.tar.xz  
RUN cd /root && tar -xvf node-v6.11.3-linux-x64.tar.xz  
RUN rm /root/node-v6.11.3-linux-x64.tar.xz  
ENV PATH="/root/node-v6.11.3-linux-x64/bin:${PATH}"  
# create a workspace for the android project and copy it there  
WORKDIR /root/project  
RUN mkdir -p /root/.gradle  
RUN mkdir -p /root/project  
COPY . /root/project  
  
RUN cd /root/project/push && npm install  
  
# build the release apk and upload it to the play store using our token  
CMD ./gradlew assembleRelease && cd /root/project/push && node push.js  

