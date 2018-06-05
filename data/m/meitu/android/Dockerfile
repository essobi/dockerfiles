FROM meitu/android-base:latest  
LABEL maintainer "Ligboy.Liu <ligboy@gmail.com>"  
  
ENV ANDROID_HOME /opt/android-sdk  
  
# ------------------------------------------------------  
# --- Download Android SDK tools into $ANDROID_HOME  
#RUN cd /opt && wget -q
https://dl.google.com/android/repository/tools_r25.2.5-linux.zip -O android-
sdk-tools.zip  
# sdk-tools-linux-3773319.zip -> tools_r25.3.1  
RUN mkdir -p ${ANDROID_HOME}  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  
RUN cd /opt \  
&& wget -q https://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip -O android-sdk-tools.zip \  
&& unzip -qq android-sdk-tools.zip \  
&& mv tools/ ${ANDROID_HOME}/tools/ \  
&& rm -f android-sdk-tools.zip \  
# Accept all licenses before installing components.  
&& yes | sdkmanager --licenses \  
&& sdkmanager "tools"  
# ------------------------------------------------------  
# --- Install Android SDKs and other build packages  
# build tools  
RUN sdkmanager "build-tools;21.1.2"  
RUN sdkmanager "build-tools;22.0.1"  
RUN sdkmanager "build-tools;23.0.1"  
RUN sdkmanager "build-tools;23.0.2"  
RUN sdkmanager "build-tools;23.0.3"  
RUN sdkmanager "build-tools;24.0.1"  
RUN sdkmanager "build-tools;24.0.2"  
RUN sdkmanager "build-tools;24.0.3"  
RUN sdkmanager "build-tools;24.0.0"  
RUN sdkmanager "build-tools;25.0.0"  
RUN sdkmanager "build-tools;25.0.1"  
RUN sdkmanager "build-tools;25.0.2"  
RUN sdkmanager "build-tools;25.0.3"  
RUN sdkmanager "build-tools;26.0.0"  
RUN sdkmanager "build-tools;26.0.1"  
RUN sdkmanager "build-tools;26.0.2"  
RUN sdkmanager "build-tools;26.0.3"  
RUN sdkmanager "build-tools;27.0.0"  
RUN sdkmanager "build-tools;27.0.1"  
RUN sdkmanager "build-tools;27.0.2"  
RUN sdkmanager "build-tools;27.0.3"  
  
# Constraint Layout  
RUN sdkmanager "extras;m2repository;com;android;support;constraint;constraint-
layout-solver;1.0.0"  
RUN sdkmanager "extras;m2repository;com;android;support;constraint;constraint-
layout-solver;1.0.1"  
RUN sdkmanager "extras;m2repository;com;android;support;constraint;constraint-
layout-solver;1.0.2"  
  
RUN sdkmanager "extras;m2repository;com;android;support;constraint;constraint-
layout;1.0.0"  
RUN sdkmanager "extras;m2repository;com;android;support;constraint;constraint-
layout;1.0.1"  
RUN sdkmanager "extras;m2repository;com;android;support;constraint;constraint-
layout;1.0.2"  
  
# NDK dependency, Convenient for updating. cmake only about 30MiB.  
RUN sdkmanager "cmake;3.6.4111459"  
  
# SDKs  
RUN sdkmanager "platforms;android-21"  
RUN sdkmanager "platforms;android-22"  
RUN sdkmanager "platforms;android-23"  
RUN sdkmanager "platforms;android-24"  
RUN sdkmanager "platforms;android-25"  
RUN sdkmanager "platforms;android-26"  
RUN sdkmanager "platforms;android-27"  
  
# google apis  
RUN sdkmanager "add-ons;addon-google_apis-google-21"  
RUN sdkmanager "add-ons;addon-google_apis-google-22"  
RUN sdkmanager "add-ons;addon-google_apis-google-23"  
RUN sdkmanager "add-ons;addon-google_apis-google-24"  
  
# Platform tools  
RUN sdkmanager "platform-tools"  
  
# Extras  
RUN sdkmanager "extras;android;m2repository"  
RUN sdkmanager "extras;google;m2repository"  
RUN sdkmanager "extras;google;google_play_services"  
RUN sdkmanager "extras;google;instantapps"  
  
# Cleanup  
RUN apt-get clean -y && apt-get autoremove -y & rm -fr /var/lib/apt/lists/*
/tmp/* /var/tmp/* /var/cache/*  
  
# Go to workspace  
RUN mkdir -p /var/workspace  
WORKDIR /var/workspace  

