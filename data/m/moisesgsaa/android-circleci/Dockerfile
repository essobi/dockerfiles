FROM ubuntu:16.04  
RUN apt-get update  
  
# Install java8  
RUN apt-get install -y software-properties-common \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& apt-get update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 \  
select true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer  
  
# Install Deps  
RUN dpkg --add-architecture i386 && apt-get update \  
&& apt-get install -y --force-yes expect wget \  
libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 lib32z1  
  
# Install Android SDK  
RUN cd /opt && wget --output-document=android-sdk.tgz --quiet \  
http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz \  
&& tar xzf android-sdk.tgz && rm -f android-sdk.tgz \  
&& chown -R root.root android-sdk-linux  
  
# Setup environment  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
  
  
# Install sdk elements  
COPY tools /opt/tools  
ENV PATH ${PATH}:/opt/tools  
RUN ["/opt/tools/android-accept-licenses.sh", \  
"android update sdk --all --force --no-ui --filter platform-tools,tools,build-
tools-25,build-tools-25.0.0,android-25,addon-google_apis_x86-google-25,extra-
android-support,extra-android-m2repository,extra-google-m2repository,extra-
google-google_play_services,sys-img-armeabi-v7a-android-25"]  
  
# Add licences codes  
RUN mkdir "$ANDROID_HOME/licenses" || true \  
&& echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" >
"$ANDROID_HOME/licenses/android-sdk-license" \  
&& echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" >
"$ANDROID_HOME/licenses/android-sdk-preview-license"  
  
RUN apt-get install -y unzip  
  
# Install gradle  
RUN cd /opt && wget --output-document=gradle.zip \  
https://services.gradle.org/distributions/gradle-3.3-all.zip \  
&& unzip gradle.zip && rm -f gradle.zip \  
&& chown -R root.root gradle-3.3  
  
ENV GRADLE_HOME=/opt/gradle-3.3  
ENV PATH=$PATH:$GRADLE_HOME/bin  
  
# Cleaning  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Go to workspace  
RUN mkdir -p /opt/workspace  
WORKDIR /opt/workspace  

