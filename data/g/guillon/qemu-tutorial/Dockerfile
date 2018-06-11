FROM ubuntu:14.04  
#  
# Image for QEMU Tutorial  
#  
# Ref to README.md file  
#  
MAINTAINER Christophe Guillon <christophe.guillon@st.com>  
  
# Basic net and development tools  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y ssl-cert wget curl \  
telnet openssh-client net-tools iputils-ping sudo && \  
apt-get install -y build-essential gcc clang python perl zip git-core && \  
apt-get install -y emacs24-nox vim-nox  
  
# QEMU base dependencies  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get install -y pkg-config \  
zlib1g-dev libglib2.0-dev libpixman-1-dev libfdt-dev  
  
# QEMU additional optional dependencies  
RUN cd /tmp && rm -f *.deb && \  
wget http://www.capstone-engine.org/download/3.0.4/ubuntu-14.04/libcapstone-
dev_3.0.4-0.1ubuntu1_amd64.deb && \  
wget http://www.capstone-
engine.org/download/3.0.4/ubuntu-14.04/libcapstone3_3.0.4-0.1ubuntu1_amd64.deb
&& \  
wget http://www.capstone-engine.org/download/3.0.4/ubuntu-14.04/python-
capstone_3.0.4-0.1ubuntu1_amd64.deb && \  
dpkg -i *.deb && rm -f *.debs  
  
# Setup sudo rule  
RUN echo '%sudo ALL=(ALL:ALL) NOPASSWD:ALL' >>/etc/sudoers.d/group-sudo && \  
chmod 440 /etc/sudoers.d/group-sudo  
  
# Add hacker user  
RUN adduser --gecos '' \--disabled-password --disabled-login hacker && \  
adduser hacker sudo  
  
USER hacker  
WORKDIR /home/hacker  
  
RUN wget -q -O qemu-plugins-next-master.zip https://github.com/guillon/qemu-
plugins/archive/next/master.zip && \  
unzip qemu-plugins-next-master.zip && \  
rm -f qemu-plugins-next-master.zip  
  
RUN cd qemu-plugins-next-master && \  
./configure --disable-werror --enable-capstone --enable-tcg-plugin \  
\--target-list=x86_64-linux-user,arm-linux-user,aarch64-linux-user,arm-softmmu
--prefix=$PWD/devimage  
  
RUN cd qemu-plugins-next-master && \  
make -j4 && \  
make install  
  
VOLUME /home/hacker  
  
ENV PATH=/home/hacker/qemu-plugins-next-master/devimage/bin:/home/hacker/qemu-
tutorial/scripts:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
COPY qemu-tutorial/ /qemu-tutorial  
COPY entrypoint.sh /  
COPY README.md /  
COPY Dockerfile /  
  
ENTRYPOINT [ "/entrypoint.sh" ]  

