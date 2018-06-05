FROM ubuntu:16.04  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
  
ENV ANDROID_SDK_VERSION r24.4.1  
ENV ANDROID_BUILD_TOOLS_VERSION 23.0.3  
#  
# Install basic packages  
#  
RUN apt-get update  
RUN apt-get install -y software-properties-common build-essential curl  
  
#  
# Add repositories and update packages list  
#  
#RUN curl -sL https://deb.nodesource.com/setup_4.x | -E bash -  
#RUN apt-get update  
#  
# Install Git  
#  
RUN apt-get install -y git  
  
#  
# Install node.js  
#  
RUN apt-get install -y nodejs  
RUN ln -fs /usr/bin/nodejs /usr/bin/node  
  
#  
# Install ruby and packages  
#  
RUN apt-get install -y ruby ruby-dev  
  
# Set ruby to use utf-8  
ENV RUBYOPT "-KU -E utf-8:utf-8"  
# Install fastlane  
RUN gem install fastlane  
  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN \curl -L https://get.rvm.io | bash -s stable  
RUN /bin/bash -l -c "rvm requirements"  
RUN /bin/bash -l -c "rvm install 2.0"  
RUN /bin/bash -l -c "rvm install ruby --latest"  
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"  
RUN /bin/bash -l -c "gem install fastlane --no-rdoc --no-ri"  
RUN /bin/bash -l -c "ruby -v"  
  
#  
# Install android deps  
#  
RUN apt-get install -y openjdk-8-jdk wget  
  
RUN apt-get install -y git-core gnupg flex bison gperf build-essential \  
zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 \  
lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev ccache \  
libgl1-mesa-dev libxml2-utils xsltproc unzip  
  
# Installs Android SDK  
ENV ANDROID_SDK_FILENAME android-sdk_${ANDROID_SDK_VERSION}-linux.tgz  
ENV ANDROID_SDK_URL http://dl.google.com/android/${ANDROID_SDK_FILENAME}  
ENV ANDROID_API_LEVELS
android-15,android-16,android-17,android-18,android-19,android-20,android-21,android-22,android-23,22,28,147,140,151,139  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
RUN cd /opt && \  
wget -q ${ANDROID_SDK_URL} && \  
tar -xzf ${ANDROID_SDK_FILENAME} && \  
rm ${ANDROID_SDK_FILENAME} && \  
echo y | android update sdk --no-ui -a --filter tools,platform-
tools,${ANDROID_API_LEVELS},build-tools-${ANDROID_BUILD_TOOLS_VERSION}  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
  
#Graddle  
RUN mkdir -p ~/opt/packages/gradle && cd $_  
RUN wget https://services.gradle.org/distributions/gradle-2.13-bin.zip  
RUN unzip gradle-2.13-bin.zip  
  
RUN ln -s ~/opt/packages/gradle/gradle-2.13/ ~/opt/gradle  
  
ENV GRADLE_HOME $HOME/opt/gradle  
  
#  
# Clone CI tools  
#  
RUN git clone https://git.jazzy.pro/jazzy-ci-tools/ci-scripts.git /root/ci-
scripts  
RUN chmod a+x /root/ci-scripts/*  
ENV PATH /root/ci-scripts:$PATH  

