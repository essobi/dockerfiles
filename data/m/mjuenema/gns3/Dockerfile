# Version: 1.0  
#  
# Based on  
#  
# * https://hub.docker.com/r/digiampietro/gns3-large  
# * https://community.gns3.com/message/28171#28171  
#  
# TODO:  
#  
# * replace hard-coded versions with placeholders and add  
# them to Dockerfile.sed.  
# * add more GNS3 related features and software.  
FROM centos:7  
MAINTAINER Markus Juenemann <markus@juenemann.net>  
  
  
# General update  
#  
RUN yum -y update  
  
# Install EPEL  
#  
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
  
# Needed RPM packages  
#  
RUN yum -y install sudo \  
tar \  
wget \  
curl \  
git \  
vim-enhanced \  
wireshark-gnome \  
cpulimit \  
telnet \  
python34 \  
python34-devel \  
python34-tools \  
gcc \  
gcc-c++ \  
make \  
cmake \  
elfutils-libelf-devel \  
uuid-devel \  
uuid-c++-devel \  
libuuid-devel \  
subversion \  
glibc-static \  
bison \  
flex \  
qemu \  
iptables \  
dnsmasq \  
uml-utilities \  
net-tools \  
libpcap-devel \  
qt5-qtbase-common \  
qt5-qtbase \  
qt5-qtbase-devel \  
qt5-qtsvg \  
qt5-qtbase-gui \  
qt5-qtsvg-devel  
  
# Download and install get-pip.py  
#  
RUN wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py && \  
python3.4 get-pip.py  
  
# Install some Python 3.4 packages  
#  
RUN pip3.4 install setuptools \  
psutil \  
raven \  
Jinja2  
  
## TODO: make version an ARG  
#RUN git clone https://github.com/docker/docker-py.git && \  
# cd docker-py && \  
# git checkout 2.0.2 && \  
# python3.4 setup.py install  
# SIP  
#  
COPY sip-4.17.tar.gz /  
RUN tar xvfz sip-4.17.tar.gz && \  
cd sip-4.17 && \  
python3.4 configure.py && \  
make && \  
make install && \  
cd / && \  
rm -rfv sip-4.17*  
  
# PyQt5 (disable unused modules)  
# Compiling this will take a while...  
#  
COPY PyQt-gpl-5.5.1.tar.gz /  
RUN tar xvfz PyQt-gpl-5.5.1.tar.gz && \  
cd PyQt-gpl-5.5.1 && \  
python3.4 configure.py --qmake /usr/lib64/qt5/bin/qmake \  
\--confirm-license \  
\--disable QtMultimedia \  
\--disable QtBluetooth \  
\--disable QtPositioning \  
\--disable Enginio \  
\--disable QtWebSockets \  
\--disable QtWebKit \  
\--disable QtWebKitWidgets \  
\--disable QtXml \  
\--disable QtSql \  
\--disable QtTest \  
\--disable QtOpenGL \  
\--disable QtPrintSupport \  
\--disable QtDBus && \  
make && \  
make install && \  
cd / && \  
rm -rfv PyQt-gpl-5.5.1*  
  
# Dynamips  
#  
ARG DYNAMIPSVERSION  
RUN git clone https://github.com/GNS3/dynamips.git && \  
cd dynamips && \  
git checkout ${DYNAMIPSVERSION} && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make && \  
make install && \  
cd / && \  
rm -rfv dynamips/  
  
# GNS3 Server  
#  
ARG GNS3VERSION  
RUN git clone https://github.com/GNS3/gns3-server.git && \  
cd gns3-server && \  
git checkout ${GNS3VERSION} && \  
python3.4 setup.py install && \  
cd / && \  
rm -rfv gns3-server/  
  
# GNS3 GUI  
#  
RUN git clone https://github.com/GNS3/gns3-gui.git && \  
cd gns3-gui && \  
git checkout ${GNS3VERSION} && \  
python3.4 setup.py install && \  
cd / && \  
rm -rfv gns3-gui/  
  
# VPCS  
#  
RUN svn checkout svn://svn.code.sf.net/p/vpcs/code/trunk vpcs && \  
cd vpcs/src && \  
./mk.sh 64 && \  
cp vpcs /usr/local/bin/ && \  
cd / && \  
rm -rfv vpcs/  
  
# iniparser  
#  
RUN git clone http://github.com/ndevilla/iniparser.git && \  
cd iniparser && \  
git checkout v4.0 && \  
make && \  
cp -v libiniparser.* /usr/lib && \  
cp -v src/*.h /usr/include && \  
cd / && \  
rm -rfv iniparser/  
  
# iouyap  
#  
RUN git clone https://github.com/GNS3/iouyap.git && \  
cd iouyap && \  
git checkout v0.96 && \  
make && \  
cp -v iouyap /usr/local/bin && \  
cd / && \  
rm -rfv ioyapp/  
  
# SSH server  
#  
RUN yum install -y openssh-server xauth && \  
yum clean all && \  
ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa && \  
ssh-keygen -f /etc/ssh/ssh_host_dsa_key -N '' -t dsa && \  
ssh-keygen -f /etc/ssh/ssh_host_ecdsa_key -N '' -t ecdsa -b 521 && \  
date | md5sum | cut -d' ' -f 1 > /etc/machine-id  
  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd \  
&& mkdir -p /var/run/sshd \  
&& useradd -u 1000 -m -s /bin/bash gns3 \  
&& echo "gns3:gns3" | chpasswd  
  
# Standard SSH port  
EXPOSE 22  
COPY entrypoint.sh /entrypoint.sh  
CMD /entrypoint.sh  
  
# Fix permissions  
#  
RUN chmod u+x /usr/local/bin/*  
  
# Fonts  
#  
RUN yum -y groupinstall fonts && \  
yum clean all  
  
# Bridge utils  
#  
RUN yum -y install bridge-utils tunctl && \  
yum clean all  
  
# Sudo  
#  
RUN echo 'gns3 ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  

