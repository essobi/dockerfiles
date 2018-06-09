FROM node  
  
# Same as "export TERM=dumb"; prevents error "Could not open terminal for
stdout: $TERM not set"  
ENV TERM linux  
  
RUN apt-get update && apt-get -y install \  
software-properties-common \  
bzip2 unzip zip \  
openssh-client \  
curl \  
wget \  
vim \  
nano \  
git \  
git-core \  
apt-transport-https  
  
RUN \  
echo "===> add webupd8 repository..." && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
apt-get update  
  
RUN echo "===> install Java" && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes oracle-
java8-installer oracle-java8-set-default  
  
RUN echo "===> clean up..." && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Android SDK  
# Set up environment variables  
ENV SDK_HOME /opt/android-sdk  
ENV ANDROID_HOME /opt/android-sdk  
ENV SDK_URL https://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip  
ENV GRADLE_URL https://services.gradle.org/distributions/gradle-4.5.1-all.zip  
ENV ANDROID_BUILD_TOOLS_VERSION 27.0.3  
RUN echo "SDK_HOME: $SDK_HOME"  
RUN echo "ANDROID_BUILD_TOOLS_VERSION: $ANDROID_BUILD_TOOLS_VERSION"  
  
WORKDIR /opt  
# Download Android SDK  
RUN mkdir "$SDK_HOME" .android \  
&& cd "$SDK_HOME" \  
&& curl --silent -o sdk.zip $SDK_URL \  
&& unzip sdk.zip \  
&& rm sdk.zip \  
&& yes | $SDK_HOME/tools/bin/sdkmanager --licenses  
  
ENV PATH="${SDK_HOME}/tools:${SDK_HOME}/tools/bin:${SDK_HOME}/platform-
tools:${PATH}"  
RUN touch /root/.android/repositories.cfg  
  
RUN echo 8933bad161af4178b1185d1a37fbf41ea5269c55 >
$ANDROID_HOME/licenses/android-sdk-license  
RUN echo d56f5187479451eabf01fb78af6dfcb131a6481e >>
$ANDROID_HOME/licenses/android-sdk-license  
RUN echo 84831b9409646a918e30573bab4c9c91346d8abd >
$ANDROID_HOME/licenses/android-sdk-preview-license  
  
RUN sdkmanager "tools" "platform-tools"  
RUN sdkmanager "build-tools;$ANDROID_BUILD_TOOLS_VERSION"  
## Android 8  
RUN sdkmanager "platforms;android-27" "platforms;android-26"  
## Android 7 and 6  
RUN sdkmanager "platforms;android-25" "platforms;android-24"
"platforms;android-23"  
## Android 5  
RUN sdkmanager "platforms;android-22" "platforms;android-21"  
## The next two lines provide Android 4 compatability to Jellybean (4.1)  
## Crosswalk does not support Ice Cream Sandwich (4.0)  
RUN sdkmanager "platforms;android-20" "platforms;android-19"  
RUN sdkmanager "platforms;android-18" "platforms;android-17"
"platforms;android-16"  
## Mavien libs for Gradle  
RUN sdkmanager "extras;android;m2repository" "extras;google;m2repository"  
  
RUN echo y | $SDK_HOME/tools/bin/sdkmanager "platforms;android-26"  
  
# Install Cordova and other useful globals  
RUN npm update && \  
npm install -g cordova@8.0.0 && \  
npm install -g phantomjs-prebuilt --unsafe-perm  
  
# Install Gradle  
RUN wget -q $GRADLE_URL -O gradle.zip \  
&& unzip gradle.zip \  
&& mv gradle-4.5.1 gradle \  
# && rm gradle.zip \  
&& mkdir /root/.gradle  
  
# Support Gradle  
ENV GRADLE_HOME /opt/gradle  
ENV PATH="${PATH}:${GRADLE_HOME}/bin"  
ENV JAVA_OPTS "-Xms512m -Xmx1536m"  
RUN echo "PATH: $PATH"  
RUN echo `which gradle`  
ENV CORDOVA_ANDROID_GRADLE_DISTRIBUTION_URL=file:///opt/gradle.zip  
  
RUN mkdir -p /tangerine/client/builds/apk  
  
ADD cordova /tangerine/client/builds/apk/  
WORKDIR /tangerine/client/builds/apk  
  
RUN cordova platform add android@7.0.0 && sleep 60  
RUN cordova plugin add cordova-plugin-whitelist --save && sleep 60  
RUN cordova plugin add cordova-plugin-geolocation --save && sleep 60  
RUN cordova plugin add cordova-plugin-camera --save && sleep 60  
RUN cordova plugin add cordova-plugin-file --save && sleep 60  
RUN cordova plugin add cordova-android-support-gradle-release --save && sleep
60  
RUN cordova plugin add cordova-hot-code-push-plugin --save && sleep 60  
RUN cordova build  
  
WORKDIR /tangerine/client  
  
# overwrite this with 'CMD []' in a dependent Dockerfile  
CMD ["/bin/bash"]  

