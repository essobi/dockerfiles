FROM ubuntu:14.04.4  
MAINTAINER Sofian Hadiwijaya "me@sofianhw.com"  
LABEL name=fb-redex  
LABEL version=1  
  
# Disable interactive package setup  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# Install Android needed pkgs  
RUN dpkg --add-architecture i386  
# RUN apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386
libgcc1:i386 zlib1g:i386 lib32z1  
# Install ReDex/Android needed pkgs  
RUN apt-get -y update  
RUN apt-get -y install \  
openjdk-7-jre \  
wget \  
git \  
g++ \  
automake \  
autoconf \  
autoconf-archive \  
libtool \  
libboost-all-dev \  
libevent-dev \  
libdouble-conversion-dev \  
libgoogle-glog-dev \  
libgflags-dev \  
liblz4-dev \  
liblzma-dev \  
libsnappy-dev \  
libjsoncpp-dev \  
make \  
zlib1g-dev \  
binutils-dev \  
libjemalloc-dev \  
libssl-dev \  
libiberty-dev \  
libc6:i386 \  
libncurses5:i386 \  
libstdc++6:i386 \  
libgcc1:i386 \  
zlib1g:i386 \  
lib32z1  
  
# Setup Android SDK env variables  
ENV ANDROID_SDK_FILENAME android-sdk_r24.4.1-linux.tgz  
ENV ANDROID_SDK_URL http://dl.google.com/android/${ANDROID_SDK_FILENAME}  
ENV ANDROID_BUILD_TOOLS_VERSION 23.0.3  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV ANDROID_SDK ${ANDROID_HOME}/build-tools/${ANDROID_BUILD_TOOLS_VERSION}  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:${ANDROID_SDK}  
  
# Download Android SDK  
RUN cd /opt && \  
wget -q ${ANDROID_SDK_URL} && \  
tar -xzf ${ANDROID_SDK_FILENAME} && \  
rm ${ANDROID_SDK_FILENAME} && \  
echo y | android update sdk --no-ui -a --filter build-
tools-${ANDROID_BUILD_TOOLS_VERSION}  
  
# Define working directory.  
WORKDIR /data  
  
# Download the repo  
RUN git clone https://github.com/facebook/redex.git  
  
# Move into redex  
WORKDIR /data/redex  
  
# Update submodules  
RUN git submodule update --init  
  
# Build Redex  
RUN autoreconf -ivf && ./configure && make && make install  
  
# Define default command.  
CMD ["bash"]  

