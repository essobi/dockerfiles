FROM ubuntu:16.04  
ENV CARGO_HOME=/cargo \  
RUSTUP_HOME=/rustup \  
PATH=$PATH:/rust/bin:/cargo/bin  
#libstdc++6:i386  
RUN dpkg --add-architecture i386 && \  
dpkg --add-architecture amd64 && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
file \  
curl \  
ca-certificates \  
python \  
unzip \  
expect \  
openjdk-9-jre \  
lib32stdc++6 libstdc++6:amd64 libstdc++6-arm64-cross libstdc++6-armel-cross \  
gcc \  
libc6-dev \  
libpulse0:amd64 && \  
curl https://sh.rustup.rs -sSf | sh -s -- -y && \  
/cargo/bin/rustup toolchain install 1.17.0 && \  
/cargo/bin/rustup target list | grep android | xargs /cargo/bin/rustup target
install && \  
/cargo/bin/rustup target list | grep apple | xargs /cargo/bin/rustup target
install && \  
ln -s $(rustc --print sysroot) /rust  
  
COPY cargo_config /cargo/config  
  
WORKDIR /android/  
  
COPY install-ndk.sh /android/  
RUN sh /android/install-ndk.sh  
  
ENV PATH=$PATH:/android/ndk-arm/bin:/android/sdk/tools:/android/sdk/platform-
tools  
  
COPY install-sdk.sh accept-licenses.sh /android/  
RUN sh /android/install-sdk.sh  
  
ENV CARGO_TARGET_ARM_LINUX_ANDROIDEABI_LINKER=arm-linux-androideabi-gcc \  
ANDROID_EMULATOR_FORCE_32BIT=1 \  
HOME=/tmp  
RUN chmod 755 /android/sdk/tools/* /android/sdk/tools/qemu/linux-x86_64/*
/android/sdk/tools/qemu/linux-x86/*  
  
RUN cp -r /root/.android /tmp  
RUN chmod 777 -R /tmp/.android  

