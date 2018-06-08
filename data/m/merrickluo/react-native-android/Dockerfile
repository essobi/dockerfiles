FROM openjdk:8  
#install nodejs  
ENV NODE_URL https://nodejs.org/dist/v7.8.0/node-v7.8.0-linux-x64.tar.gz  
  
RUN curl -L $NODE_URL | tar -zxvf- -C /opt/  
  
ENV PATH $PATH:/opt/node-v7.8.0-linux-x64/bin  
  
# install yarn  
ENV YARN_VERSION 0.24.4  
RUN npm install -g yarn  
  
#install android sdk  
ENV ANDROID_SDK_URL https://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip  
  
RUN mkdir -p /opt/android-sdk && \  
curl $ANDROID_SDK_URL -o sdk.zip && \  
unzip sdk.zip -d /opt/android-sdk && \  
rm sdk.zip  
  
ENV ANDROID_HOME /opt/android-sdk  
ENV PATH $PATH:$ANDROID_HOME/tools  
ENV PATH $PATH:$ANDROID_HOME/tools/bin  
  
RUN yes | sdkmanager --licenses && \  
sdkmanager "platform-tools" "extras;android;m2repository"
"platforms;android-23" "build-tools;23.0.1"  
  
# android build tool needed  
RUN apt-get update && apt-get install -y lib32stdc++6 lib32z1 jq  

