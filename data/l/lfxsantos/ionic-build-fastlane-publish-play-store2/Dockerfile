FROM niklasmerz/ionic-build-android-ci-docker:latest  
MAINTAINER Filipe Xavier  
  
ENV SUPPLY_VERSION=0.5.2  
  
RUN apt-get update && apt-get install -y ruby-full && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get autoremove -y && \  
apt-get clean  
  
RUN apt-get -qq update && apt-get -qq install -y less && \  
gem install supply:$SUPPLY_VERSION && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get autoremove -y && apt-get clean  
  
RUN echo 'y' | /opt/android-sdk-linux/tools/android update sdk -u -a -t
platform-tools,build-tools-25.0.2,android-25,extra-android-support,extra-
google-m2repository,extra-android-m2repository

