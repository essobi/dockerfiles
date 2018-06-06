FROM ubuntu:16.04  
ENV ANDROID_HOME=/opt/android-sdk-linux  
  
COPY gradle /tmp/gradle  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
git \  
lib32stdc++6 \  
lib32z1 \  
openjdk-8-jdk \  
unzip \  
wget \  
curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip  
RUN URL=$(curl https://developer.android.com/studio/index.html | perl -nE
'm(href="([^"]+/sdk-tools-linux-[^"]+)") && say $1') \  
&& curl -o /tmp/sdk.zip "$URL" \  
&& mkdir -p $ANDROID_HOME \  
&& cd $ANDROID_HOME \  
&& unzip /tmp/sdk.zip \  
&& rm /tmp/sdk.zip  
  
COPY packages.lst /tmp/  
RUN yes | /opt/android-sdk-linux/tools/bin/sdkmanager --licenses \  
&& /opt/android-sdk-linux/tools/bin/sdkmanager
--package_file=/tmp/packages.lst  

