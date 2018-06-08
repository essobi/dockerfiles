FROM ubuntu:16.04  
  
ARG DEBIAN_FRONTEND=noninteractive  
ARG DEV_USER_NAME=Genesis  
ARG DEV_USER=genesis-dev  
ARG DEV_USER_PASSWD=genesis  
  
# Packages needed or useful for Genesis development.  
#  
# We manage most these in a PPA, and keep them installed. Some Python  
# dependencies can't be satisfied with Ubuntu 16.04 packages, and are  
# installed via pip3.  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
software-properties-common \  
&& add-apt-repository ppa:osf-maintainers/ppa \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends zmp-dev \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip3 install --system pyelftools  
  
# Add CI dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
iproute2 \  
net-tools \  
python3-requests \  
qemu-system-arm \  
socat \  
wget \  
&& wget -O /tmp/install-rust.sh https://sh.rustup.rs \  
&& chmod +x /tmp/install-rust.sh \  
&& apt-get install -y --no-install-recommends curl \  
&& /tmp/install-rust.sh -y \  
&& easy_install3 pykwalify \  
&& apt-get purge -y --auto-remove curl \  
&& rm /tmp/install-rust.sh \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Create the user which will run the SDK binaries.  
RUN useradd -c $DEV_USER_NAME \  
-d /home/$DEV_USER \  
-G sudo,dialout,floppy,plugdev,users \  
-m \  
-s /bin/bash \  
$DEV_USER  
  
# Add default password for the SDK user (useful with sudo)  
RUN echo $DEV_USER:$DEV_USER_PASSWD | chpasswd  
  
# Initialize development environment for $DEV_USER.  
RUN sudo -u $DEV_USER -H git config --global credential.helper 'cache
--timeout=3600'  

