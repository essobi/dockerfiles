FROM google/dart:1.24.3  
MAINTAINER John Ryan <john.p.ryan4@gmail.com>  
LABEL Description="Dart SDK with content-shell"  
  
# Configuration  
ENV CHANNEL stable  
ENV SDK_VERSION 1.24.3  
ENV ARCHIVE_URL https://storage.googleapis.com/dart-
archive/channels/$CHANNEL/release/$SDK_VERSION  
ENV PATH $PATH:/usr/lib/dart/bin  
  
# Install third-party dependencies.  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu precise main multiverse" \  
>> /etc/apt/sources.list  
RUN apt-get update; echo 'true'  
RUN apt-get install -y --force-yes git wget unzip xvfb chromedriver
libgconf-2-4 gdb  
  
# https://github.com/dart-lang/sdk/issues/28549#issuecomment-277534958  
RUN apt-get install -y --force-yes gdb  
  
RUN apt-get clean  
  
# Download the SDK.  
RUN wget $ARCHIVE_URL/sdk/dartsdk-linux-x64-release.zip  
RUN unzip dartsdk-linux-x64-release.zip  
RUN cp -r dart-sdk/* /usr/local  
RUN rm -rf dartsdk-linux-x64-release.zip  
  
# Install Content Shell.  
RUN wget $ARCHIVE_URL/dartium/content_shell-linux-x64-release.zip  
RUN unzip content_shell-linux-x64-release.zip  
RUN rm content_shell-linux-x64-release.zip  
ENV PATH /drt-lucid64-full-$CHANNEL-$SDK_VERSION.0:$PATH  
RUN ln -s /drt-linux-x64-stable-1.$SDK_VERSION.0/content_shell
/usr/local/bin/content_shell  
  
# Install Dartium.  
RUN wget $ARCHIVE_URL/dartium/dartium-linux-x64-release.zip  
RUN unzip dartium-linux-x64-release.zip  
RUN ln -s /dartium-linux-x64-stable-$SDK_VERSION.0/chrome
/usr/local/bin/dartium  
  
# Install Flutter.  
RUN cd / && git clone -b dev https://github.com/flutter/flutter.git  
ENV PATH=/flutter/bin:$PATH  
RUN flutter doctor  
RUN apt-get -y --force-yes install libstdc++6 fonts-droid  
RUN flutter doctor  
  
# https://circleci.com/docs/2.0/high-uid-error/  
RUN rm -rfv /flutter/bin/cache/artifacts/gradle_wrapper/  

