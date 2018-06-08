# Container for compiling businfo for Android  
#  
FROM debian:jessie  
MAINTAINER Mathias Monnerville <mathias@monnerville.com>  
  
# ia32 libs required for Android tools  
RUN dpkg --add-architecture i386  
RUN apt-get -qq update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y \  
python \  
git \  
vim \  
wget \  
sqlite3 \  
openjdk-7-jdk \  
ant \  
make \  
libncurses5:i386 \  
libstdc++6:i386 \  
zlib1g:i386  
  
# Install Go  
WORKDIR /usr/local  
RUN wget https://storage.googleapis.com/golang/go1.4.2.linux-amd64.tar.gz  
RUN tar xzf go1.4.2.linux-amd64.tar.gz  
  
# Install Android SDK  
RUN wget http://dl.google.com/android/android-sdk_r24.0.2-linux.tgz  
RUN tar xzf android-sdk_r24.0.2-linux.tgz  
RUN chown -R root:staff /usr/local/android-sdk-linux/  
RUN rm -f *.tgz *.tar.gz  
# Required distribution for building the Android application (android list sdk
--all)  
# 1: Android SDK Tools, revision 24.0.2  
# 2: Android SDK Platform-tools, revision 21  
# 3: Android SDK Build-tools, revision 21.1.2  
# 25: SDK Platform Android 4.1.2, API 16, revision 5  
# 85: Google APIs, Android API 16, revision 3  
# 113: Android Support Library, revision 21.0.3  
RUN echo yes | /usr/local/android-sdk-linux/tools/android update sdk -u -a -t
1,2,3,25,85,113  
  
RUN useradd -d /home/businfo -m -s /bin/bash businfo  
WORKDIR /home/businfo  
USER businfo  
RUN mkdir -p go/bin go/src go/pkg  
ENV PATH /usr/local/go/bin:/usr/local/android-sdk-
linux/tools:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
ENV TIMESTAMP 5  
RUN git clone https://github.com/gotsunami/businfo-tools.git  
RUN git clone https://github.com/gotsunami/businfo-sample-lines.git  
RUN git clone https://github.com/gotsunami/businfo-android.git  
ADD android-local.properties businfo-android/local.properties  
# Remove it  
ADD gmaps.properties businfo-android/gmaps.properties  
ADD tools-local.properties businfo-tools/local.properties  
  
VOLUME /home/businfo/businfo-android/bin  
  
WORKDIR /home/businfo/businfo-android  
ENTRYPOINT ["/usr/bin/ant"]  

