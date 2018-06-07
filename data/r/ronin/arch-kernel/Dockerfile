FROM pritunl/archlinux:latest  
ARG VCS_REF  
ARG BUILD_DATE  
LABEL org.label-schema.description="Dockerfile to build linux kernel" \  
org.label-schema.version="0.0.2" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/ronin13/arch-kernel" \  
org.label-schema.build-date=$BUILD_DATE  
MAINTAINER Raghavendra Prabhu <me@rdprabhu.com>  
  
ARG VUID=1000  
RUN pacman -S --noconfirm base-devel wget kmod inetutils bc libelf  
RUN usermod -u $VUID -d /home/nobody -s /bin/bash nobody  
RUN install -d -m 0755 -o nobody /home/nobody  
  
WORKDIR /home/nobody  
USER nobody  
  
RUN wget -O -
https://git.archlinux.org/svntogit/packages.git/snapshot/packages-
packages/linux.tar.gz | tar zxf -  
WORKDIR packages-packages/linux/repos/core-x86_64  
  
ADD run.sh /run.sh  
ADD config.localmodconfig config.x86_64  
ADD PKGBUILD PKGBUILD  
  
VOLUME /deploy  
  
CMD ["/run.sh", "/deploy"]  
  

