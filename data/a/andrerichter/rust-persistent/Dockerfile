# -*- coding: utf-8 -*-  
#  
#
=============================================================================  
#  
# This is a template from:  
# https://www.github.com/andrerichter/docker-volume-permission-template  
#  
# Author(s):  
# Andre Richter, <andre.o.richter@gmail.com>  
#  
#
=============================================================================  
ARG RUSTUP_BASEIMAGE=rustlang/rust:nightly  
  
FROM $RUSTUP_BASEIMAGE  
  
MAINTAINER Andre Richter <andre.o.richter@gmail.com>  
  
ARG IMAGE_NAME=rust-persistent:nightly  
ENV IMAGE_NAME=$IMAGE_NAME  
  
ARG DEBIAN_FRONTEND=noninteractive  
ENV TERM=xterm-256color  
  
#
=============================================================================  
#  
# Additional useful packages  
#  
#
=============================================================================  
RUN set -ex; \  
apt-get update; \  
apt-get install -q -y --no-install-recommends \  
build-essential \  
gdb \  
gosu \  
sudo \  
xutils-dev \  
; \  
apt-get autoremove -q -y; \  
apt-get clean -q -y; \  
rm -rf /var/lib/apt/lists/*  
  
#
=============================================================================  
#  
# Wrapper for non-root login  
#  
#
=============================================================================  
COPY entrypoint.sh /usr/local/bin/  
COPY .bash_aliases /etc/skel/  
  
ENTRYPOINT ["bash", "entrypoint.sh"]  
CMD ["/bin/bash"]  

