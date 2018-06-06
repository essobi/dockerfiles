FROM google/dart:2.0-dev  
MAINTAINER John Ryan <john.p.ryan4@gmail.com>  
LABEL Description="Dart SDK with content-shell"  
  
# Configuration  
ENV CHANNEL "dev"  
ENV SDK_VERSION "2.0.0-dev.32.0"  
ENV DARTIUM_VERSION "1.24.2"  
ENV ARCHIVE_URL "https://storage.googleapis.com/dart-
archive/channels/$CHANNEL/release/$SDK_VERSION"  
ENV PATH $PATH:/usr/lib/dart/bin  
  
# Install third-party dependencies.  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu precise main multiverse" \  
>> /etc/apt/sources.list  
RUN apt-get update; echo 'true'  
RUN apt-get install -y --force-yes git wget unzip xvfb chromedriver
libgconf-2-4  
  
# https://github.com/dart-lang/sdk/issues/28549#issuecomment-277534958  
RUN apt-get install -y --force-yes gdb  
  
RUN apt-get clean  
  
# Download the SDK.  
RUN wget $ARCHIVE_URL/sdk/dartsdk-linux-x64-release.zip  
RUN unzip dartsdk-linux-x64-release.zip  
RUN cp -r dart-sdk/* /usr/local  
RUN rm -rf dartsdk-linux-x64-release.zip  
  
# Install Content Shell.  
# RUN wget $ARCHIVE_URL/dartium/content_shell-linux-x64-release.zip  
# RUN unzip content_shell-linux-x64-release.zip  
# RUN rm content_shell-linux-x64-release.zip  
# ENV PATH /drt-lucid64-full-$CHANNEL-$DARTIUM_VERSION.0:$PATH  
# RUN ln -s /content-shell_i/content_shell /usr/local/bin/content_shell  
# Install Dartium.  
# RUN wget $ARCHIVE_URL/dartium/dartium-linux-x64-release.zip  
# RUN unzip dartium-linux-x64-release.zip  
# RUN ln -s /dartium-linux-x64-stable-$DARTIUM_VERSION.0/chrome
/usr/local/bin/dartium  

