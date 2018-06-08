#  
# Zephyr Build Container  
#  
# https://github.com/dockerfile/ubuntu  
#  
# Pull base image.  
FROM ubuntu:16.04  
# Install.  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget && \  
apt-get install -y git make gcc g++ python3-ply ncurses-dev lib32z1
lib32ncurses5 && \  
apt-get install -y python python-yaml python-requests python-zmq ccache
python-pip && \  
pip install pycrypto && \  
mkdir -p /root/.ssh && \  
mkdir -p /mnt/artifacts && \  
rm -rf /var/lib/apt/lists/*  
  
# Setup Build Enviroment  
ENV LANG C  
ENV ZEPHYR_BASE /root/zephyr-project  
ENV GCCARMEMB_TOOLCHAIN_PATH /root/gcc-arm-none-eabi-5_4-2016q2  
ENV ZEPHYR_GCC_VARIANT gccarmemb  
ENV CROSS_COMPILE /root/gcc-arm-none-eabi-5_4-2016q2/bin/arm-none-eabi-  
  
# Pull GCC ARM Embedded Toolchain.  
RUN \  
cd /root && \  
wget https://launchpad.net/gcc-arm-
embedded/5.0/5-2016-q2-update/+download/gcc-arm-none-
eabi-5_4-2016q2-20160622-linux.tar.bz2 && \  
tar -C . -xaf gcc-arm-none-eabi-5_4-2016q2-20160622-linux.tar.bz2  
  
# Setup Zephyr Mirror  
RUN \  
mkdir -p /srv/mirrors && \  
cd /srv/mirrors && \  
git clone \--mirror https://gerrit.zephyrproject.org/r/zephyr zephyr-mirror  
  
# Add files.  
ADD root/.bashrc /root/.bashrc  
ADD root/.gitconfig /root/.gitconfig  
ADD root/.scripts /root/.scripts  
  
# Set environment variables.  
ENV HOME /root  
ENV USE_CCACHE 1  
# Define working directory.  
WORKDIR /root  
  
# Copy build script  
COPY build-test-zephyr.sh /root/build-test-zephyr.sh  
# Copy LAVA helpers  
COPY *.yaml /root/  
COPY submityaml.py /root/submityaml.py  
COPY logger.py /root/logger.py  
# Copy Image Signing Helpers  
COPY newtimg.py /root/newtimg.py  
COPY zep2newt.py /root/zep2newt.py  
COPY image_sign.pem /root/image_sign.pem  
# Copy Hawkbit Helpers  
COPY hawkbit.py /root/hawkbit.py  
  
# Setup Keys  
COPY id_rsa /root/.ssh/id_rsa  
COPY id_rsa.pub /root/.ssh/id_rsa.pub  
COPY config /root/.ssh/config  
RUN \  
chmod 600 /root/.ssh/id_rsa  
  
# Fill ccache  
RUN \  
cd /root && \  
git clone /srv/mirrors/zephyr-mirror zephyr-project && \  
cd zephyr-project && \  
ccache -M 50G && \  
/bin/bash -c "source zephyr-env.sh && sanitycheck --platform qemu_cortex_m3
--build-only --enable-slow --no-clean --testcase-root=tests" && \  
cd /root && \  
rm -rf zephyr-project  
  
# Define default command.  
CMD ./build-test-zephyr.sh  

