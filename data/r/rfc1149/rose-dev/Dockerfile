FROM debian:stretch  
MAINTAINER Samuel Tardieu <sam@rfc1149.net>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Add backports and testing  
RUN echo "deb http://ftp.debian.org/debian stretch-backports main" >>
/etc/apt/sources.list  
RUN echo "deb http://ftp.debian.org/debian testing main" >>
/etc/apt/sources.list  
ADD testing.pref /etc/apt/preferences.d/  
  
# Add Java 8 download environment  
RUN apt-get -qq update && apt-get -y install gnupg2  
ADD webupd8team-java.list /etc/apt/sources.list.d/  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
# Install packages  
RUN apt-get -qq update  
RUN apt-get -y dist-upgrade  
RUN apt-get --no-install-recommends -y install \  
build-essential ca-certificates clang clang-format cmake curl git g++ python \  
gcc-arm-none-eabi binutils-arm-none-eabi gdb-arm-none-eabi \  
libstdc++-arm-none-eabi-newlib \  
libnewlib-arm-none-eabi ccache arduino-mk autoconf automake libmysqlcppconn-
dev virtualenv \  
unzip libpq-dev python3-dev postgresql sudo \  
oracle-java8-installer oracle-java8-set-default \  
python3-pip python3-pep8 python3-pyqt4 && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Build Criterion  
RUN (cd /tmp && git clone https://github.com/Snaipe/Criterion && \  
cd Criterion && git submodule update --init && mkdir build && cd build && \  
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .. && make && make install && \  
cd /tmp && rm -rf Criterion)  
  
# Include rust through rustup  
RUN curl https://sh.rustup.rs -sSf | sh -s -- --default-toolchain stable -y  
ENV PATH=/root/.cargo/bin:$PATH  
  
# Install Android SDK  
ENV ANDROID_BUILD_TOOLS_BOOTSTRAP_VERSION=25.2.4 \  
ANDROID_HOME=/opt/android-sdk-linux  
ENV PATH=${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
RUN cd /opt && \  
wget -q
https://dl.google.com/android/repository/tools_r${ANDROID_BUILD_TOOLS_BOOTSTRAP_VERSION}-linux.zip
&& \  
mkdir android-sdk-linux && \  
cd android-sdk-linux && \  
unzip ../tools_r${ANDROID_BUILD_TOOLS_BOOTSTRAP_VERSION}-linux.zip && \  
rm ../tools_r${ANDROID_BUILD_TOOLS_BOOTSTRAP_VERSION}-linux.zip  
ENV ANDROID_API_LEVELS=android-26,android-27 \  
ANDROID_BUILD_TOOLS_VERSION=27.0.1  
RUN echo y | android update sdk --no-ui -a --filter platform-
tools,${ANDROID_API_LEVELS},extra-android-support,extra-
android-m2repository,extra-google-m2repository,build-
tools-${ANDROID_BUILD_TOOLS_VERSION}  

