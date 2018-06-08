FROM runmymind/docker-android-sdk:ubuntu-standalone  
  
WORKDIR /  
  
RUN git clone https://github.com/flutter/flutter.git && ln -s
/flutter/bin/flutter /usr/bin/flutter  
  
RUN export PATH=$ANDROID_HOME/tools/bin:$PATH && \  
echo y | sdkmanager "tools" && \  
echo y | sdkmanager "platform-tools" && \  
echo y | sdkmanager "build-tools;26.0.3" && \  
echo y | sdkmanager "platforms;android-26" && \  
echo y | sdkmanager "extras;android;m2repository" && \  
echo y | sdkmanager "extras;google;m2repository" && \  
echo y | sdkmanager "patcher;v4" >/dev/null  
  
RUN flutter doctor  

