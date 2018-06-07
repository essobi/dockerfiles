FROM ubuntu:14.04  
MAINTAINER Kyle Brock "kylejbrock@gmail.com"  
# Install java8  
RUN apt-get update && apt-get install -y software-properties-common && add-
apt-repository -y ppa:webupd8team/java && apt-get update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer  
RUN apt-get update && apt-get install -y git-core qemu-kvm libvirt-bin ubuntu-
vm-builder bridge-utils libgl1-mesa-dev  
  
# Install Base Packages  
RUN dpkg --add-architecture i386 && \  
apt-get update -y && \  
apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 expect
curl build-essential python-dev libssl-dev libffi-dev python-pip libxml2-dev
&& \  
rm -rf /var/lib/apt/lists/* && \  
apt-get autoremove -y && \  
apt-get clean  
  
# Install Python Deps  
RUN pip install -U pip  
RUN pip install -U setuptools  
RUN pip install -U boto  
RUN pip install -U httplib2  
RUN pip install -U packaging  
RUN pip install -U pyOpenSSL  
RUN pip install google-api-python-client  
RUN pip install -U oauth2client==1.5.2  
  
# License Util  
RUN curl -L -o /tmp/accept-licenses https://github.com/embarkmobile/android-
sdk-installer/raw/version-2/accept-licenses  
RUN chmod u+x /tmp/accept-licenses  
  
# Installs Android SDK  
ENV ANDROID_SDK_FILENAME android-sdk_r24.4.1-linux.tgz  
ENV ANDROID_SDK_URL http://dl.google.com/android/${ANDROID_SDK_FILENAME}  
ENV ANDROID_API_LEVELS
android-15,android-16,android-17,android-18,android-19,android-20,android-21,android-22,android-23,android-24,android-25  
ENV ANDROID_BUILD_TOOLS_VERSION_25_1 25.0.1  
ENV ANDROID_BUILD_TOOLS_VERSION_25 25.0.0  
ENV ANDROID_BUILD_TOOLS_VERSION_24_2 24.0.2  
ENV ANDROID_BUILD_TOOLS_VERSION_24_1 24.0.1  
ENV ANDROID_BUILD_TOOLS_VERSION_23_3 23.0.3  
ENV ANDROID_BUILD_TOOLS_VERSION_23_2 23.0.2  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
RUN cd /opt && \  
wget -q ${ANDROID_SDK_URL} && \  
tar -xzf ${ANDROID_SDK_FILENAME} && \  
rm ${ANDROID_SDK_FILENAME} && \  
/tmp/accept-licenses "android update sdk --no-ui -a --filter tools,platform-
tools,${ANDROID_API_LEVELS},build-
tools-${ANDROID_BUILD_TOOLS_VERSION_25},build-
tools-${ANDROID_BUILD_TOOLS_VERSION_24_1},build-
tools-${ANDROID_BUILD_TOOLS_VERSION_24_2},build-
tools-${ANDROID_BUILD_TOOLS_VERSION_25_1},build-
tools-${ANDROID_BUILD_TOOLS_VERSION_23_3},build-
tools-${ANDROID_BUILD_TOOLS_VERSION_23_2},extra-android-m2repository,extra-
google-m2repository" "android-sdk-license-ed0d0a5b|android-sdk-
license-5be876d5|android-sdk-license-c81a61d9"  
  
RUN /tmp/accept-licenses "android update sdk -a -u -t sys-img-x86-android-24"
"android-sdk-license-ed0d0a5b|android-sdk-license-5be876d5|android-sdk-
license-c81a61d9"  
  
RUN echo no | android create avd --force -n test -t android-24  
  
ENV HOME /root  
ENV SHELL /bin/bash  
ADD start-emulator /usr/local/bin/  
  
RUN chmod u+x /usr/local/bin/start-emulator  

