FROM jetbrains/teamcity-agent:9.1.7  
MAINTAINER Tixif devops@tixif.com  
  
#=============================================================================#  
RUN apt-get update && apt-get install -y \  
lib32ncurses5 \  
lib32gomp1 \  
lib32z1-dev \  
lib32ncurses5 \  
lib32gomp1 \  
lib32z1-dev \  
build-essential  
  
# Setup git to use https  
RUN git config --global url."https://".insteadOf git://  
  
#=============================================================================#  
# Setup NVM  
ENV NVM_DIR /opt/nvm  
RUN git clone https://github.com/creationix/nvm.git "${NVM_DIR}" && \  
cd "${NVM_DIR}" && \  
git checkout `git describe --abbrev=0 --tags`  
RUN echo "[[ -s $NVM_DIR/nvm.sh ]] && . $NVM_DIR/nvm.sh" >> ~/.bashrc  
  
## Install stable version  
RUN . $NVM_DIR/nvm.sh && nvm install stable  
  
#=============================================================================#  
# Download and untar SDK  
ENV ANDROID_SDK_URL http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz  
RUN curl -L "${ANDROID_SDK_URL}" | tar --no-same-owner -xz -C /opt  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV ANDROID_SDK /opt/android-sdk-linux  
ENV PATH ${ANDROID_HOME}/tools:$ANDROID_HOME/platform-tools:$PATH  
  
## Install Android SDK components  
ENV ANDROID_COMPONENTS platform-tools,build-tools-23.0.2,build-
tools-23.0.3,android-23  
ENV GOOGLE_COMPONENTS extra-android-m2repository,extra-google-m2repository  
RUN echo y | android update sdk --no-ui --all --filter "${ANDROID_COMPONENTS}"
; \  
echo y | android update sdk --no-ui --all --filter "${GOOGLE_COMPONENTS}"  
  
# Download gradle  
ENV GRADLE_DISTRIBUTION gradle-2.2.1-all.zip  
ENV GRADLE_DISTRIBUTION_URL
http://services.gradle.org/distributions/"${GRADLE_DISTRIBUTION}"  
RUN mkdir -p /opt/gradle  
RUN curl -L "${GRADLE_DISTRIBUTION_URL}" -o
/opt/gradle/"${GRADLE_DISTRIBUTION}"  
  
## Setup cordova path relative to agent's working directory  
ENV CORDOVA_ANDROID_GRADLE_DISTRIBUTION_URL
../../../../../../../gradle/"${GRADLE_DISTRIBUTION}"  
#=============================================================================#  

