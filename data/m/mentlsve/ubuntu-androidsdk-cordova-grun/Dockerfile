# This Dockerfile is inspired by  
# https://registry.hub.docker.com/u/ugnb/ubuntu-cordova-android-build/  
# https://github.com/jenkinsci/docker/blob/master/Dockerfile  
FROM ubuntu:14.04  
ENV DL_DIR /tmp/downloads  
ENV ANDROID_SDK_DIST_URL http://dl.google.com/android/android-
sdk_r24.2-linux.tgz  
ENV ANDROID_SDK_DIST android-sdk.tgz  
ENV ANDROID_HOME_ROOT /android  
ENV ANDROID_SDK_VERSION 21  
RUN mkdir $ANDROID_HOME_ROOT  
ENV ANDROID_HOME $ANDROID_HOME_ROOT/sdk  
RUN mkdir $ANDROID_HOME  
  
RUN apt-get update  
RUN apt-get install -y wget default-jdk ant  
  
RUN mkdir $DL_DIR  
RUN wget -O $DL_DIR/$ANDROID_SDK_DIST $ANDROID_SDK_DIST_URL  
RUN tar -C $ANDROID_HOME -zxvf $DL_DIR/$ANDROID_SDK_DIST \--strip-components=1  
RUN rm -f $DL_DIR/$ANDROID_SDK_DIST  
  
RUN ( sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) |
$ANDROID_HOME/tools/android update sdk -u --filter platform-
tool,tool,android-$ANDROID_SDK_VERSION,extra,`$ANDROID_HOME/tools/android list
sdk --extended | grep -oE '"build-tools-[^"]+"' | grep -oE '[^"]+' | head -n1`  
  
RUN apt-get install -y nodejs git npm  
RUN ln -s "$(which nodejs)" /usr/bin/node  
  
RUN apt-get install -y lib32stdc++6 lib32z1 # `cordova build` will fail
without this  
  
RUN npm install -g cordova  
RUN npm install -g grunt-cli  
  
ENV JENKINS_HOME /var/lib/jenkins  
RUN mkdir $JENKINS_HOME  
  
RUN useradd -d "$JENKINS_HOME" -u 498 -m -s /bin/bash jenkins  
RUN chown -R jenkins $JENKINS_HOME  
RUN chown -R jenkins $ANDROID_HOME  
RUN chown -R jenkins $ANDROID_HOME_ROOT  
  
USER jenkins  
WORKDIR $JENKINS_HOME  
  
ENV PATH $PATH:$ANDROID_HOME/tools  
ENV PATH $PATH:$ANDROID_HOME/platform-tools  
ENV PATH $PATH:$ANDROID_HOME/build-tools  
  
ENV ANDROID_HOME $ANDROID_HOME_ROOT/sdk  

