FROM debian:jessie  
MAINTAINER Geoff Taylor <hub.docker.com@opinionatedgeek.com>  
  
# Update the system and install essential tools.  
RUN apt-get update && apt-get -yq install \  
automake \  
binutils \  
file \  
gcc \  
git \  
libncurses5-dev \  
make \  
sudo \  
vim \  
wget \  
xutils-dev  
  
ENV ANDROID_NDK_VERSION android-ndk-r10e  
  
# Set up a user for development.  
RUN groupadd -r developer && useradd -r -g developer --uid 1000 \--home
/home/developer --create-home developer && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
echo "export ANDROID_NDK_VERSION=\"${ANDROID_NDK_VERSION}\"" >>
/home/developer/.bashrc && \  
echo 'export ANDROID_API_VERSION="android-21"' >> /home/developer/.bashrc && \  
echo 'export ANDROID_TOOLCHAIN="arm-linux-androideabi"' >>
/home/developer/.bashrc && \  
echo 'export ANDROID_TOOLCHAIN_VERSION="${ANDROID_TOOLCHAIN}-4.9"' >>
/home/developer/.bashrc && \  
echo 'export ANDROID_API="${ANDROID_API_VERSION}"' >> /home/developer/.bashrc
&& \  
echo 'export ANDROID_NDK="/opt/${ANDROID_NDK_VERSION}"' >>
/home/developer/.bashrc && \  
echo 'export ANDROID_NDK_ROOT="${ANDROID_NDK}"' >> /home/developer/.bashrc &&
\  
echo 'export
TOOLCHAIN_VERSION_ROOT="${ANDROID_NDK}/toolchains/${ANDROID_TOOLCHAIN_VERSION}"'
>> /home/developer/.bashrc && \  
echo 'export
TOOLCHAIN_BIN="${TOOLCHAIN_VERSION_ROOT}/prebuilt/linux-x86_64/bin"' >>
/home/developer/.bashrc && \  
echo 'export CC="${TOOLCHAIN_BIN}/${ANDROID_TOOLCHAIN}-gcc"' >>
/home/developer/.bashrc && \  
echo 'export CXX="${TOOLCHAIN_BIN}/${ANDROID_TOOLCHAIN}-g++"' >>
/home/developer/.bashrc && \  
echo 'export LD="${TOOLCHAIN_BIN}/${ANDROID_TOOLCHAIN}-ld"' >>
/home/developer/.bashrc && \  
echo 'export AR="${TOOLCHAIN_BIN}/${ANDROID_TOOLCHAIN}-ar"' >>
/home/developer/.bashrc && \  
echo 'export RANLIB="${TOOLCHAIN_BIN}/${ANDROID_TOOLCHAIN}-ranlib"' >>
/home/developer/.bashrc && \  
echo 'export STRIP="${TOOLCHAIN_BIN}/${ANDROID_TOOLCHAIN}-strip"' >>
/home/developer/.bashrc && \  
echo 'export SYSROOT="${ANDROID_NDK}/platforms/${ANDROID_API_VERSION}/arch-
arm/"' >> /home/developer/.bashrc && \  
echo 'export CFLAGS="--sysroot=${SYSROOT}"' >> /home/developer/.bashrc && \  
echo 'export CXXFLAGS="--sysroot=${SYSROOT}"' >> /home/developer/.bashrc && \  
echo 'export CPPFLAGS="--sysroot=${SYSROOT}"' >> /home/developer/.bashrc && \  
echo 'export LDFLAGS="--sysroot=${SYSROOT}"' >> /home/developer/.bashrc && \  
echo 'export
PATH="${PATH}:${ANDROID_NDK}:${ANDROID_NDK}/toolchains:${TOOLCHAIN_BIN}"' >>
/home/developer/.bashrc && \  
chown developer:developer -R /home/developer && \  
. /home/developer/.profile  
  
# Set up the NDK  
RUN chmod a+w /opt && \  
cd /opt && \  
wget http://dl.google.com/android/ndk/${ANDROID_NDK_VERSION}-linux-x86_64.bin
&& \  
chmod a+x ${ANDROID_NDK_VERSION}-linux-x86_64.bin && \  
su -c ./${ANDROID_NDK_VERSION}-linux-x86_64.bin developer && \  
chmod a+w /opt  
  
ENV HOME /home/developer  
USER developer  
WORKDIR /home/developer  

