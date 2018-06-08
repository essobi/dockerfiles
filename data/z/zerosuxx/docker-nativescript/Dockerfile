FROM thedrhax/android-sdk:latest  
MAINTAINER Tamas Mohos <tomi@mohos.name>  
  
#ENV DEBIAN_FRONTEND="noninteractive"  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN $ANDROID_HOME/tools/bin/sdkmanager --verbose "tools" "platform-tools"
"platforms;android-26" "build-tools;26.0.2" "extras;android;m2repository"
"extras;google;m2repository"  
  
USER root  
RUN apt-get update \  
&& curl -sL https://deb.nodesource.com/setup_10.x | bash -  
  
RUN apt-get -y install apt-transport-https unzip usbutils nodejs --no-install-
recommends  
  
# NativeScript  
RUN npm install -g nativescript --unsafe-perm  
  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["/docker-entrypoint.sh"]  

