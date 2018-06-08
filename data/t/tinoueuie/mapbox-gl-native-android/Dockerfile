FROM manabugt/android:latest  
  
RUN apt-get install -y make git build-essential automake \  
libtool make cmake pkg-config lib32stdc++6 lib32z1  
  
#Might be better to run "apt-get install oracle-java7-set-default" instead.  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
  
ENV ANDROID_NDK_PATH /opt/android-ndk  
  
#Already set by base image  
#ENV ANDROID_HOME /opt/android-sdk  
  
# Just to make sure. Already done by base image  
WORKDIR /opt/workspace  
  
  

