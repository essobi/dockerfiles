FROM jenkins:latest  
MAINTAINER jsonfry "jason@ocastastudios.com"  
USER root  
  
# Android And Other Dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends git expect
lib32stdc++6 lib32z1  
  
# Clean up  
RUN apt-get clean  
  
# Download And Extract Android SDK  
RUN cd /opt && curl -O http://dl.google.com/android/android-
sdk_r24.4.1-linux.tgz  
RUN cd /opt && tar xzf android-sdk_r24.4.1-linux.tgz  
RUN cd /opt && rm -f android-sdk_r24.4.1-linux.tgz  
RUN chmod -R +xr /opt/android-sdk-linux  
  
# Android SDK volumes so it doesn't get wiped on image updates  
VOLUME ["/opt/android-sdk-linux"]  
  
# Android SDK Paths  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  

