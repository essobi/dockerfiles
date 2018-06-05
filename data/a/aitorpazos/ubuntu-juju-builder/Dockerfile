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
COPY jujuBuilder /opt/  
RUN chown -c root:root /etc/sudoers && \  
chmod -c 0440 /etc/sudoers && \  
chmod a+rx /opt/jujuBuilder && \  
mkdir -p /work && \  
ln -s /usr/include/asm-generic /usr/include/asm  
VOLUME /work  
WORKDIR /work  
ENV USER_UID 1000  
ENV JUJU_BASE github.com/juju/juju/  
ENV JUJU_CMD ${JUJU_BASE}...  
# Supported JUJU_ARCH values: 386 amd64 armhf arm64  
ENV JUJU_ARCH amd64  
ENV JUJU_ARM_VER 7  
CMD useradd -u ${USER_UID} -d /home/juju -m juju && \  
chown -R juju /work /home/juju && \  
su -l juju --preserve-environment -c "cd /work && /bin/bash /opt/jujuBuilder"  

