FROM ubuntu:17.04  
  
MAINTAINER matt@motionmobs.com  
  
  
# ------------------------------------------------------  
# --- Install required tools  
  
RUN apt-get update -qq \  
&& apt-get install -y openjdk-8-jdk wget expect git curl unzip lcov git-core
emacs-nox screen libstdc++6 lib32stdc++6 \  
&& apt-get clean  
  
# ------------------------------------------------------  
# --- Download Android SDK tools into $ANDROID_SDK_HOME  
  
RUN useradd -u 1000 -M -s /bin/bash android  
RUN chown 1000 /opt  
  
ENV ANDROID_SDK_HOME=/opt/android-sdk-linux  
ENV PATH $PATH:/opt/android-sdk-linux/platform-tools:/opt/android-sdk-
linux/tools/bin:/opt/android-sdk-
linux/tools:/opt/tools:/flutter/bin/cache/dart-sdk/bin:/flutter/bin  
  
USER android  
  
# Copy install tools  
COPY tools /opt/tools  
  
#Copy accepted android licenses  
COPY licenses /opt/licenses  
  
RUN mkdir -p /opt/android-sdk-linux  
  
RUN "/opt/tools/android-sdk-update.sh"  
  
USER root  
  
RUN echo "Creating Test AVD" && "/opt/tools/create-avd.sh"  
#flutter setup  
  
WORKDIR /  
  
RUN git clone https://github.com/flutter/flutter.git && \  
/flutter/bin/flutter doctor && \  
apt-get remove -y curl unzip && \  
apt autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
  
  
VOLUME ["/opt/android-sdk-linux"]  

