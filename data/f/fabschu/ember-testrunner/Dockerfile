FROM fabschu/ember-testrunner  
MAINTAINER Fabian Schulte <fabian.schulte@neomatt.de>  
  
RUN npm install -g cordova  
  
# From webratio/java  
RUN apt-get update -y && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update -y && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
apt-get remove software-properties-common -y && \  
apt-get autoremove -y && \  
apt-get clean  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# From webratio/android-sdk  
# Installs i386 architecture required for running 32 bit Android tools  
RUN dpkg --add-architecture i386 && \  
apt-get update -y && \  
apt-get install -y wget libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 &&
\  
rm -rf /var/lib/apt/lists/* && \  
apt-get autoremove -y && \  
apt-get clean  
  
RUN apt-get update -y && \  
apt-get install -y unzip  
  
ENV ANDROID_SDK_VERSION=r25.2.3  
ENV ANDROID_BUILD_TOOLS_VERSION=build-tools-25.0.3,build-tools-23.0.1  
ENV ANDROID_SDK_FILENAME=tools_${ANDROID_SDK_VERSION}-linux.zip  
ENV
ANDROID_SDK_URL=https://dl.google.com/android/repository/${ANDROID_SDK_FILENAME}  
ENV
ANDROID_API_LEVELS=android-15,android-16,android-17,android-18,android-19,android-20,android-21,android-22,android-23,android-24,android-25,android-26  
ENV ANDROID_HOME=/opt  
ENV PATH
${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:${PATH}  
  
RUN cd /opt && \  
curl -sSO ${ANDROID_SDK_URL} && \  
unzip -q ${ANDROID_SDK_FILENAME} && \  
rm -rf ${ANDROID_SDK_FILENAME} && \  
( sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) |
${ANDROID_HOME}/tools/android -s --clear-cache update sdk --no-ui --force
--all --filter tools,platform-tools,${ANDROID_BUILD_TOOLS_VERSION},extra-
android-support,${ANDROID_API_LEVELS},extra-android-m2repository,extra-
google-m2repository && \  
mkdir -p "$ANDROID_HOME/tools/licenses" && \  
echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" >
"$ANDROID_HOME/tools/licenses/android-sdk-license" && \  
echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" >
"$ANDROID_HOME/tools/licenses/android-sdk-preview-license"  
  
#install imagemagick  
RUN apt-get update  
RUN apt-get install -y \  
wget \  
imagemagick  
  
# Install Gradle  
RUN cd /usr/local/ && curl -L -O
https://services.gradle.org/distributions/gradle-3.3-all.zip && unzip -o
gradle-3.3-all.zip  
ENV GRADLE_HOME /usr/local/gradle-3.3  
ENV PATH $PATH:$GRADLE_HOME/bin  
RUN rm -rf /usr/local/gradle-3.3-all.zip  
  
RUN touch /root/.android/repositories.cfg  

