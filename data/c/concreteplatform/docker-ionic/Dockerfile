FROM node:8-stretch  
  
RUN apt-get update &&\  
apt-get install -y locales ruby-full python-pip software-properties-common
openjdk-8-jdk gradle &&\  
apt-get clean  
  
RUN pip install awscli --upgrade --user  
ENV PATH=~/.local/bin:$PATH  
  
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG=en_US.UTF-8  
RUN npm install -g npm@latest  
RUN npm install -g ionic@2 code-push-cli cordova@6  
RUN gem install fastlane -NV  
  
# Install Android SDK  
RUN wget https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz && \  
tar -xvzf android-sdk_r24.4.1-linux.tgz && \  
mv android-sdk-linux /usr/local/android-sdk && \  
rm android-sdk_r24.4.1-linux.tgz  
  
ENV ANDROID_COMPONENTS platform-tools,android-23,build-tools-23.0.2,build-
tools-24.0.0  
# Install Android tools  
RUN echo y | /usr/local/android-sdk/tools/android update sdk --filter
"${ANDROID_COMPONENTS}" \--no-ui -a  
  
# Install Gradle  
RUN wget https://services.gradle.org/distributions/gradle-4.7-bin.zip && \  
mkdir /opt/gradle && \  
unzip -d /opt/gradle gradle-4.7-bin.zip  
ENV PATH=$PATH:/opt/gradle/gradle-4.7/bin  
  
# Install Android NDK  
RUN wget http://dl.google.com/android/repository/android-
ndk-r12-linux-x86_64.zip && \  
unzip android-ndk-r12-linux-x86_64.zip && \  
mv android-ndk-r12 /usr/local/android-ndk && \  
rm android-ndk-r12-linux-x86_64.zip  
  
# Environment variables  
ENV ANDROID_HOME /usr/local/android-sdk  
ENV ANDROID_SDK_HOME $ANDROID_HOME  
ENV ANDROID_NDK_HOME /usr/local/android-ndk  
ENV JENKINS_HOME $HOME  
ENV PATH ${INFER_HOME}/bin:${PATH}  
ENV PATH $PATH:$ANDROID_SDK_HOME/tools  
ENV PATH $PATH:$ANDROID_SDK_HOME/platform-tools  
ENV PATH $PATH:$ANDROID_SDK_HOME/build-tools/23.0.2  
ENV PATH $PATH:$ANDROID_SDK_HOME/build-tools/24.0.0  
ENV PATH $PATH:$ANDROID_NDK_HOME  
  
# Export JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/  
  
# Support Gradle  
ENV TERM dumb  
ENV JAVA_OPTS "-Xms4096m -Xmx4096m"  
ENV GRADLE_OPTS "-XX:+UseG1GC -XX:MaxGCPauseMillis=1000"  
ENTRYPOINT ["/bin/bash"]  

