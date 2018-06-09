FROM phusion/baseimage  
  
#=============================================================================  
# Install ROS Kinetic  
#=============================================================================  
# setup keys  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
421C365BD9FF1F717815A3895523BAEEB01FA116  
  
# setup sources.list  
RUN echo "deb http://packages.ros.org/ros/ubuntu xenial main" >
/etc/apt/sources.list.d/ros-latest.list  
  
# install bootstrap tools  
RUN apt-get update && apt-get install --no-install-recommends -y \  
python-rosdep \  
python-rosinstall \  
python-vcstools \  
&& rm -rf /var/lib/apt/lists/*  
  
# setup environment  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
# bootstrap rosdep  
RUN rosdep init \  
&& rosdep update  
  
# install ros packages  
ENV ROS_DISTRO kinetic  
RUN apt-get update && apt-get install -y \  
ros-kinetic-ros-core=1.3.1-0* \  
ros-kinetic-ros-base=1.3.1-0* \  
ros-kinetic-perception=1.3.1-0* \  
&& rm -rf /var/lib/apt/lists/*  
  
#=============================================================================  
# Install SGX  
#=============================================================================  
COPY ./patches /patches  
  
RUN apt-get update -q -q && \  
apt-get install wget python git patch build-essential ocaml automake autoconf
libtool libssl-dev libcurl4-openssl-dev protobuf-compiler protobuf-c-compiler
libprotobuf-dev libprotobuf-c0-dev alien uuid-dev libxml2-dev cmake pkg-config
--yes --force-yes && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /tmp/icls && \  
cd /tmp/icls && \  
wget http://registrationcenter-
download.intel.com/akdlm/irc_nas/11414/iclsClient-1.45.449.12-1.x86_64.rpm &&
\  
alien --scripts iclsClient-1.45.449.12-1.x86_64.rpm && \  
dpkg -i iclsclient_1.45.449.12-2_amd64.deb && \  
rm -rf /tmp/icls  
  
RUN cd /tmp && \  
git clone https://github.com/01org/dynamic-application-loader-host-
interface.git && \  
cd /tmp/dynamic-application-loader-host-interface && \  
cmake . && \  
make && \  
make install && \  
rm -rf /tmp/dynamic-application-loader-host-interface  
  
RUN cd /tmp && \  
git clone https://github.com/01org/linux-sgx.git && \  
cd / && \  
for patch in /patches/*; do patch --prefix=/patches/ -p0 --force "--
input=$patch" || exit 1; done && \  
rm -rf /patches && \  
cd /tmp/linux-sgx && \  
./download_prebuilt.sh  
  
RUN cd /tmp/linux-sgx && \  
make && \  
make sdk_install_pkg && \  
make psw_install_pkg  
  
RUN mkdir -p /opt/intel && \  
cd /opt/intel && \  
yes yes | /tmp/linux-sgx/linux/installer/bin/sgx_linux_x64_sdk_*.bin && \  
/tmp/linux-sgx/linux/installer/bin/sgx_linux_x64_psw_*.bin && \  
rm -rf /tmp/linux-sgx  
  
COPY ./etc /etc  

