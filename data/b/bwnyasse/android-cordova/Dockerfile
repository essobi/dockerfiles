FROM bwnyasse/cordova  
  
MAINTAINER bwnyasse  
  
RUN \  
apt-get update && \  
apt-get install -y lib32stdc++6 lib32z1  
  
# download and extract android sdk  
RUN curl http://dl.google.com/android/android-sdk_r24.2-linux.tgz | tar xz -C
/usr/local/  
ENV ANDROID_HOME /usr/local/android-sdk-linux  
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools  
  
ENV ANDROID_COMPILE_SDK '25'  
ENV ANDROID_BUILD_TOOLS '25.0.2'  
ENV ANDROID_SDK_TOOLS '25.2.5'  
# accept licences  
#RUN mkdir -p $ANDROID_HOME/licenses/ \  
# && echo "8933bad161af4178b1185d1a37fbf41ea5269c55" >
$ANDROID_HOME/licenses/android-sdk-license \  
# && echo "84831b9409646a918e30573bab4c9c91346d8abd" >
$ANDROID_HOME/licenses/android-sdk-preview-license  
RUN mkdir -p $ANDROID_HOME/licenses/ \  
&& echo -e "8933bad161af4178b1185d1a37fbf41ea5269c55\c" >
${ANDROID_HOME}/licenses/android-sdk-license \  
&& echo -e
"79120722343a6f314e0719f863036c702b0e6b2a\n84831b9409646a918e30573bab4c9c91346d8abd\c"
> ${ANDROID_HOME}/licenses/android-sdk-preview-license \  
&& echo -e "8403addf88ab4874007e1c1e80a0025bf2550a37\c" >
${ANDROID_HOME}/licenses/intel-android-sysimage-license  
  
# update and accept licences  
RUN ( sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) | /usr/local/android-
sdk-linux/tools/android update sdk --no-ui -a --filter platform-
tools,android-${ANDROID_COMPILE_SDK},build-tools-${ANDROID_BUILD_TOOLS}; \  
find /usr/local/android-sdk-linux -perm 0744 | xargs chmod 755  
  
# install the Android build tools  
RUN ( sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) | /usr/local/android-
sdk-linux/tools/android update sdk --no-ui -a -t 4;  
#  
# ENV ANDROID_COMPILE_SDK '24'  
# ENV ANDROID_BUILD_TOOLS '25.0.2'  
# ENV ANDROID_SDK_TOOLS '25.2.5'  
ENV GRADLE_USER_HOME /src/gradle  
  
VOLUME /src  
WORKDIR /src  

