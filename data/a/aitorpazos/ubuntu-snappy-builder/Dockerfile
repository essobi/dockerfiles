# This Dockerfile builds an image that builds Ubuntu Snappy for x86, x86_64,
armhf and arm64  
FROM ubuntu:wily  
MAINTAINER Aitor Pazos <mail@aitorpazos.es>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
golang-go \  
gcc-5-multilib \  
gcc-5-arm-linux-gnueabihf \  
gcc-5-aarch64-linux-gnu \  
git \  
bzr \  
sudo  
COPY sudoers /etc/sudoers  
COPY snappyBuilder /opt/  
RUN chown -c root:root /etc/sudoers && \  
chmod -c 0440 /etc/sudoers && \  
chmod a+rx /opt/snappyBuilder && \  
mkdir -p /work && \  
ln -s /usr/include/asm-generic /usr/include/asm  
VOLUME /work  
WORKDIR /work  
ENV USER_UID 1000  
ENV SNAPPY_BASE github.com/ubuntu-core/snappy  
# Supported SNAPPY_ARCH values: 386 amd64 armhf arm64  
ENV SNAPPY_ARCH amd64  
ENV SNAPPY_ARM_VER 7  
CMD useradd -u ${USER_UID} -d /home/snappy -m snappy && \  
chown -R snappy /work /home/snappy && \  
su -l snappy --preserve-environment -c "cd /work && /bin/bash
/opt/snappyBuilder"  

