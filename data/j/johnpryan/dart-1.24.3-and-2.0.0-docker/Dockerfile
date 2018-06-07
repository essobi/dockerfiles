FROM google/dart:2.0-dev  
MAINTAINER John Ryan <john.p.ryan4@gmail.com>  
LABEL Description="Dart SDK with content-shell"  
  
# Configuration  
ENV CHANNEL stable  
ENV SDK_VERSION 1.24.3  
ENV ARCHIVE_URL https://storage.googleapis.com/dart-
archive/channels/$CHANNEL/release/$SDK_VERSION  
  
RUN apt-get update; echo 'true'  
RUN apt-get install -y --force-yes git wget unzip  
  
RUN wget $ARCHIVE_URL/sdk/dartsdk-linux-x64-release.zip  
RUN unzip dartsdk-linux-x64-release.zip  
RUN cp -r dart-sdk/* /usr/local  
RUN rm -rf dartsdk-linux-x64-release.zip  
  
RUN mv /dart-sdk dart-1-sdk  
  
#ENV PATH $PATH:/usr/lib/dart/bin  

