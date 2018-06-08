FROM lissonpsantos2/debian-jessie-basic:latest  
  
MAINTAINER Alisson Pereira dos Santos <lissonpsantos2@gmail.com>  
  
#IMAGE VARIABLES  
ENV PROJECT_FOLDER /home/project-folder  
ENV IMAGE_ALIAS PHONEGAP  
ENV SEPARATOR -  
ENV INFO_IMAGE "go to ${PROJECT_FOLDER} and run phonegap"  
#ANDROID SDK CONFIGURATION VARIABLES  
ENV ANDROID_HOME /sdk  
ENV ANDROID_SDK_VERSION 3859397  
ENV ANDROID_SDK_FILENAME sdk-tools-linux-${ANDROID_SDK_VERSION}.zip  
ENV ANDROID_SDK_URL
https://dl.google.com/android/repository/${ANDROID_SDK_FILENAME}  
ENV ANDROID_API_LEVELS
android-15,android-16,android-17,android-18,android-19,android-20,android-21,android-22,android-23,android-24,android-25,android-26,android-27  
ENV ANDROID_HOME /sdk  
ENV ANDROID_BUILD_TOOLS_VERSION 27.0.3  
#GRADLE CONFIGURATION VARIABLES  
ENV GRADLE_HOME /opt/gradle  
ENV GRADLE_VERSION 4.5.1  
ENV GRADLE_FILENAME gradle-${GRADLE_VERSION}-bin.zip  
ENV GRADLE_URL https://services.gradle.org/distributions/${GRADLE_FILENAME}  
  
#COMMON VARIABLES  
ENV PATH ${PATH}:${GRADLE_HOME}/gradle-${GRADLE_VERSION}/bin  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
#CREATE FOLDERS  
RUN mkdir ${PROJECT_FOLDER}  
RUN mkdir ${ANDROID_HOME}  
RUN mkdir ${GRADLE_HOME}  
  
#UPDATE IMAGE  
RUN apt-get update  
RUN apt-get upgrade -y  
  
#INSTALL PACKAGES  
RUN apt-get install -y npm  
  
#INSTALL JAVA 1.8  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial
main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN apt-get update  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | sudo debconf-set-selections  
RUN apt-get -y install oracle-java8-installer  
  
#INSTALL NODE  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
RUN apt-get install -y nodejs  
RUN npm install -g n  
RUN n 8.*  
  
#INSTALL SDK DEPENDENCIES  
RUN cd ${ANDROID_HOME} && wget ${ANDROID_SDK_URL} && \  
unzip ${ANDROID_SDK_FILENAME} && rm ${ANDROID_SDK_FILENAME} && \  
yes | android update sdk --no-ui -a --filter tools,platform-
tools,${ANDROID_API_LEVELS},build-tools-${ANDROID_BUILD_TOOLS_VERSION}  
  
#INSTALL GRADLE  
RUN cd ${GRADLE_HOME} && wget ${GRADLE_URL} && \  
unzip -d /opt/gradle ${GRADLE_FILENAME} && rm ${GRADLE_FILENAME}  
  
#INSTALL UTILS  
RUN npm cache clean -f  
RUN npm install -g bower  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  
RUN npm install -g gulp  
RUN npm install -g phonegap  

