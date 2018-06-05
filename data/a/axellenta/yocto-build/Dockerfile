# Base on Ubuntu 16.04 LTS  
FROM ubuntu:16.04  
# Yocto dependencies (for Yocto 2.2)  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -q update && \  
DEBIAN_FRONTEND="noninteractive" apt-get -qq install -y \  
gawk wget git-core diffstat unzip texinfo gcc-multilib \  
build-essential chrpath socat python3 \  
cpio python pkgconf && \  
apt-get -q clean -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
rm -f /var/cache/apt/*.bin && \  
find /usr/share/man -name "*.gz" | xargs rm -f && \  
locale-gen en_US.UTF-8  
  
# Set up locale to make Python and BitBake happy  
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'  
# Install sudo  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -q update && \  
DEBIAN_FRONTEND="noninteractive" apt-get -qq install -y sudo && \  
apt-get -q clean -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
rm -f /var/cache/apt/*.bin && \  
find /usr/share/man -name "*.gz" | xargs rm -f  
  
# A minimal init system for Linux containers  
# https://engineeringblog.yelp.com/2016/01/dumb-init-an-init-for-docker.html  
RUN wget -q -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64  
RUN chmod +x /usr/local/bin/dumb-init  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  
  
# Add group/user  
RUN groupadd -g 1000 buildgroup  
RUN useradd --create-home -d /var/build -s /bin/bash -u 1000 -g 1000 -G sudo
builduser  
  
# Allow sudo without password  
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
# Use bash instead of dash for /bin/sh  
RUN ln -sf bash /bin/sh  
  
USER builduser  
WORKDIR /var/build  

