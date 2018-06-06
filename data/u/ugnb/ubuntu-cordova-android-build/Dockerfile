FROM ubuntu:14.04  
#RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
ENV DL_DIR /tmp/downloads  
ENV ANDROID_SDK_DIST_URL http://dl.google.com/android/android-
sdk_r24.0.2-linux.tgz  
ENV ANDROID_SDK_DIST android-sdk.tgz  
ENV ANDROID_HOME_ROOT /android  
ENV ANDROID_SDK_VERSION 19  
ENV ANDROID_HOME $ANDROID_HOME_ROOT/sdk  
ENV PATH $PATH:$ANDROID_HOME/tools  
ENV PATH $PATH:$ANDROID_HOME/platform-tools  
ENV PATH $PATH:$ANDROID_HOME/build-tools  
  
  
RUN mkdir $DL_DIR  
RUN mkdir $ANDROID_HOME_ROOT  
RUN mkdir $ANDROID_HOME  
  
RUN apt-get update  
RUN apt-get install -y wget default-jdk ant  
  
RUN wget -O $DL_DIR/$ANDROID_SDK_DIST $ANDROID_SDK_DIST_URL  
RUN tar -C $ANDROID_HOME -zxvf $DL_DIR/$ANDROID_SDK_DIST \--strip-components=1  
RUN rm -f $DL_DIR/$ANDROID_SDK_DIST  
RUN ( sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) |
$ANDROID_HOME/tools/android update sdk -u --filter platform-
tool,tool,android-$ANDROID_SDK_VERSION,extra,`$ANDROID_HOME/tools/android list
sdk --extended | grep -oE '"build-tools-[^"]+"' | grep -oE '[^"]+' | head -n1`  
  
RUN apt-get install -y nodejs git npm  
RUN ln -s "$(which nodejs)" /usr/bin/node  
  
RUN apt-get install -y lib32stdc++6 lib32z1 # `codova build` will fail without
this  
RUN npm install -g cordova  

