FROM fedora:20  
MAINTAINER AJ Christensen (aj@junglist.io)  
  
# Use yum to prep the container.  
RUN yum install -y \  
gcc \  
gcc-c++ \  
qt5*devel \  
glibc.i686 \  
libstdc++.i686 \  
java-1.8.0-openjdk-devel \  
libusb-devel \  
systemd-devel \  
gtest \  
astyle \  
make \  
wget \  
git \  
bzip2 \  
expect  
  
# Makefiles all expect qmake to point to qmake-qt5  
RUN ln -sfv /usr/bin/qmake-qt5 /usr/bin/qmake  
  
# Copy the current work directory source code  
ADD . /taulabs  
  
WORKDIR /taulabs  
  
RUN useradd -d /taulabs -M -s /bin/bash taulabs -U  
RUN chown -Rc taulabs: .  
RUN echo '%taulabs ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/taulabs  
USER taulabs  
  
RUN make arm_sdk_install  
  
RUN make android_sdk_install  
RUN make/scripts/expect-update-sdk  
  
# Make sure you run this container with a memory limit  
# RUN make -j package  
RUN make all_clean  
RUN make -j all_colibri  

