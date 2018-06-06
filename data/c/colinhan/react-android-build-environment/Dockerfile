FROM openjdk:8-jdk  
# Install required modules  
RUN apt-get \--quiet update \--yes && \  
apt-get \--quiet install \--yes wget tar unzip lib32stdc++6 lib32z1 && \  
rm -rf /var/lib/apt/lists/*  
  
# Install android-sdk;  
RUN wget \--quiet \--output-document=android-sdk.tgz
https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz && \  
tar \--extract \--gzip \--file=android-sdk.tgz  
  
# install node.js  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
  
# install yarn and other required modules  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get \--quiet update \--yes && \  
apt-get \--quiet install \--yes yarn build-essential && \  
rm -rf /var/lib/apt/lists/*  
  
# install react-native-cli  
RUN npm install -g react-native-cli  
  
# install specified versions of android sdk and others  
RUN echo y | /android-sdk-linux/tools/android \--silent update sdk \--no-ui
\--all \--filter android-25 && \  
echo y | /android-sdk-linux/tools/android \--silent update sdk \--no-ui \--all
\--filter android-24 && \  
echo y | /android-sdk-linux/tools/android \--silent update sdk \--no-ui \--all
\--filter android-23 && \  
echo y | /android-sdk-linux/tools/android \--silent update sdk \--no-ui \--all
\--filter platform-tools && \  
echo y | /android-sdk-linux/tools/android \--silent update sdk \--no-ui \--all
\--filter build-tools-25.0.2 && \  
echo y | /android-sdk-linux/tools/android \--silent update sdk \--no-ui \--all
\--filter build-tools-23.0.1 && \  
echo y | /android-sdk-linux/tools/android \--silent update sdk \--no-ui \--all
\--filter extra-android-m2repository  
  
ENV ANDROID_HOME=/android-sdk-linux  
ENV PATH=${PATH}:/android-sdk-linux/platform-tools/  

