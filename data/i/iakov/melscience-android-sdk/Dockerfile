FROM runmymind/docker-android-sdk:latest  
MAINTAINER jake.kirilenko@gmail.com  
ENV _JAVA_OPTIONS="-Xmx3000m -XX:ParallelGCThreads=2 -XX:ConcGCThreads=2
-XX:ParallelGCThreads=2
-Djava.util.concurrent.ForkJoinPool.common.parallelism=2"  
ENV PATH="/opt/android-sdk-linux/platform-tools:/opt/android-sdk-
linux/tools/bin:/opt/android-sdk-linux/tools:/opt/android-sdk-
linux/bin:/usr/local/bin:$PATH"  
RUN curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash  
RUN apt-get update && apt-get full-upgrade -y  
RUN apt-get install -y git-lfs openssh-client  
  
RUN apt-get install git-lfs  
  
RUN sdkmanager "system-images;android-24;google_apis;armeabi-v7a" \  
"system-images;android-19;google_apis;armeabi-v7a" \  
"ndk-bundle" "platforms;android-27" \  
"cmake;3.6.4111459" \  
"lldb;3.0" \  
"platform-tools" \  
"emulator" \  
"build-tools;27.0.3"  
  
RUN echo no | avdmanager create avd -n testEmulator24 -k "system-
images;android-24;google_apis;armeabi-v7a"  
RUN echo no | avdmanager create avd -n testEmulator19 -k "system-
images;android-19;google_apis;armeabi-v7a"  
  
ENV ANDROID_HOME="/opt/android-sdk-linux"  
ENV ANDROID_NDK_HOME="/opt/android-sdk-linux/ndk-bundle"  

