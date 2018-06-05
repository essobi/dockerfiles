FROM rxwen/ubuntu-jdk  
  
MAINTAINER Raymond Wen "rx.wen218@gmail.com"  
ENV ANDROID_SDK_VERSION 3859397  
ENV GRADLE_VERSION 3.4.1  
USER root  
RUN apt-get update && apt-get install -y zip unzip curl wget openssl make
openssh-client git python libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5
lib32z1  
  
# Install Android SDK  
ENV ANDROID_HOME /opt/android-sdk  
RUN wget https://dl.google.com/android/repository/sdk-tools-
linux-${ANDROID_SDK_VERSION}.zip \  
&& mkdir -p ${ANDROID_HOME} \  
&& unzip -d ${ANDROID_HOME} sdk-tools-linux-${ANDROID_SDK_VERSION}.zip \  
&& rm sdk-tools-linux-${ANDROID_SDK_VERSION}.zip  
ENV GRADLE_HOME /opt/gradle  
RUN wget
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \  
&& unzip -d /opt/ gradle-${GRADLE_VERSION}-bin.zip \  
&& mv /opt/gradle-${GRADLE_VERSION} ${GRADLE_HOME} \  
&& rm gradle-${GRADLE_VERSION}-bin.zip  
  
# Setup environment  
ENV PATH ${PATH}:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools/bin:${ANDROID_HOME}/ndk-bundle:${GRADLE_HOME}/bin  
RUN curl https://storage.googleapis.com/git-repo-downloads/repo >
/usr/bin/repo  
RUN chmod a+x /usr/bin/repo  
  
# Install sdk components  
RUN yes | sdkmanager --licenses  
RUN sdkmanager --update --verbose  
RUN sdkmanager \  
"build-tools;19.1.0" \  
"build-tools;23.0.3" \  
"build-tools;25.0.3" \  
"build-tools;26.0.2" \  
"extras;android;m2repository" \  
"platform-tools" \  
"platforms;android-26" \  
"platforms;android-25" \  
"platforms;android-23" \  
"platforms;android-19" \  
"platforms;android-8"  
#"ndk-bundle" \  
# the ndk-bundle vr15b doesn't compile out code, force r14  
RUN wget -q https://dl.google.com/android/repository/android-
ndk-r14b-linux-x86_64.zip \  
&& unzip -q -d ${ANDROID_HOME} android-ndk-r14b-linux-x86_64.zip \  
&& mv ${ANDROID_HOME}/android-ndk-r14b ${ANDROID_HOME}/ndk-bundle \  
&& rm android-ndk-r14b-linux-x86_64.zip && sdkmanager --list  

