FROM openjdk:8  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
  
# ------------------------------------------------------  
# --- Install required tools  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends \  
wget \  
unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
# ------------------------------------------------------  
# --- Download Android SDK tools into $ANDROID_HOME  
RUN cd /opt && wget -q
https://dl.google.com/android/repository/tools_r25.2.5-linux.zip -O android-
sdk-tools.zip && \  
cd /opt && unzip -q android-sdk-tools.zip && \  
mkdir -p ${ANDROID_HOME} && \  
cd /opt && mv tools/ ${ANDROID_HOME}/tools/ && \  
cd /opt && rm -f android-sdk-tools.zip  
  
RUN echo y | android update sdk --no-ui --all \--filter platform-tools | grep
'package installed' && \  
echo y | android update sdk --no-ui --all \--filter android-25 | grep 'package
installed' && \  
echo y | android update sdk --no-ui --all \--filter build-tools-25.0.2 | grep
'package installed' && \  
echo y | android update sdk --no-ui --all \--filter extra-android-m2repository
| grep 'package installed' && \  
echo y | android update sdk --no-ui --all \--filter extra-google-m2repository
| grep 'package installed' && \  
echo y | android update sdk --no-ui --all \--filter extra-google-
google_play_services | grep 'package installed'  
  
# --- Install fastlane  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends \  
build-essential git-core ruby ruby-dev \  
&& gem install fastlane --no-ri \--no-rdoc \  
&& fastlane --version \  
&& apt-get remove \--purge -y \  
build-essential git-core ruby ruby-dev \  
&& rm -rf /var/lib/apt/lists/*  

