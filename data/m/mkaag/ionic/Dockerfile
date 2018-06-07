FROM mkaag/baseimage  
MAINTAINER Maurice Kaag <mkaag@me.com>  
  
#
-----------------------------------------------------------------------------  
# Environment variables  
#
-----------------------------------------------------------------------------  
ENV IONIC_VERSION 1.7.14  
ENV CORDOVA_VERSION 6.0.0  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:/opt/tools  
RUN echo ANDROID_HOME="${ANDROID_HOME}" >> /etc/environment  
  
#
-----------------------------------------------------------------------------  
# Pre-install  
#
-----------------------------------------------------------------------------  
RUN \  
apt-get update -qqy \  
&& dpkg --add-architecture i386 \  
&& apt-get update -qqy \  
&& apt-get install -qqy \  
python-software-properties \  
software-properties-common \  
expect \  
ant \  
wget \  
libc6-i386 \  
lib32stdc++6 \  
lib32gcc1 \  
lib32ncurses5 \  
lib32z1 \  
qemu-kvm \  
kmod  
  
RUN \  
add-apt-repository ppa:webupd8team/java -y \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
&& apt-get update -qqy \  
&& apt-get install -qqy oracle-java7-installer  
  
#
-----------------------------------------------------------------------------  
# Install  
#
-----------------------------------------------------------------------------  
RUN \  
apt-get update -qqy \  
&& apt-get install -y npm \  
&& ln -s /usr/bin/nodejs /usr/local/bin/node \  
&& npm update -g \  
&& npm install -g cordova@"$CORDOVA_VERSION" ionic@"$IONIC_VERSION" \  
&& npm install -g bplist-parser minimatch inherits path-is-absolute inflight
once \  
&& npm cache clean  
  
WORKDIR /opt  
RUN \  
wget --output-document=android-sdk.tgz --quiet
http://dl.google.com/android/android-sdk_r24.2-linux.tgz \  
&& tar xzf android-sdk.tgz \  
&& rm -f android-sdk.tgz  
  
#
-----------------------------------------------------------------------------  
# Post-install  
#
-----------------------------------------------------------------------------  
ADD build/android-accept-licenses.sh /opt/tools/android-accept-licenses.sh  
RUN chmod +x /opt/tools/android-accept-licenses.sh  
  
RUN ["/opt/tools/android-accept-licenses.sh", "android update sdk --all --no-
ui --filter platform-tools,build-tools-23.0.2,android-23,addon-
google_apis_x86-google-23,extra-android-support,extra-
android-m2repository,extra-google-m2repository,sys-img-x86-android-23"]  
  
WORKDIR /myApp  
EXPOSE 8100 35729  
CMD ["ionic", "serve", "8100", "35729"]  
  
#
-----------------------------------------------------------------------------  
# Clean up  
#
-----------------------------------------------------------------------------  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

