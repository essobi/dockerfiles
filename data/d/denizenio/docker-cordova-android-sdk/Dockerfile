FROM beevelop/cordova:latest  
  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y lib32stdc++6 lib32z1 nodejs git tar bzip2 python build-
essential jq ssh  
  
# Install Ruby.  
RUN \  
apt-get update && \  
apt-get install -y ruby-dev ruby  
  
# Latest NPM Node  
# RUN npm install -g npm@latest  
RUN npm cache clean --force  
  
# download and extract android sdk  
# RUN curl http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz | tar xz
-C /usr/local/  
RUN cd /usr/local/ \  
&& wget -q https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz -O
android-sdk.tgz \  
&& tar -xvzf android-sdk.tgz \  
&& rm -f android-sdk.tgz \  
&& chown -R root:root /usr/local  
  
ENV ANDROID_HOME /usr/local/android-sdk-linux  
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools  
  
# update and accept licences  
RUN ( sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) | /usr/local/android-
sdk-linux/tools/android update sdk --no-ui -a --filter platform-tool,build-
tools-25.0.2,build-tools-26.0.1,build-tools-26.0.2,android-25,android-26; \  
find /usr/local/android-sdk-linux -perm 0744 | xargs chmod 755  
  
RUN touch /root/.android/repositories.cfg  
  
# Install Fastlane (for CI deployments)  
RUN gem install fastlane --no-rdoc --no-ri  
  
# Upgrade Cordova to Latest  
RUN npm install -g ionic@latest  
RUN npm install -g --unsafe-perm cordova@latest  
RUN npm install -g cordova-lib@latest  
RUN npm install -g cordova-common@latest  
  
# Install Gulp and Bower  
RUN npm install -g gulp@latest  
RUN npm install -g bower@latest  
  
ENV GRADLE_USER_HOME /src/gradle  
VOLUME /src  
WORKDIR /src  
  
RUN npm install -g cordova@latest  

