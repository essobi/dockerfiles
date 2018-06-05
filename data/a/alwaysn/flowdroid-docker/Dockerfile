FROM debian:latest  
MAINTAINER @FrenchYeti  
  
RUN useradd -ms /bin/bash flowdroid  
  
# Install all dependencies  
RUN apt-get update && \  
apt-get install -y unzip wget openjdk-8-jre-headless libc6-i386 lib32stdc++6
lib32z1 && \  
apt-get -y install bash-completion python2.7 python-dev python-protobuf
python-openssl python-twisted && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Setup Android sdk  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH $PATH:${ANDROID_HOME}/tools:$ANDROID_HOME/platform-tools  
  
RUN wget -qO- "http://dl.google.com/android/android-sdk_r24.3.4-linux.tgz" |
tar -zx -C /opt && \  
chown -R flowdroid:flowdroid /opt/android-sdk-linux && \  
echo y | /opt/android-sdk-linux/tools/android update sdk --no-ui --all
--filter platform-tools --force && \  
wget -q "https://dl.google.com/android/repository/platform-24_r02.zip" && \  
unzip platform-24_r02.zip -d $ANDROID_HOME/platforms/. && \  
chown -R flowdroid:flowdroid /opt/android-sdk-linux  
  
VOLUME /opt/flowdroid  
  
# Switch to flowdroid's home directory  
USER flowdroid  
WORKDIR /home/flowdroid  
  
# Download dependencies  
RUN wget -c 'https://soot-build.cs.uni-
paderborn.de/public/origin/develop/soot/soot-develop/build/sootclasses-
trunk.jar' && \  
wget -c 'https://github.com/secure-software-engineering/soot-
infoflow/releases/download/FlowDroid_1.5/soot-infoflow.jar' && \  
wget -c 'https://github.com/secure-software-engineering/soot-infoflow-
android/releases/download/FlowDroid_1.5/soot-infoflow-android.jar' && \  
wget -c
'http://central.maven.org/maven2/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar'
&& \  
wget -c
'http://central.maven.org/maven2/org/slf4j/slf4j-simple/1.7.5/slf4j-simple-1.7.5.jar'
&& \  
wget -c 'https://github.com/secure-software-engineering/soot-infoflow-
android/raw/develop/lib/axml-2.0.jar'  
  
# Download sinks, sources and callbacks  
RUN wget -c 'https://github.com/secure-software-engineering/soot-
infoflow/raw/develop/EasyTaintWrapperSource.txt' && \  
wget -c 'https://github.com/secure-software-engineering/soot-infoflow-
android/raw/develop/SourcesAndSinks.txt' && \  
wget -c 'https://github.com/secure-software-engineering/soot-infoflow-
android/raw/develop/AndroidCallbacks.txt'  
  
# Alias for Flowdroid  
RUN echo "alias flowdroid='java -Xmx4g -cp .:soot-trunk.jar:soot-
infoflow.jar:soot-infoflow-
android.jar:slf4j-api-1.7.5.jar:slf4j-simple-1.7.5.jar:axml-2.0.jar
soot.jimple.infoflow.android.TestApps.Test'" >> /home/flowdroid/.bashrc  

