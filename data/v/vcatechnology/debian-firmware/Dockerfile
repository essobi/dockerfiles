FROM vcatechnology/debian-toolchain  
MAINTAINER VCA Technology <developers@vcatechnology.com>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG PROJECT_NAME  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="$PROJECT_NAME" \  
org.label-schema.description="An up-to-date Debian image to build VCA
firmware" \  
org.label-schema.url="https://www.debian.org/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/vcatechnology/docker-debian-
firmware" \  
org.label-schema.vendor="VCA Technology" \  
org.label-schema.version=$VERSION \  
org.label-schema.license=MIT \  
org.label-schema.schema-version="1.0"  
# Install packages  
RUN sudo vca-install-package \  
cpio dosfstools gdb isc-dhcp-server ovmf python3-pexpect python3-requests
squashfs-tools zip python3-pip  
RUN sudo pip3 install paramiko  

