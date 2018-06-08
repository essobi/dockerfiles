FROM openjdk:8-jdk  
  
RUN apt-get \--quiet update \--yes  
RUN apt-get \--quiet install --yes wget tar unzip lib32stdc++6 lib32z1  
RUN wget --quiet --output-document=android-sdk.tgz
https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz  
RUN tar --extract --gzip --file=android-sdk.tgz  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
\--filter android-26  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
\--filter platform-tools  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
\--filter build-tools-26.0.2  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
\--filter extra-android-m2repository  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
\--filter extra-google-google_play_services  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
\--filter extra-google-m2repository  
ENV ANDROID_HOME=$PWD/android-sdk-linux  
ENV PATH=$PATH:$PWD/android-sdk-linux/platform-tools/  
  
RUN wget -q --output-document=android-ndk.zip
https://dl.google.com/android/repository/android-ndk-r16-linux-x86_64.zip && \  
unzip android-ndk.zip && \  
rm -f android-ndk.zip && \  
mv android-ndk-r16 android-ndk-linux  
ENV ANDROID_NDK=$PWD/android-ndk-linux  
ENV ANDROID_NDK_HOME=$PWD/android-ndk-linux  
  
  
  
RUN wget --quiet --output-document=android-wait-for-emulator
https://raw.githubusercontent.com/travis-ci/travis-
cookbooks/0f497eb71291b52a703143c5cd63a217c8766dc9/community-
cookbooks/android-sdk/files/default/android-wait-for-emulator  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
\--filter sys-img-x86-google_apis-26  
RUN echo no | android-sdk-linux/tools/android create avd -n test -t android-26
\--abi google_apis/x86  
RUN chmod +x ./android-wait-for-emulator  
  
  
  

