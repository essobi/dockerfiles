FROM vcatechnology/fedora-toolchain  
MAINTAINER VCA Technology <developers@vcatechnology.com>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG PROJECT_NAME  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="$PROJECT_NAME" \  
org.label-schema.description="An up-to-date Fedora image to build VCA
firmwared" \  
org.label-schema.url="https://getfedora.org/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/vcatechnology/docker-fedora-
firmware" \  
org.label-schema.vendor="VCA Technology" \  
org.label-schema.version=$VERSION \  
org.label-schema.license=MIT \  
org.label-schema.schema-version="1.0"  
# Install packages  
RUN sudo vca-install-package \  
dhcp-server dosfstools edk2-ovmf fakeroot gdb python3-pexpect python3-requests
squashfs-tools  

