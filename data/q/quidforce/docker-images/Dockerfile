FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
#DNS update: This is needed to run yum and to let the docker build process
access the internet.  
RUN "sh" "-c" "echo nameserver 8.8.8.8 >> /etc/resolv.conf"  
  
RUN apt-get update -y && \  
apt-get install -y git ssh tar gzip ca-certificates \  
wget curl xz-utils nano less unzip bzip2 pkg-config make autotools-dev
automake upx g++ zlib1g-dev \  
openssh-server gdb net-tools \  
nasm cmake texinfo python \  
sudo && \  
update-rc.d ssh defaults && \  
useradd --create-home --shell /bin/bash --groups sudo dev && \  
echo "dev:password" | chpasswd && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get autoremove -y && \  
apt-get clean  
  
RUN cd ~/ && \  
curl -s -O https://dl.google.com/android/repository/android-
ndk-r15c-linux-x86_64.zip && \  
unzip -q android-ndk-r15c-linux-x86_64.zip && \  
rm android-ndk-r15c-linux-x86_64.zip && \  
~/android-ndk-r15c/build/tools/make_standalone_toolchain.py --arch arm64 --api
21 --unified-headers --stl gnustl --install-dir /toolchain &&\  
rm -rf ~/android-ndk-r15c  
  
ENV PATH /toolchain/bin:${PATH}  
ENV build_dir /root/build  
ENV TARGET /toolchain/sysroot/  
  
ENV host aarch64-linux-android  
ENV cpu 4  
ENV CFLAGS "-D__ANDROID_API__=21 -fvisibility=hidden -fdata-sections
-ffunction-sections -fPIC -fPIE -I${TARGET}/usr/include -I${TARGET}/include"  
ENV CXXFLAGS "-D__ANDROID_API__=21 -fvisibility=hidden -fdata-sections
-ffunction-sections -fPIC -fPIE -I${TARGET}/usr/include -I${TARGET}/include"  
ENV CPPFLAGS "-D__ANDROID_API__=21 -I${TARGET}/usr/include
-I${TARGET}/include"  
ENV LDFLAGS "-pie -L${TARGET}/lib -L${TARGET}/usr/lib"  
ENV libdir ${TARGET}/lib  
  
ENV PKG_CONFIG_PATH ${TARGET}/lib/pkgconfig  
  
RUN mkdir -p ${build_dir} && \  
echo "# this one is important " > /toolchain/cmake.toolchain && \  
echo "SET(CMAKE_SYSTEM_NAME Android) " >> /toolchain/cmake.toolchain && \  
echo "#this one not so much " >> /toolchain/cmake.toolchain && \  
echo "SET(CMAKE_SYSTEM_VERSION 1)" >> /toolchain/cmake.toolchain && \  
echo "# specify the cross compiler " >> /toolchain/cmake.toolchain && \  
echo "SET(CMAKE_C_COMPILER ${host}-gcc) " >> /toolchain/cmake.toolchain && \  
echo "SET(CMAKE_CXX_COMPILER ${host}-g++)" >> /toolchain/cmake.toolchain  
  
COPY build.sh /root/build.sh  
COPY lock-obj-pub.* ${build_dir}/  
COPY libdjvulibre.patch ${build_dir}/  
  
RUN bash /root/build.sh  
  

