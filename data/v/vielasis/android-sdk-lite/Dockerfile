FROM vielasis/ubuntu-base  
  
# Set android home  
ENV ANDROID_HOME /opt/android-sdk-linux  
  
# Copy additional tools  
COPY tools /opt/tools  
  
# Download additional packages  
RUN dpkg --add-architecture i386 \  
&& apt-get update -qq \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-8-jdk libc6:i386
libstdc++6:i386 libgcc1:i386 libncurses5:i386 libz1:i386 \  
&& rm -rf /var/lib/apt/lists/*  
  
# Download Android SDK  
RUN cd /opt && wget https://dl.google.com/android/android-
sdk_r24.4.1-linux.tgz -O android-sdk.tgz \  
&& tar -xzf android-sdk.tgz \  
&& rm -f android-sdk.tgz  
  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
# Update SDK  
RUN /opt/tools/accept_license.sh "android update sdk -u -a --filter platform-
tools,extra-android-
support,android-25,android-24,android-23,android-22,android-21" \  
&& /opt/tools/accept_license.sh "android update sdk -u -a --filter build-
tools-25.0.0,build-tools-24.0.3,build-tools-24.0.2,build-tools-24.0.1,build-
tools-24.0.0,build-tools-23.0.3,build-tools-23.0.2,build-tools-23.0.1,build-
tools-22.0.1,build-tools-21.1.2" \  
&& /opt/tools/accept_license.sh "android update sdk -u -a --filter extra-
android-m2repository,extra-google-m2repository,extra-google-
google_play_services,addon-google_apis-google-24,addon-google_apis-
google-23,addon-google_apis-google-22,addon-google_apis-google-21"  
  
# Version name  
ENV ANDROID_LITE_REV 1.0.0

