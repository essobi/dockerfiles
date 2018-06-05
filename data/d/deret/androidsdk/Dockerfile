FROM openjdk:8-jdk  
  
ENV ANDROID_SDK_TOOLS 3859397  
ENV ANDROID_COMPILE_SDK 25  
ENV ANDROID_BUILD_TOOLS 25.0.3  
RUN apt-get update \  
&& apt-get install -y lib32stdc++6 lib32z1  
  
RUN mkdir /androidsdk \  
&& cd /androidsdk \  
&& wget -O tools.zip https://dl.google.com/android/repository/sdk-tools-
linux-${ANDROID_SDK_TOOLS}.zip \  
&& unzip tools.zip  
  
RUN cd /androidsdk \  
&& echo y | ./tools/bin/sdkmanager "tools" \  
&& echo y | ./tools/bin/sdkmanager "platform-tools" \  
&& echo y | ./tools/bin/sdkmanager "platforms;android-${ANDROID_COMPILE_SDK}"
\  
&& echo y | ./tools/bin/sdkmanager "build-tools;${ANDROID_BUILD_TOOLS}"  
  
ENV ANDROID_HOME /androidsdk  
ENV PATH $PATH:/androidsdk/platform-tools  
  
ENTRYPOINT /bin/bash  

