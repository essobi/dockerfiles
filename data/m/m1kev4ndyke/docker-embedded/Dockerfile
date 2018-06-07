FROM debian:stretch  
  
RUN apt-get update && \  
apt-get install -y build-essential \  
git \  
cmake \  
gcc \  
python \  
gcc-arm-none-eabi \  
libnewlib-arm-none-eabi \  
qemu-system-arm \  
gcovr \  
wget \  
openjdk-8-jdk \  
unzip \  
zip \  
pkg-config \  
zlib1g-dev \  
&& \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR home/tools/aarch64-toolchain  
RUN wget -q
https://releases.linaro.org/components/toolchain/binaries/7.1-2017.08/aarch64-elf/gcc-
linaro-7.1.1-2017.08-x86_64_aarch64-elf.tar.xz && \  
tar xf gcc-linaro-7.1.1-2017.08-x86_64_aarch64-elf.tar.xz && \  
rm -f gcc-linaro-7.1.1-2017.08-x86_64_aarch64-elf.tar.xz  
  
WORKDIR home/tools/bazel  
RUN wget -q
https://github.com/bazelbuild/bazel/releases/download/0.9.0/bazel-0.9.0-installer-
linux-x86_64.sh && \  
chmod +x bazel-0.9.0-installer-linux-x86_64.sh && \  
./bazel-0.9.0-installer-linux-x86_64.sh && \  
rm -f bazel-0.9.0-installer-linux-x86_64.sh  
  
ENV PATH "$PATH:$HOME/bin:/home/tools/aarch64-toolchain/gcc-
linaro-6.3.1-2017.02-x86_64_aarch64-elf/bin"  

