  
FROM ubuntu:16.10  
LABEL maintainer="takahasi <3263ta@gmail.com>" \  
description="OpenRTM on Docker: OpenRTM-aist on Docker images." \  
build_type="ubuntu-all"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN set -x && \  
apt-get update -qq  
  
RUN apt-get install -y curl \  
bc \  
bsdmainutils \  
apt-utils \  
aptitude \  
iputils-ping \  
net-tools \  
subversion \  
git \  
cmake \  
libopencv-dev \  
python-pip \  
python-tk \  
default-jre &&\  
curl -O http://svn.openrtm.org/OpenRTM-aist/tags/RELEASE_1_1_2/OpenRTM-
aist/build/pkg_install_ubuntu.sh && \  
chmod a+x pkg_install_ubuntu.sh && sync && \  
./pkg_install_ubuntu.sh -c && \  
curl -O http://svn.openrtm.org/OpenRTM-aist-Python/tags/RELEASE_1_1_2/OpenRTM-
aist-Python/installer/install_scripts/pkg_install_python_ubuntu.sh && \  
chmod a+x pkg_install_python_ubuntu.sh && sync && \  
./pkg_install_python_ubuntu.sh -y && \  
pip install -U pip && \  
pip install rtshell && \  
rtshell_post_install -n && \  
curl -O
http://openrtm.org/pub/openrtp/packages/1.1.2.v20160526/eclipse442-openrtp112v20160526-linux-
gtk-x86_64.tar.gz && \  
tar xzf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \  
rm -rf eclipse442-openrtp112v20160526-linux-gtk-x86_64.tar.gz && \  
ln -s /eclipse/openrtp /usr/bin/ && \  
svn export http://svn.openrtm.org/ImageProcessing/trunk/ImageProcessing/ && \  
cd ImageProcessing/opencv/components/ && mkdir -p build && cd build && \  
cmake -DCMAKE_INSTALL_PREFIX=/usr.. && make install && cd /  
  
RUN apt-get autoclean -y && \  
apt-get autoremove -y  
  
ENTRYPOINT ["/bin/bash", "-c"]  

